#!/usr/bin/env python3
"""Interactive installer for claude-toolkit plugins.

Discovers plugins automatically, lets users pick which to install,
and registers them into the local-plugins marketplace for Claude Code.
"""

import json
import os
import platform
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

TOOLKIT_DIR = Path(__file__).resolve().parent
CLAUDE_DIR = Path.home() / ".claude"
PLUGINS_DIR = CLAUDE_DIR / "plugins"
MARKETPLACE_DIR = PLUGINS_DIR / "marketplaces" / "local-plugins"
MARKETPLACE_PLUGINS_DIR = MARKETPLACE_DIR / "plugins"
MARKETPLACE_JSON = MARKETPLACE_DIR / ".claude-plugin" / "marketplace.json"

BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
RESET = "\033[0m"

NO_COLOR = os.environ.get("NO_COLOR") is not None or not sys.stdout.isatty()
if NO_COLOR:
    BOLD = DIM = GREEN = YELLOW = RED = CYAN = RESET = ""


def discover_plugins() -> list[dict]:
    """Find all plugin directories containing .claude-plugin/plugin.json."""
    plugins = []
    for entry in sorted(TOOLKIT_DIR.iterdir()):
        plugin_json = entry / ".claude-plugin" / "plugin.json"
        if not plugin_json.is_file():
            continue
        meta = json.loads(plugin_json.read_text())
        skill_dir = entry / "skills"
        skill_count = (
            len(list(skill_dir.glob("*/SKILL.md"))) if skill_dir.is_dir() else 0
        )
        plugins.append(
            {
                "name": entry.name,
                "path": entry,
                "description": meta.get("description", ""),
                "skills": skill_count,
            }
        )
    return plugins


def read_marketplace() -> dict:
    """Read the current marketplace.json, creating it if needed."""
    if MARKETPLACE_JSON.is_file():
        return json.loads(MARKETPLACE_JSON.read_text())
    return {
        "name": "local-plugins",
        "description": "Locally installed plugins",
        "owner": {"name": "local"},
        "plugins": [],
    }


def get_marketplace_plugin_names() -> set[str]:
    """Return set of plugin names currently registered in marketplace."""
    manifest = read_marketplace()
    return {p["name"] for p in manifest.get("plugins", [])}


def get_install_status(plugin_name: str) -> str:
    """Return install status: 'installed', 'stale', 'registered', or 'not installed'."""
    target = MARKETPLACE_PLUGINS_DIR / plugin_name
    registered = plugin_name in get_marketplace_plugin_names()

    if target.is_symlink():
        actual = target.resolve()
        expected = TOOLKIT_DIR / plugin_name
        if actual == expected:
            return "installed" if registered else "linked"
        return "stale"
    if target.is_dir():
        return "registered" if registered else "local"
    return "not installed"


def prompt_selection(plugins: list[dict]) -> list[dict]:
    """Interactive multi-select: users toggle plugins with numbers."""
    selected = [True] * len(plugins)

    while True:
        print(f"\n{BOLD}Available plugins:{RESET}\n")
        for i, plugin in enumerate(plugins):
            status = get_install_status(plugin["name"])
            marker = f"{GREEN}x{RESET}" if selected[i] else " "
            status_label = ""
            if status == "installed":
                status_label = f" {GREEN}(installed){RESET}"
            elif status in ("stale", "linked"):
                status_label = f" {YELLOW}({status}){RESET}"
            print(
                f"  [{marker}] {BOLD}{i + 1}{RESET}. {plugin['name']}"
                f" {DIM}({plugin['skills']} skills){RESET}{status_label}"
            )
            desc = plugin["description"]
            if len(desc) > 80:
                desc = desc[:77] + "..."
            print(f"      {DIM}{desc}{RESET}")

        print(
            f"\n{DIM}Toggle: enter numbers (e.g. 1 3). "
            f"'a' = select all, 'n' = select none.{RESET}"
        )
        answer = input(f"{BOLD}Confirm selection? [Y/toggle]: {RESET}").strip().lower()

        if answer in ("", "y", "yes"):
            break
        if answer == "a":
            selected = [True] * len(plugins)
            continue
        if answer == "n":
            selected = [False] * len(plugins)
            continue
        for token in answer.replace(",", " ").split():
            if token.isdigit():
                idx = int(token) - 1
                if 0 <= idx < len(plugins):
                    selected[idx] = not selected[idx]

    return [p for p, s in zip(plugins, selected) if s]


def ensure_marketplace_exists() -> None:
    """Create the local-plugins marketplace structure if it doesn't exist."""
    MARKETPLACE_PLUGINS_DIR.mkdir(parents=True, exist_ok=True)
    MARKETPLACE_JSON.parent.mkdir(parents=True, exist_ok=True)
    if not MARKETPLACE_JSON.is_file():
        manifest = {
            "name": "local-plugins",
            "description": "Locally installed plugins",
            "owner": {"name": "local"},
            "plugins": [],
        }
        MARKETPLACE_JSON.write_text(json.dumps(manifest, indent=2) + "\n")

    known_marketplaces_file = PLUGINS_DIR / "known_marketplaces.json"
    if known_marketplaces_file.is_file():
        known = json.loads(known_marketplaces_file.read_text())
    else:
        known = {}

    if "local-plugins" not in known:
        known["local-plugins"] = {
            "source": {"source": "directory", "path": str(MARKETPLACE_DIR)},
            "installLocation": str(MARKETPLACE_DIR),
            "lastUpdated": datetime.now(timezone.utc).isoformat(),
        }
        known_marketplaces_file.write_text(json.dumps(known, indent=2) + "\n")
        print(f"  {GREEN}INIT{RESET}    Registered local-plugins marketplace")


