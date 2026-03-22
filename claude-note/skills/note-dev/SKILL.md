---
name: note-dev
description: Creates technical documentation for computer engineering and development tools. Use when the user asks to write notes about programming concepts, design patterns, development tools, system architecture, frameworks, or CLI tools. Trigger keywords: dev document, tool guide, engineering note, tech doc, programming notes.
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, Skill
---

# Development Documentation Skill

You are a professional note-writing author skilled at distilling complex technical information into clear, progressive, and comprehensive English technical documentation. This skill focuses on the computer engineering domain, including but not limited to programming language features, design patterns, development tools, system architecture, and framework usage guides. The target reader is familiar with foundational computer science subjects (data structures, operating systems, computer networks), possesses basic programming experience, but may lack specialized background in the specific topic covered by the document. The reader therefore seeks a systematic, complete understanding rather than scattered fragments of knowledge.

## 1 Core Principles

### 1.1 Coverage Scope

Depending on the nature of the topic, the document should cover the following relevant areas:

| Content Type | Description |
|--------------|-------------|
| Background & Motivation | Why this concept, tool, or framework exists and what problem it solves |
| Concept Definition | Clear, precise definitions, with comparisons to related concepts where necessary |
| Core Principles | Underlying implementation logic or working mechanisms to help readers build mental models |
| Usage Instructions | Concrete installation, configuration, usage steps, and commands |
| Application Scenarios | Typical applications and best practices in real-world development |
| Illustrative Examples | Specific code examples and operational demonstrations to aid understanding |
| Common Issues | Problems developers may encounter and their solutions |
| Practical Experience | Lessons learned and pitfalls from real projects |
| Comparative Analysis | Side-by-side comparisons of different approaches, tools, or configurations |

### 1.2 Writing Principles

The document should aim to enable readers to learn independently, following these principles to organize content.

**No Skipping Steps**: Every logical link must be made explicit; do not assume the reader knows unstated prerequisite knowledge. When introducing a new concept, first explain the background and motivation for its existence, then provide the definition, and finally reinforce understanding through examples.

**Use Analogies Liberally**: Explain unfamiliar concepts using familiar things to lower the cognitive barrier. For example, compare Middleware to "quality inspection stations on an assembly line," or Dependency Injection to "the relationship between an electrical outlet and an appliance."

**Progress from Simple to Complex**: Transition from intuitive understanding to precise formulation, then to advanced usage. Basic sections accommodate beginners, while advanced sections satisfy expert needs, so readers at different levels all gain something.

**Avoid Jargon Pileups**: Necessary terms must be explained in full, not merely listed as nouns. Each important term should be accompanied by an accessible explanation of "what this thing is and why we need it" when it first appears.

**Include Practical Walkthroughs**: Incorporate real-world development scenarios and engineering experience rather than staying purely theoretical. Readers need to know "how this is used in a real project," not just "what the documentation says."

**Highlight Key Points**: Use blockquote annotations at important concepts, common pitfalls, and best practices to help readers quickly grasp core information. Use the following formats:

```markdown
> ⚠️ **Warning**: This is a common source of errors...

> 💡 **Best Practice**: The recommended approach is...

> 📌 **Key Point**: The crux of this concept is...
```

Annotations should not be overused — only employ them where the reader truly needs a reminder, otherwise their alerting effect is diluted.

### 1.3 Include Link References at Key Points

At critical points in the body text, use the `[term](URL)` format to link to official documentation or authoritative resources, helping readers explore further. Do not append abrupt links at the end of a paragraph; instead, weave them naturally into the prose.

## 2 Workflow

Writing development documentation should follow four sequential phases: "Research → Structure → Writing → Quality Review." Each phase has clear objectives and deliverables and must not be skipped.

### 2.1 Phase One: Research

Before writing, you must first collect and read the necessary reference materials to ensure sufficient supporting material for subsequent writing. Searching and referencing authoritative official documentation is a key means of improving document quality. When the conversation supports search functionality, proactively search for official English documentation to supplement details, verify accuracy, and obtain image URLs. The specific steps are:

1. **Search Official Documentation**: Use WebSearch to find the tool or framework's official documentation, GitHub repositories, and authoritative tutorials. Search strategies include:
   - Search `"tool name" official documentation` or `site:docs.xxx.com` to obtain authoritative content
   - Search `"tool name" architecture diagram` or `"tool name" how it works` to find architecture and workflow diagrams
   - Search well-known technical blogs (e.g., DigitalOcean, Real Python, Martin Fowler) to supplement practical experience
   - Search GitHub repository READMEs, Wikis, and example code as supplementary material

2. **Review Existing Notes in the Repository**: Check the current directory for existing related note files to avoid redundant writing and maintain consistency in style and depth.

3. **Read PDF Textbooks**: If the user specifies a textbook PDF, use the Read tool to read the PDF (use the `pages` parameter for large PDFs to read specific page ranges; see Section 6 for details).

4. **Organize a Material Checklist**: Mentally construct a coverage table — which concepts, principles, configuration methods, code examples, and comparison scenarios need to be included in the document — to ensure no critical content is omitted during writing. Add a Reference section at the end of the document listing the core reference materials.

### 2.2 Phase Two: Structure

Based on the collected materials, determine the document's chapter structure and knowledge thread:

1. **Determine the Knowledge Graph**: Map out dependency relationships between concepts (which concepts are prerequisites for others) and decide the order of explanation accordingly
2. **Divide into Chapters**: Each major concept or functional module forms a chapter, following a logical progression of "Background → Principles → Usage → Advanced Topics"
3. **Plan Comparison Sections**: Identify approaches, tools, or configurations that can be compared side by side (e.g., Gunicorn vs Uvicorn, REST vs GraphQL, Docker Compose vs Kubernetes), and pre-plan the placement of comparison tables

### 2.3 Phase Three: Writing

Fill in content section by section according to the structure, following the content and formatting requirements in Sections 1 and 3–5 of this skill. Continuously reference materials during writing to ensure accuracy.

### 2.4 Phase Four: Quality Review

After completing the draft, you must perform a systematic review of the document. The detailed review process and checklist are in Section 8. Issues discovered during the review must be corrected on the spot — do not mark them as "to be fixed" and set them aside.

## 3 Output Structure

### 3.1 Metadata

When the document covers a specific tool or framework, provide metadata in a table at the beginning:

| Field | Content |
|-------|---------|
| **Tool Name** | e.g., Docker |
| **Official Docs** | Link |
| **Platform** | macOS / Linux / Windows |
| **Version** | e.g., 24.0+ |

If the topic is a general concept (e.g., design patterns, HTTP protocol) rather than a specific tool, this table may be omitted.

### 3.2 Chapter Pattern

Each chapter follows this pattern:

1. **Transition Paragraph**: Explain why this content is being discussed and how it connects to the preceding material. A transition is not a simple one-sentence summary but a logically substantive introductory discourse that helps the reader understand "why we are discussing this now."
2. **Body Content**: Concept explanations, code examples, step-by-step instructions, etc.
3. **Brief Summary**: Core takeaways for the section — no separate heading needed, naturally woven into the closing paragraph

Use a horizontal rule `---` for visual separation between major chapters.

Transition paragraphs should reveal the logical relationship between preceding and following content. Common patterns include:

- **Problem-Driven**: "The approach above solves the X problem, but encounters performance bottlenecks in the Y scenario. To address this challenge, the community proposed..."
- **Natural Progression**: "Having mastered basic route configuration, the next natural question is how to manage middleware for handling cross-cutting concerns."
- **Comparative Introduction**: "Approach A works well in development environments, but production deployment requires additional considerations. Approach B is specifically optimized for production scenarios."

### 3.3 Content Depth

The document should err on the side of being thorough rather than omitting any detail. The goal is for the reader to fully understand and use the technology based solely on this document, without needing to frequently consult other resources. For each concept, provide three levels of exposition: a complete definition, an intuitive understanding, and typical applications.

