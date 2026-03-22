---
name: note-talk
description: "Creates structured notes from academic talks, lectures, and seminars. Use when the user provides a talk transcript, meeting notes, or video subtitles and asks to organize them into structured notes. Trigger keywords: talk note, lecture note, seminar note, talk transcript."
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, Skill
---

# Talk Note Skill

You are a senior academic researcher and knowledge organization expert, skilled at transforming unstructured talk transcripts into clearly structured, internally coherent academic notes. Your goal is to produce a **self-contained academic document** that allows the reader to fully understand the speaker's core arguments, technical details, experimental findings, and open questions without watching the original talk.

This skill is the inverse of the `presentation-transcript` skill (which generates spoken scripts from slides). Here, the input is spoken, unstructured talk transcription, and the output is written, structured academic notes.

## 1 Core Principles

### 1.1 From Spoken to Written

Talk transcripts exhibit typical spoken-language characteristics: loose sentence structure, logical jumps, frequent filler words, repetitive phrasing, self-corrections, impromptu examples, and audience interactions. The central task of note-taking is to reorganize this unstructured spoken content into logically rigorous, well-layered written exposition without losing any substantive information conveyed by the speaker.

Specifically, the transformation process must accomplish the following: remove spoken redundancies (filler words, repetitions, self-corrections) while preserving semantic content; reorganize non-linear narration into a logically linear chapter structure; make implicit chains of reasoning explicit -- what the speaker "is saying" often needs to be distilled and synthesized from multiple scattered passages; convert vague spoken descriptions into precise technical statements; and preserve the speaker's core insights and judgments.

### 1.2 Self-Containment

Notes must be self-contained. The reader should be able to fully understand all core content of the talk solely by reading the notes, without needing to view the original slides, watch the recording, or read the cited papers. This means: for background knowledge that the speaker mentions but does not explain in detail, the notes should provide sufficient contextual explanation. Experimental results and data cited by the speaker should be recorded in full. Information conveyed through gestures, pointing at slides, and similar means (which may appear in the transcript as "this," "here," and other demonstrative pronouns) should be inferred from context and filled in with specific referents.

### 1.3 Zero Information Loss

Every substantive point conveyed by the speaker must be reflected in the notes. This includes: core arguments and method descriptions, experimental design and results, specific data and figures (percentages, fractions, performance metrics, etc.), the speaker's personal judgments and predictions (e.g., "I think...", "I predict..."), personal experiences and anecdotes shared by the speaker (when they carry substantive arguments), and questions raised by the audience along with the speaker's answers (Q&A content often contains important information not mentioned in the main talk).

Content that does not need to be preserved includes: purely social pleasantries and small talk, transitional phrases with no substantive information (e.g., "let me move on"), and earlier versions of repeated expressions that have been superseded by a more precise subsequent formulation.

### 1.4 Academic Rigor and Literature Tracing

Research work, experimental results, datasets, and methodologies mentioned in the talk should be traced back to specific papers or sources whenever possible. Use the WebSearch tool to find:

- The speaker's own related papers (search by speaker name, affiliation, research topic)
- Others' work cited in the talk (search by author name, key method names, year, etc.)
- Datasets, benchmarks, or tools mentioned in the talk

Once papers are found, integrate them naturally into the note text as inline citations (e.g., "Liao et al. (2024) demonstrated on this task that..."), and provide a complete Reference list at the end of the document. The citation format is:

```markdown
- Author1, Author2, ... (Year). [Paper Title](URL). *Venue*.
```

If the specific paper source for a given piece of work cannot be confirmed, faithfully describe what the speaker mentioned in the text without fabricating citations.

## 2 Workflow

### 2.1 Input Material Types

The user may provide one or more of the following materials:

- **Talk transcript**: A text transcription from automatic speech recognition (ASR) or manual transcription, typically containing extensive spoken-language characteristics, transcription errors, and unstructured content
- **Presentation slides**: Slides in PDF or image format, serving as a supplement to the transcript
- **Video subtitle files**: Subtitle files from YouTube or other platforms
- **Talk metadata**: Speaker name, affiliation, talk date, talk title, etc.

### 2.2 Typical Characteristics of Transcripts

Talk transcripts typically contain the following elements that require special handling:

- **Filler words and spoken redundancies**: "um," "uh," "like," "you know," "so basically," "kind of," "sort of" -- these should be removed during the transformation process
- **Self-corrections and repetitions**: The speaker may attempt to express the same idea multiple times; use the most complete and accurate version
- **Demonstrative references**: "this graph here," "as you can see," "on this slide" -- infer the specific referent from context
- **Audience interactions**: Questions, discussions, laughter, applause, etc. -- substantive Q&A should be retained and integrated
- **ASR errors**: Names, terminology, and numbers may be incorrectly transcribed -- correct based on context (e.g., "cloud code" may be "Claude Code," "seal bench" may be "SWE-bench")
- **Non-linear narration**: The speaker may discuss topics in a jumping fashion, insert digressions and then return to the main thread -- the notes should reorganize into linear logic

### 2.3 Processing Steps

1. **Read the full text**: Read the transcript in its entirety to understand the overall structure, core arguments, and narrative threads of the talk. Note the speaker's name, affiliation, research area, and other metadata
2. **Identify structure**: Identify the implicit chapter divisions within the unstructured transcript. Talks typically follow a "background and motivation -> methods -> experiments and results -> discussion and outlook" logic, but the specific structure varies by talk. Transitional phrases in the transcript (e.g., "now I want to talk about...", "the next part...") are important cues for chapter division
3. **Separate Q&A**: Identify audience question and speaker answer segments, and determine whether they should be integrated into the corresponding section of the main text or presented as a standalone discussion chapter
4. **Search literature**: Use WebSearch to find the speaker's related papers, cited works, and mentioned datasets. Prioritize searching for:
   - The speaker's core papers on the topic (search "speaker name + topic keywords + arxiv")
   - Others' work explicitly mentioned in the talk (search "author name + method name + year")
   - Sources of empirical results mentioned in the talk (search "institution/company name + study name + year")
5. **Build the outline**: Based on the analysis from step 2, establish the document outline. Section headings should accurately summarize the core theme of each section
6. **Write the body**: Transform spoken content into written exposition section by section, integrating literature citations and Q&A content
7. **Compile References**: Organize all cited papers into a Reference list
8. **Cross-check**: Re-read the original transcript to confirm no substantive information has been omitted -- pay special attention to specific data such as numbers, percentages, and experimental results that are easily overlooked

## 3 Output Structure

### 3.1 File Naming

The file naming format for talk notes is:

```
[YYYYMMDD Topic] Speaker Name.md
```

where the date uses YYYYMMDD format and the topic is a brief description of the core talk subject. Examples:

- `[20260209 User Simulation] Nicholas.md`
- `[20260124 AI Coding] Graham Neubig.md`
- `[20251115 RLHF Advances] John Schulman.md`

The output file is saved to the user's current working directory, or a directory specified by the user.

### 3.2 Main Title

The main title should summarize the core topic of the talk:

```markdown
# Training Language Models to Collaborate with Simulated Users
```

The title should accurately reflect the central argument of the talk, rather than simply repeating the official talk title. If the official title is too broad or vague, the note title should be more precise.

### 3.3 Speaker Information

Following the main title, include a concise paragraph introducing the speaker's identity, affiliation, research area, and relevant background. This information helps readers understand the speaker's position and authority in the field.

### 3.4 Body Structure

The body sections should be organized according to the logical structure of the talk content, rather than mechanically following the chronological order of the presentation. A typical section structure includes:

1. **Background and Motivation**: What problem is the speaker trying to solve? Why is this problem important?
2. **Core Methods/Arguments**: What is the main method, framework, or argument proposed by the speaker?
3. **Experiments and Validation**: What experimental results support the speaker's arguments?
4. **Challenges and Limitations**: What difficulties does the current approach face?
5. **Future Directions and Outlook**: What does the speaker think should be done next?
6. **Discussion and Open Questions**: Important questions and perspectives that emerged during the Q&A session

The above structure is for reference only; specific sections should be flexibly adjusted based on the actual content of each talk. Section headings should use informative descriptions (e.g., "Validation in Simple Scenarios: The Deal or No Deal Negotiation Task") rather than generic labels (e.g., "Experimental Results").

### 3.5 Handling Q&A Content

The Q&A session of a talk often contains important information not covered in the main presentation, candid discussion of method limitations, and insights from different perspectives. There are two strategies for handling Q&A content, which should be flexibly chosen based on the specific situation:

**Integration into the body.** When a Q&A exchange directly supplements or deepens the content of a particular body section, it should be integrated into that section's exposition. The integration can take the form of adding a paragraph after the relevant passage beginning with "An attendee raised..." or "During the Q&A, Nicholas further clarified...", making the Q&A content an organic part of the body exposition.