def install(plugins: list[dict]) -> None:
    """Symlink selected plugins into local-plugins marketplace and register them."""
    ensure_marketplace_exists()
    manifest = read_marketplace()
    existing_names = {p["name"] for p in manifest["plugins"]}

    print(f"\n{BOLD}Installing to local-plugins marketplace{RESET}")
    print(f"{DIM}{MARKETPLACE_PLUGINS_DIR}{RESET}\n")

    for plugin in plugins:
        source = plugin["path"]
        target = MARKETPLACE_PLUGINS_DIR / plugin["name"]

        if target.is_symlink():
            target.unlink()
        elif target.is_dir():
            backup = target.with_suffix(f".bak.{os.getpid()}")
            shutil.move(str(target), str(backup))
            print(f"  {YELLOW}BACKUP{RESET}  {target.name} -> {backup.name}")

        target.symlink_to(source, target_is_directory=True)
        print(f"  {GREEN}LINK{RESET}    {plugin['name']} -> {source}")

        if plugin["name"] not in existing_names:
            manifest["plugins"].append(
                {
                    "name": plugin["name"],
                    "description": plugin["description"],
                    "source": f"./plugins/{plugin['name']}",
                }
            )
            print(f"  {GREEN}ADD{RESET}     {plugin['name']} -> marketplace.json")

    MARKETPLACE_JSON.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"\n{GREEN}Done. {len(plugins)} plugin(s) added to local-plugins.{RESET}")
    print(f"\n{BOLD}Next steps:{RESET}")
    print(
        f"  Run {CYAN}/reload-plugins{RESET} in Claude Code, then install each plugin:"
    )
    for plugin in plugins:
        name = plugin["name"]
        print(f"    {CYAN}/plugin install {name}@local-plugins{RESET}")


def uninstall() -> None:
    """Remove toolkit symlinks from marketplace and deregister from manifest."""
    if not MARKETPLACE_PLUGINS_DIR.is_dir():
        print("Nothing to uninstall.")
        return

    manifest = read_marketplace()
    removed = 0
    remaining_plugins = []

    for entry in MARKETPLACE_PLUGINS_DIR.iterdir():
        if entry.is_symlink() and entry.resolve().is_relative_to(TOOLKIT_DIR):
            entry.unlink()
            print(f"  {RED}REMOVE{RESET}  {entry.name}")
            removed += 1
        else:
            remaining_plugins.append(entry.name)

    manifest["plugins"] = [
        p for p in manifest["plugins"] if p["name"] in remaining_plugins
    ]
    MARKETPLACE_JSON.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"\nRemoved {removed} plugin(s) from local-plugins marketplace.")
    if removed > 0:
        print(
            f"\n{BOLD}Next:{RESET} Run {CYAN}/reload-plugins{RESET} in Claude Code to apply."
        )


def show_status(plugins: list[dict]) -> None:
    """Print a status table of all discovered plugins."""
    print(f"\n{BOLD}Toolkit:{RESET}     {TOOLKIT_DIR}")
    print(f"{BOLD}Marketplace:{RESET} {MARKETPLACE_DIR}")
    print(f"{BOLD}System:{RESET}      {platform.system()} {platform.machine()}\n")

    header = f"{'PLUGIN':<20} {'STATUS':<14} {'SKILLS':<8} PATH"
    print(f"{BOLD}{header}{RESET}")
    print("-" * 70)

    for plugin in plugins:
        status = get_install_status(plugin["name"])
        color = {
            "installed": GREEN,
            "stale": YELLOW,
            "linked": YELLOW,
            "registered": CYAN,
            "local": YELLOW,
            "not installed": DIM,
        }.get(status, "")
        print(
            f"{plugin['name']:<20} {color}{status:<14}{RESET} "
            f"{plugin['skills']:<8} {DIM}{plugin['path']}{RESET}"
        )


def main() -> None:
    """Entry point: parse command and run."""
    plugins = discover_plugins()
    if not plugins:
        print(f"{RED}No plugins found in {TOOLKIT_DIR}{RESET}")
        sys.exit(1)

    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command == "install":
        selected = prompt_selection(plugins)
        if not selected:
            print("No plugins selected.")
            return
        install(selected)
    elif command == "uninstall":
        uninstall()
    elif command == "status":
        show_status(plugins)
    else:
        print(f"{BOLD}claude-toolkit installer{RESET}\n")
        print(f"Usage: {sys.argv[0]} {{install|uninstall|status}}\n")
        print("  install    Add plugins to local-plugins marketplace")
        print("  uninstall  Remove toolkit plugins from marketplace")
        print("  status     Show current installation status")
        sys.exit(1 if command is not None else 0)


if __name__ == "__main__":
    main()