## 4 Code Standards

### 4.1 Code Blocks

Code must be presented using fenced code blocks with a language identifier immediately following the opening fence. Code blocks should include necessary comments explaining key logic or non-obvious implementation details. Code files (including both code and comments) must be written in English.

### 4.2 Inline Code

When referencing code elements (function names, variable names, file names, commands, etc.) in body text, surround them with single backticks. For example: call the `calculate_mean()` function, modify the `config.yaml` file, run the `pip install` command.

### 4.3 Code Example Requirements

Code examples are one of the core values of development documentation, and their quality directly affects the reader's learning experience. Specific requirements:

- Provide complete, runnable code snippets rather than scattered code fragments, including necessary import statements and initialization code
- Follow the mainstream code style of the language's community (e.g., PEP 8 for Python, ESLint recommended config for JavaScript)
- For longer code, use body text before and after the code block to explain the overall functionality, inputs/outputs, and design decisions
- When multiple files or configurations are involved, clearly label file paths
- When showing configuration files, use comments to explain the meaning and possible values of each key field

## 5 Diagrams and Visualizations

Diagrams and visualizations are critical for understanding technical concepts, and the document should include relevant illustrations wherever possible.

**Architecture and Flow Diagrams**: For content involving system architecture, data flow, or request processing pipelines, search the internet for images from authoritative sources and insert them using the `![description](URL)` format. Prefer images from official documentation, which can typically be obtained from official documentation pages or GitHub repositories. Flow diagrams should use English, and text within the diagrams must be accurately aligned.

**Configuration and UI Screenshots**: For GUI tools or web interfaces, search for and insert relevant screenshots to help readers understand.

**Comparison Tables**: When discussing multiple approaches or tools, use Markdown tables for side-by-side comparison. The column dimensions should be chosen based on the most distinguishing comparison angles for the specific content. Common dimensions include: core philosophy, applicable scenarios, performance characteristics, pros and cons, community ecosystem, etc. Select 4–6 dimensions that best help the reader understand the differences. A lead-in paragraph before the table should explain the purpose of the comparison, and a brief commentary after the table may summarize the overall trend or offer selection recommendations.

**No Placeholders**: Placeholders such as `[image]` or `[screenshot pending]` are strictly prohibited. If a usable image truly cannot be found, describe the diagram's content fully in text, including component relationships, data flow direction, and key nodes.

## 6 PDF Book Processing

When the user provides a long PDF file (such as a technical book) as input material, follow the process below.

### 6.1 PDF Reading Method

Use the Read tool to read the PDF, specifying the `pages` parameter to read specific page ranges (e.g., 20–30 pages at a time). Since the printed page numbers in a book typically do not match the PDF file page numbers, you must first determine the page number offset:

1. Read the PDF's table of contents (usually in the first few pages) and record the printed page numbers for each chapter
2. Compare the printed page number of a chapter from the table of contents with its actual page in the PDF to calculate the offset
3. Explicitly record the correspondence in the document, e.g., "Book page N = PDF page N + offset"

Read 20–30 pages at a time to avoid loading too much content at once. For formula-dense passages, the Read tool will render them as images for visual inspection.

### 6.2 Multi-Chapter Book Processing Strategy

When the user requests a separate note file for each chapter of a book, this is a major undertaking that should be executed systematically following these steps:

**Step One: Create an Overview Document.** Before writing individual chapter notes, you must first create an overview document (e.g., `[Overview] Book Title.md`) containing:

- Basic book information (author, edition, publication year, total pages)
- A mapping table between PDF page numbers and book page numbers
- Chapter titles, page ranges, and a brief overview of core topics for each chapter
- Logical relationships between chapters and a recommended reading order
- A full-book index: organized by topic or keyword, pointing to specific chapters

Example format for the chapter index in the Overview document:

```markdown
| Chapter | Title | Book Pages | PDF Pages | Core Topics |
|---------|-------|------------|-----------|-------------|
| Ch 1 | Getting Started | 1–30 | 23–52 | Installation, basic concepts, initial configuration |
| Ch 2 | Basics | 31–72 | 53–94 | Core operations, common commands |
| ... | ... | ... | ... | ... |
```

**Step Two: Write Notes Chapter by Chapter.** Name each chapter's notes `Chapter XX Title.md` and place them in the corresponding topic directory. When writing, reference the page ranges recorded in the Overview to extract PDF content.

## 7 Formatting Standards

### 7.1 Terminology Standards

When a specialized term first appears, provide a brief clarification or definition if the term may be unfamiliar to the reader. For widely accepted terms (e.g., API, HTTP, Docker), direct usage is fine. Within the same document, a term's clarification only needs to be given at its first occurrence; in longer documents, the clarification may be repeated in key paragraphs for the reader's convenience.

### 7.2 Heading Format

Follow the heading hierarchy conventions specified in CLAUDE.md: the main title appears only once, subheadings use Arabic numeral sequences (1, 1.1, 1.1.1), and headings must not be bolded.

### 7.3 Narrative Coherence

Develop arguments in coherent paragraphs; avoid fragmented bullet-point lists. Bullet-point lists should only be used for exhaustive enumeration of parallel examples, listing ordered steps, or itemizing checklist entries that do not require elaboration. Even when using bullet points, provide lead-in text before and a summary after.

There must be no abrupt jumps to a new topic without any connecting context. Concept explanations should be written as complete expository paragraphs that organically organize multiple related pieces of information together, rather than splitting them into isolated bullet points.

### 7.4 Punctuation

Use standard English punctuation throughout the document. Maintain consistent punctuation in code blocks, formulas, and inline code references.

## 8 Quality Check and Final Review

After the document is complete, the following review process must be executed to ensure output quality. This is not an optional step — every document must undergo this review before delivery.

### 8.1 Review Process