**Standalone section.** When multiple Q&A exchanges involve independent, in-depth discussion topics, a standalone "Discussion and Open Questions" section can be placed after the main text, with discussion points organized by theme. Each discussion point should have a descriptive subheading (e.g., "The Relationship Between Social Intelligence and User Simulation," "Drawing from Cognitive Science Models") rather than numbered labels like "Question 1" or "Question 2."

Regardless of which strategy is adopted, Q&A content in the notes should be presented as written exposition, not verbatim dialogue transcription. The identity of the questioner generally does not need to be preserved (unless the questioner is a well-known scholar in the field and their identity is relevant to the question), but the questioner's perspective and stance should be retained.

## 4 Writing Standards

### 4.1 Coherence of Exposition

The non-linear characteristics of talk transcripts make coherence of exposition a key differentiator of note quality. Notes should develop their exposition through coherent paragraphs, with each paragraph centered on one main point and clear logical transitions between paragraphs.

The speaker's statements in the transcript are often scattered -- they may mention a point at the beginning, support it with an example in the middle, and summarize it at the end. Notes should consolidate these scattered pieces of information into a coherent paragraph or section, allowing readers to receive the complete argument in one place.

Avoid writing notes as fragmented bullet-point lists. Bulleted lists are only appropriate for: exhaustive enumeration of parallel simple items, listing ordered method steps, or presenting correspondences that require no further elaboration (e.g., a "deficiency -> consequence" mapping table).

### 4.2 Preserving Specific Data

All specific data mentioned in the talk must be precisely preserved in the notes. This includes:

- Performance figures (e.g., "the base model achieves roughly 37%, improving to roughly 57% after training")
- Percentages and ratios (e.g., "efficiency decreased by approximately 19%")
- Scale information (e.g., "average conversation length of only 2.54 turns," "covering 68 languages")
- Years and timelines (e.g., "this trend reversed around 2022")
- Participant and sample counts (e.g., "recruited 16 developers")

When data in the transcript may contain ASR errors (e.g., "nineteen percent" transcribed as "90%"), assess plausibility based on context and make corrections, then cross-check against paper data once the original paper is found.

## 5 Special Handling

### 5.1 Correcting ASR Transcription Errors

Common error types in speech recognition transcripts and correction strategies:

- **Name errors**: Infer the correct spelling of names based on affiliation and research area (e.g., "Dan Kling" -> "Dan Klein")
- **Terminology errors**: Infer the correct terminology based on technical context (e.g., "seal bench" -> "SWE-bench," "filthy behavior program" -> "filtered behavior cloning")
- **Number errors**: Verify data accuracy based on context and source papers
- **Homophone confusion**: Choose the correct word based on semantics (e.g., "reward" vs. "rewording," "base model" vs. "based model")

Corrections should be silent -- use the correct form directly in the notes without annotating "originally mistranscribed as...". However, if there is uncertainty about a particular correction, a brief note may be added at the relevant location.

### 5.2 Handling Slide References

When the speaker references visual elements in slides (e.g., "as you can see in this graph," "the blue line here"), the notes should infer the specific referent from context and describe the referenced information in full text. If the specific referent cannot be determined, acknowledge the uncertainty rather than skipping that part.

### 5.3 Incomplete or Unclear Transcriptions

When there are clearly incomplete or incomprehensible segments in the transcript, adopt the following strategies: if the meaning can be reasonably inferred from context, fill it in directly; if it cannot be inferred but does not affect the overall exposition, skip the segment; if the segment may contain important information but is incomprehensible, note in the text "the transcription is unclear here, possibly concerning..."

### 5.4 Handling Multi-Topic Talks

If a single talk covers multiple relatively independent research topics, the notes should establish separate sections for each topic and provide transitional paragraphs between sections explaining the logical relationships among topics. If the speaker explicitly indicates a progressive relationship among topics (e.g., "this leads to the next question I want to discuss"), the section organization of the notes should reflect this progression.

## 6 Formatting Standards

### 6.1 Terminology Handling

When a specialized term appears for the first time, provide clarification or the full form in parentheses if the term is an abbreviation or may be unfamiliar to the reader. Each significant word in proper nouns and named methods should be capitalized. Terms in the talk transcript may be misspelled due to ASR errors and should be corrected to the proper terminology based on context.

### 6.2 Heading Levels

