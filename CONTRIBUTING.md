# Contributing

Thanks for your interest in contributing to claude-toolkit!

## Adding a Skill

1. Create a directory under the appropriate plugin: `claude-<plugin>/skills/<skill-name>/`
2. Add a `SKILL.md` with YAML frontmatter (`name`, `description`) and the skill prompt
3. Run `/reload-plugins` in Claude Code to pick up the new skill
4. Test it with `/<plugin-name>:<skill-name>`

See the [Claude Code plugin docs](https://docs.anthropic.com/en/docs/claude-code/plugins) for the full skill specification.

## Reporting Issues

Open a [GitHub issue](../../issues) with:
- What you expected to happen
- What actually happened
- Steps to reproduce

## Submitting a PR

1. Fork the repo and create a feature branch
2. Keep changes focused — one skill or fix per PR
3. Test your skill in Claude Code before submitting
4. Open a PR with a clear description of the change

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