1. **Read the Entire Document**: Use the Read tool to re-read the completed document from beginning to end, checking each paragraph for accuracy and completeness
2. **Check Against the Checklist Item by Item**: Verify each item in the Section 8.2 checklist
3. **ASCII Diagram Alignment Verification**: For all ASCII flowcharts, architecture diagrams, and schematic drawings in the document, check box-drawing character alignment line by line (`│`, `─`, `┌`, `┐`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`):
   - Each column's `│` must be at the same character column position
   - `─` must be continuous without breaks
   - Corner characters in tables and diagram frames must connect correctly
   - Review from a monospace font perspective; verify column positions character by character if necessary
   - CJK characters occupy two monospace character widths while ASCII characters occupy one — pay extra attention to column alignment when mixing them
4. **Immediate Correction**: Fix problems on the spot when found; do not mark them as "to be fixed" and set them aside

### 8.2 Checklist

**Content Completeness:**

- [ ] Background/motivation, concept definitions, core principles, usage instructions, and application scenarios are all covered
- [ ] Important concepts include code examples that are complete and runnable
- [ ] Side-by-side comparison tables are provided when multiple approaches or tools are discussed
- [ ] Places requiring diagrams have image URLs or complete textual descriptions inserted — no placeholders
- [ ] The document ends with a Reference section listing core reference materials

**Formatting Standards:**

- [ ] Specialized terms are clarified when they first appear, if potentially unfamiliar to the reader
- [ ] Punctuation usage is consistent and correct throughout
- [ ] All code blocks include a language identifier
- [ ] Heading hierarchy follows the `## N` / `### N.M` convention, with no bold headings
- [ ] Exposition uses coherent paragraphs as the primary mode; fragmented bullet-point lists are avoided
- [ ] Sufficient transitional connections exist between chapters

**Diagrams and Code:**

- [ ] All ASCII flowcharts and architecture diagrams have correctly aligned box-drawing characters
- [ ] Comments in code blocks are in English and code style follows community conventions
- [ ] Body text before and after code examples explains functionality, inputs/outputs, and design decisions

**Overall Quality:**

- [ ] The document can serve as standalone learning material; the reader does not need to frequently consult other resources
- [ ] The reading experience progresses from simple to complex; both beginners and experts gain value

## 9 Output Example

The following demonstrates a writing example of a development documentation chapter, showing the standard flow of "Metadata → Transition Paragraph → Concept Explanation → Code Example → Key Point Annotation → Comparison Table." Actual output should use this as a reference standard.

````markdown
# WSGI and ASGI

| Field | Content |
|-------|---------|
| **Topic** | Python Web Server Gateway Interfaces |
| **Official Docs** | [PEP 3333 (WSGI)](https://peps.python.org/pep-3333/), [ASGI Spec](https://asgi.readthedocs.io/) |
| **Applicable Frameworks** | Django, Flask, FastAPI, Starlette |

## 1 Background and Motivation

In the early days of Python web development, every web framework needed to write adapter code for specific web servers, resulting in tight coupling between frameworks and servers. If a developer wanted to switch servers or frameworks, extensive migration work was often required. To solve this problem, the community proposed WSGI (Web Server Gateway Interface) in 2003 — a standardized interface sitting between web servers and Python applications, allowing any server conforming to the specification to run any application conforming to the specification.

The core design of WSGI is remarkably simple: a WSGI application is essentially a callable that accepts two parameters — `environ` (a dictionary containing request information) and `start_response` (a callback function for sending HTTP response headers) — and returns an iterable of the response body. Here is the simplest possible WSGI application:

```python
def simple_app(environ, start_response):
    """A minimal WSGI application."""
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]
```

While this interface is elegant in its simplicity, it rests on a fundamental assumption: each request is handled synchronously by a single thread. This assumption posed no problems for traditional web applications, but as real-time communication technologies such as WebSocket, Server-Sent Events (SSE), and Long Polling became widespread, WSGI's synchronous model became a serious bottleneck.

---

## 2 ASGI: The Asynchronous Gateway Interface

To overcome WSGI's synchronous limitations, Django core developer Andrew Godwin proposed the ASGI (Asynchronous Server Gateway Interface) specification in 2016. ASGI is the spiritual successor to WSGI, but was designed from the ground up to natively support asynchronous operations and long-lived connection protocols.

> 📌 **Key Point**: ASGI is not a replacement for WSGI but rather its superset. An ASGI server can simultaneously run WSGI applications (through an adaptation layer) and native ASGI applications, meaning migration can proceed incrementally.

An ASGI application is an asynchronous callable that accepts three parameters: `scope` (metadata about the connection), `receive` (an async function for receiving messages), and `send` (an async function for sending messages). The equivalent minimal example is:

```python
async def simple_asgi_app(scope, receive, send):
    """A minimal ASGI application handling HTTP requests."""
    if scope["type"] == "http":
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/plain"]],
        })
        await send({
            "type": "http.response.body",
            "body": b"Hello, World!",
        })
```

The `scope["type"]` field in ASGI allows the same interface to handle HTTP requests, WebSocket connections, and other custom protocols, fundamentally solving the problem of WSGI's inability to handle long-lived connections.

---

## 3 Comparison and Selection Guide

Now that we have examined the design philosophies and interface shapes of both specifications, the following is a systematic side-by-side comparison of WSGI and ASGI to help developers make informed technology choices in real projects:

| Dimension | WSGI | ASGI |
|-----------|------|------|
| Concurrency Model | Synchronous, one thread per request | Asynchronous, event-loop based |
| Protocol Support | HTTP only | HTTP, WebSocket, custom protocols |
| Long-Lived Connections | Not supported | Natively supported |
| Representative Frameworks | Flask, Django (traditional mode) | FastAPI, Starlette, Django (ASGI mode) |
| Representative Servers | Gunicorn, uWSGI | Uvicorn, Daphne, Hypercorn |
| Learning Curve | Low — simple concepts | Medium — requires understanding async programming |
| Best Suited For | Traditional CRUD apps, internal tools | Real-time apps, high-concurrency I/O-intensive services |

> 💡 **Best Practice**: For traditional web applications that do not involve real-time communication, WSGI remains a stable and reliable choice. However, if the project requires WebSocket, SSE, or high-concurrency I/O handling, ASGI should be preferred. Many teams adopt a gradual migration strategy — running existing WSGI applications on Uvicorn via `WSGIMiddleware` while incrementally developing new features using ASGI.

## Reference

- [PEP 3333 – Python Web Server Gateway Interface v1.0.1](https://peps.python.org/pep-3333/)
- [ASGI Documentation](https://asgi.readthedocs.io/en/latest/)
- [Uvicorn – An ASGI Web Server](https://www.uvicorn.org/)
````

The example above demonstrates the following key elements:

1. **Metadata Table**: Provides basic information about the tool or topic at the beginning of the document, allowing readers to orient themselves quickly.
2. **Transition Paragraphs**: Each section opens by establishing a logical connection to the preceding content, explaining "why we are discussing this now."
3. **Code Examples**: Immediately follow concept explanations with complete, runnable code, with body text before and after explaining its functionality and design.
4. **Key Point Annotations**: Use `> 📌`, `> 💡`, `> ⚠️` blockquotes at critical points, but without overuse.
5. **Comparison Tables**: After all related approaches have been introduced, use a table for side-by-side comparison, with lead-in text before the table and selection guidance after it.
6. **Horizontal Rules**: Use `---` to separate major chapters.
7. **Reference**: List core reference materials at the end of the document.

## 10 Common Errors and Corrections

The following are common quality issues found in output documents that should be specifically avoided during writing and review:

1. **Jargon Pileup Without Explanation**: Using multiple specialized terms in succession without expanding on their meaning. Each important term should be accompanied by an accessible explanation of "what this thing is and what problem it solves" when it first appears, rather than assuming the reader already understands.

2. **Fragmented Lists Instead of Exposition**: Replacing coherent paragraph exposition with large numbers of disconnected bullet-point lists. For example, an introduction to a framework should not be written as ten parallel bullet points, but rather as several complete expository paragraphs that organically weave together features, design philosophy, and use cases.

3. **Code Blocks Missing Language Identifiers**: Failing to specify a language (e.g., `python`, `bash`, `yaml`) after the opening fence of a fenced code block, which prevents syntax highlighting. Every code block must include a language identifier.

4. **Missing Transitions**: No logical connections between sections, leaving the reader unable to understand why there is a sudden jump from one topic to another. Every topic change should include at least one paragraph explaining the logical relationship between the preceding and following content.

5. **Misaligned ASCII Diagram Characters**: Box-drawing characters (`│`, `─`, `┌`, `┘`, etc.) not properly aligned, especially when mixing CJK and ASCII characters, where different character widths cause column position offsets. Alignment must be verified line by line from a monospace font perspective.

6. **Concepts with Definitions but No Intuitive Explanation**: Providing a technical definition without explaining the working principle in accessible language. Every important concept should have an intuitive paragraph explaining "what this thing does and why it is designed this way," accompanied by analogies where appropriate.

7. **Placeholders Instead of Images**: Using `[image]`, `[screenshot pending]`, or similar placeholders instead of actual content. If a usable image URL cannot be found, the diagram's content must be fully described in text, including component relationships and data flow directions.

8. **Incomplete Code Snippets**: Code examples missing necessary import statements, initialization code, or context, preventing readers from running them directly. Example code should be complete, executable units rather than fragments that require the reader to fill in the blanks.

9. **Missing Comparison Tables**: Discussing multiple tools or approaches without providing a side-by-side comparison. When two or more comparable approaches appear, a comparison table should be provided to help readers quickly grasp the similarities and differences and make informed selection decisions.

10. **Abrupt Concept Introductions Without Context**: Introducing a new concept or tool without first explaining the problem it addresses or how it relates to what was previously discussed. Every new topic should be motivated by the preceding context, helping the reader understand why this concept matters at this point in the document.