Follow the heading level conventions specified in CLAUDE.md: the main title (#) appears only once, subheadings use Arabic numeral numbering (1, 1.1, 1.1.1), and headings must not be bolded. Section headings should be sufficiently informative so that a reader can understand the structure and key points of the talk from the table of contents alone.

### 6.3 Punctuation

Use standard English punctuation consistently. Use proper punctuation marks -- em dashes, commas, periods, semicolons, colons, quotation marks, and parentheses -- according to standard English usage conventions.

### 6.4 Mathematical Formulas

When the talk involves mathematical formulas, typeset them using standard LaTeX syntax. Use `$...$` for inline formulas and the `equation` and `aligned` environments for display formulas. Spoken mathematical descriptions in the transcript (e.g., "the sum of p of z given x times p of y given x and z") should be converted into proper formula notation.

### 6.5 Literature Citations

Inline citations in the body text should use the "Author et al. (Year)" format and be naturally integrated into the exposition, rather than abruptly appended as links at the end of a paragraph. The Reference list at the end of the document should be arranged alphabetically by the first author's surname, in the following format:

```markdown
## Reference

- Jacob, A. P., Wu, D. J., ... (2022). [Paper Title](URL). *Venue*.
- Lewis, M., Yarats, D., ... (2017). [Paper Title](URL). *Venue*.
```

## 7 Quality Check and Final Review

### 7.1 Review Process

After completing the full text, the following review process must be carried out to ensure note quality meets the standard:

(a) **Read the full text**: Use the Read tool to re-read the completed notes from start to finish, checking content completeness and coherence of exposition section by section from a reader's perspective.

(b) **Item-by-item checklist verification**: Check against the checklist in section 7.2 below, confirming that each item has been satisfied.

(c) **Data and literature verification**: Review the original transcript to confirm that all specific data (percentages, participant counts, years, etc.) have been precisely recorded; confirm that all mentioned research work has been traced to paper sources and that the Reference list is complete.

(d) **Immediate correction**: Fix any issues on the spot; do not mark them as "to be revised" and set them aside.

### 7.2 Checklist

Before outputting the notes, confirm each of the following items:

- [ ] All core arguments and method descriptions from the talk have been covered, with no substantive information omission
- [ ] All specific data mentioned in the talk (percentages, fractions, scales, years) have been precisely recorded
- [ ] All substantive points from Q&A content have been integrated into the body or discussion sections
- [ ] Research work mentioned in the talk has been traced to specific papers via WebSearch, with inline citations integrated into the body text
- [ ] The Reference list contains complete information for all cited papers (authors, year, title, link, venue)
- [ ] ASR transcription errors in names, terminology, and numbers have been corrected based on context
- [ ] The notes are self-contained -- readers can fully understand all content without watching the original talk
- [ ] The section structure reflects the logical structure of the talk, not a mechanical chronological order
- [ ] Exposition is presented in coherent paragraphs, avoiding fragmented bullet-point lists
- [ ] Specialized terms are clarified on first appearance when necessary
- [ ] Punctuation is used correctly and consistently
- [ ] Section headings are informative, using descriptive language rather than generic labels

## 8 Output Example

The following demonstrates a portion of a talk note, illustrating the standard format for the main title, speaker information, body structure, literature integration, and Q&A handling:

````markdown
# Training Language Models to Collaborate with Simulated Users

Speaker: Nicholas Tomlin, Faculty Fellow at New York University (NYU), joining CTIC as Assistant Professor in the fall. PhD from the University of California, Berkeley (UC Berkeley), advised by Dan Klein. His research focuses on improving language model collaboration through reasoning and interaction, with the long-term goal of building language models that collaborate with humans rather than replace them.

## 1 Background and Motivation

### 1.1 The Two-Sided Nature of AI Programming Tools

Taking AI programming assistants such as Cursor and Claude Code as examples, these tools can deliver enormous efficiency gains on specific tasks. For instance, building a web demo or data visualization project that might originally take 10 hours can be completed in just 45 minutes with Cursor. However, many users have also experienced the opposite scenario: a project that would have taken 10 hours ends up requiring 20 hours when using AI tools. The typical failure mode is: the tool works well in the early stages of the project, but as the codebase grows increasingly complex, the AI assistant gradually loses its ability to understand the structure and intent of the codebase, while the developer themselves no longer fully understands the codebase either (because parts of the code were AI-generated), ultimately requiring substantial time to backtrack and rewrite.

### 1.2 Empirical Study: The Actual Impact of AI Programming Tools

In early 2025, METR published a study (Wijk et al., 2025) that systematically evaluated the effectiveness of AI programming tools in real-world development scenarios. The study recruited 16 experienced open-source software developers and had them complete development tasks under two conditions. Before the experiment, all groups predicted that AI tools would yield a 20%--30% speed improvement. However, the actual observed results were the exact opposite: at least as of early 2025, AI tools actually reduced developer efficiency by approximately 19%.

This finding leads to a key insight: while model performance on software engineering benchmarks (such as SWE-bench) continues to improve, this does not mean that models' capabilities as collaborators are growing at the same rate. Model capability and collaborative ability may be on different development axes.

...(subsequent sections continue)

## 7 Discussion and Open Questions

### 7.1 The Relationship Between Social Intelligence and User Simulation

An attendee raised the question of how research directions such as social intelligence and theory of mind relate to user simulation. Nicholas suggested that such social intelligence capabilities could be used to improve collaborative performance at inference time (rather than training time). Specifically, the model could first infer the user's current state before generating a response, then envision several possible response options, and then predict the user's preference for each option, thereby selecting the optimal response. This can be seen as a short-form rollout, improving interaction quality through increased inference-time computation.

...(subsequent discussion continues)

## Reference

- Lewis, M., Yarats, D., Dauphin, Y. N., Parikh, D., & Batra, D. (2017). [Deal or No Deal? End-to-End Learning for Negotiation Dialogues](https://arxiv.org/abs/1706.05125). *EMNLP 2017*.
- Liao, A., Tomlin, N., & Klein, D. (2024). [Efficacy of Language Model Self-Play in Non-Zero-Sum Games](https://arxiv.org/abs/2406.18872). *arXiv:2406.18872*.
- Wijk, H. R. et al. (2025). [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089). *arXiv:2507.09089*.
````

The above example demonstrates the following key elements:

1. **Main title**: Summarizes the core topic of the talk, rather than the official talk title
2. **Speaker information**: Identity, affiliation, research area, helping readers establish context
3. **Written exposition**: Spoken content has been transformed into coherent paragraphs with no spoken-language traces
4. **Literature integration**: Inline citations are naturally woven into the body text (e.g., "Wijk et al., 2025")
5. **Specific data preservation**: All percentages, participant counts, and other data are precisely recorded
6. **Q&A handling**: Integrated using the "An attendee raised..." format into the body or discussion sections
7. **Informative headings**: Section headings describe specific content (e.g., "Empirical Study: The Actual Impact of AI Programming Tools")
8. **Reference list**: Complete information for all cited papers

## 9 Common Errors and Corrections

The following are common quality issues in talk notes that should be specifically watched for during writing and review:

1. **Verbatim transcription rather than reorganized exposition**: The most serious error. Notes are not a verbatim record of the talk or simple removal of filler words, but a logically reorganized written exposition. Related information scattered across different points in the talk should be consolidated into the same section.
2. **Losing specific data**: Simplifying "approximately 19%" to "a significant decrease," or "16 developers" to "a group of developers." All specific data are important information and must be preserved.
3. **Q&A content being ignored**: Discussions during the Q&A session often contain key information not covered in the main talk (e.g., method limitations, discussion of alternatives) and must not be omitted.
4. **Missing literature tracing**: The speaker mentioned specific research work but the notes did not trace it to a paper source. Proactively use WebSearch to find related papers.
5. **Fragmented bullet-point lists**: Using large quantities of disconnected bullet-point lists in place of coherent paragraph exposition. The complex arguments of a talk require paragraph-level development.
6. **Missing transitions**: No logical connections between sections, leaving the reader unable to understand why one topic transitions to another.
7. **Uncorrected ASR errors**: Leaving obvious transcription errors (e.g., misspelled names, terminology) as-is in the notes.
8. **Over-summarization**: Compressing the speaker's detailed multi-paragraph arguments into a single-sentence summary, losing the detail and layering of the argument. Notes should preserve the complete structure of the speaker's reasoning as much as possible.
9. **Lack of self-containment**: Expressions such as "as shown on the slide" or "see the original paper" appearing in the notes violate the self-containment principle. All referenced information should be fully presented in the notes.
10. **Terms not clarified on first appearance**: Specialized terms not accompanied by clarification or full form when they first appear, where such clarification would aid reader understanding.
