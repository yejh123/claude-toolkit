---
name: google-form
description: "Generate Google Forms via Apps Script (.gs files): design surveys, questionnaires, and feedback forms with correct FormApp API usage. Use when the user wants to create a Google Form, build a survey, design a questionnaire, write a feedback form, or generate an Apps Script for FormApp. Triggers on: Google Form, survey, questionnaire, feedback form, Apps Script, FormApp, create a form."
metadata:
  version: "1.0"
  last_updated: "2026-03-22"
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch
---

# Google Form — Apps Script Form Generator

Generate production-ready `.gs` scripts that create Google Forms programmatically using the FormApp API. Handles form structure, question types, validation, multi-section navigation, and deployment.

## Quick Start

```
Create a Google Form for collecting user feedback on our product
Build a survey with Likert scales and conditional sections
Generate an Apps Script that creates a registration form with email validation
Design a questionnaire with grid questions and checkboxes
```

## Trigger Conditions

**Triggers on**: Google Form, create a survey, build a questionnaire, feedback form, Apps Script form, FormApp, create a form, survey design, form automation

**Does NOT trigger on**:
- Google Sheets scripting without forms -> general Apps Script help
- Form response processing or analysis -> data analysis task
- Google Forms UI editing (no code needed) -> direct user action
- Non-Google survey tools (Typeform, SurveyMonkey) -> not applicable

## Workflow

### Step 1: Clarify Form Requirements

Before writing any code, gather these details from the user:

1. **Purpose**: What is the form for? (feedback, registration, research survey, etc.)
2. **Sections**: How many logical sections? Should they appear as separate pages?
3. **Question types**: Free text, multiple choice, checkboxes, grids, scales, etc.
4. **Validation**: Required fields, character limits, selection constraints
5. **Settings**: Anonymous? Editable responses? Progress bar? One response per user?

If the user provides a rough outline, map each question to the appropriate FormApp item type before coding.

### Step 2: Design Form Structure

Map the user's requirements to FormApp constructs:

| User Need | FormApp Method | Notes |
|-----------|---------------|-------|
| Single-answer choice | `addMultipleChoiceItem()` | Radio buttons |
| Multi-answer choice | `addCheckboxItem()` | Checkboxes |
| Short free text | `addTextItem()` | Single line |
| Long free text | `addParagraphTextItem()` | Multi-line |
| Rating (1-N) | `addScaleItem()` | Linear scale with labels |
| Feature matrix | `addGridItem()` | Rows x columns radio grid |
| Multi-select matrix | `addCheckboxGridItem()` | Rows x columns checkbox grid |
| Date | `addDateItem()` | Date picker |
| Time | `addTimeItem()` | Time picker |
| File upload | `addFileUploadItem()` | Requires sign-in |
| New page | `addPageBreakItem()` | Section separator |

### Step 3: Generate the `.gs` Script

Write the complete Apps Script following the code conventions below. The script must be copy-paste ready — the user should only need to paste it into the Apps Script editor and run it.

### Step 4: Provide Deployment Instructions

Always end with these 5 steps:

1. Open https://script.google.com and create a new project
2. Paste the entire script into the editor
3. Run the main function (e.g., `createMyForm()`)
4. Grant Google Forms permissions when prompted
5. Check the execution log (View > Logs) for the edit and published URLs

## Code Conventions

All generated `.gs` scripts must follow these rules:

### Language and Syntax

- Use `var` for all declarations (not `const` or `let`) for broadest Apps Script compatibility
- Use `function` declarations (not arrow functions)
- Use string concatenation with `+` for multi-line strings (no template literals)
- Use `Array.map(function(...) { ... })` (not arrow syntax)

### File Structure

```
1. File-level JSDoc comment (purpose + usage instructions)
2. Top-level var arrays for shared option lists
3. Main entry function (creates form, calls section helpers)
4. One helper function per section (addXxxSection)
```

- One main entry function that creates the form and calls section helpers
- One helper function per logical section (e.g., `addBackgroundSection`, `addFeedbackSection`)
- Shared option arrays as top-level `var` declarations (avoids duplication and makes editing easy)

### Form Setup

Always configure these in the main function:

```javascript
form.setIsQuiz(false);           // unless explicitly a quiz
form.setProgressBar(true);       // for multi-section forms
form.setAllowResponseEdits(false);
form.setLimitOneResponsePerUser(false);
```

### URL Logging

Always log both URLs at the end of the main function:

```javascript
Logger.log("Form created successfully!");
Logger.log("Edit URL: " + form.getEditUrl());
Logger.log("Published URL: " + form.getPublishedUrl());
```

### Naming

- Main function: `createXxxForm()` (e.g., `createFeedbackForm`)
- Section helpers: `addXxxSection(form)` (e.g., `addBackgroundSection`)
- Option arrays: `ALL_CAPS` descriptive names (e.g., `GRID_FEATURES`, `INTEREST_SCALE`)

## UX Pitfalls

These are hard-won lessons — follow them to avoid broken or unusable forms.

### Grid Items: Keep Labels Short

Google Forms **truncates** long text in grid rows and columns. This is the most common pitfall.

- **Row labels**: Keep to 15 characters or fewer
- **Column labels**: Use just numbers (`"1"`, `"2"`, `"3"`, `"4"`, `"5"`) for scales
- **Scale definitions**: Put the full scale description in the question title, not in column labels

```javascript
// WRONG: Long column labels get truncated
q.setColumns(["Not interested", "Slightly interested", "Moderately interested", "Very interested", "Must have"]);

// RIGHT: Short column labels + scale defined in title
q.setTitle(
  "How interested are you in each feature?\n" +
  "(1 = Not interested, 2 = Slightly, 3 = Moderate, 4 = Very, 5 = Must have)"
);
q.setColumns(["1", "2", "3", "4", "5"]);
```

For row labels, use abbreviated versions and put full descriptions elsewhere:

```javascript
// WRONG: "Real-time session monitoring dashboard" (too long, gets truncated)
// RIGHT: "Real-time monitoring" (short, fits)
var GRID_FEATURES = ["Step timeline", "Cost estimation", "Analytics", "Flow diagrams"];
```

### Checkboxes and Multiple Choice: Enable "Other"

Always add `showOtherOption(true)` on checkboxes and multiple-choice questions where the user might have answers you haven't listed:

```javascript
q.showOtherOption(true);
```

### Multi-Page Forms: Use PageBreakItem

Use `addPageBreakItem()` (not `addSectionHeaderItem()`) to create separate pages with navigation:

```javascript
var section = form.addPageBreakItem();
section.setTitle("Section Title");
section.setHelpText("Brief description of this section");
```

`addSectionHeaderItem()` only adds a visual divider within the same page — it does not create a new page.

### Progress Bar

Enable the progress bar for any form with 2+ sections:

```javascript
form.setProgressBar(true);
```

### Validation

Use validation builders for constraints. Common patterns:

```javascript
// Require exactly N checkbox selections
var validation = FormApp.createCheckboxValidation()
  .requireSelectExactly(3)
  .build();
checkboxItem.setValidation(validation);

// Text must be an email
var emailValidation = FormApp.createTextValidation()
  .requireTextIsEmail()
  .build();
textItem.setValidation(emailValidation);
```

### Help Text

Use `setHelpText()` for examples and clarifications — it renders as smaller gray text below the question:

```javascript
q.setHelpText('e.g. "Why did the agent make 12 edits to the same file?"');
```

## Question Type Quick Reference

| Use Case | Method | Key Methods |
|----------|--------|-------------|
| Radio buttons | `addMultipleChoiceItem()` | `setChoices()`, `showOtherOption()` |
| Checkboxes | `addCheckboxItem()` | `setChoices()`, `showOtherOption()`, `setValidation()` |
| Short text | `addTextItem()` | `setValidation()` |
| Long text | `addParagraphTextItem()` | `setValidation()` |
| Linear scale | `addScaleItem()` | `setBounds(low, high)`, `setLabels(lowLabel, highLabel)` |
| Radio grid | `addGridItem()` | `setRows()`, `setColumns()` |
| Checkbox grid | `addCheckboxGridItem()` | `setRows()`, `setColumns()` |
| Dropdown | `addListItem()` | `setChoices()` |
| Date | `addDateItem()` | `setIncludesYear()` |
| Time | `addTimeItem()` | — |
| Duration | `addDurationItem()` | — |
| Star rating | `addRatingItem()` | `setRatingScaleLevel()`, `setRatingIcon()` |
| File upload | `addFileUploadItem()` | `setMaxFiles()`, `setMaxFileSize()` |
| Page break | `addPageBreakItem()` | `setTitle()`, `setHelpText()`, `setGoToPage()` |

For the full FormApp API reference, load `references/formapp-api.md`.

## Output Format

Every response must include:

1. **Complete `.gs` file** — copy-paste ready, following all conventions above
2. **Deployment instructions** — the 5-step process from Step 4

Do not generate partial scripts or pseudocode. The output must run successfully in the Apps Script editor without modification.

## Quality Standards

| Dimension | Requirement |
|-----------|-------------|
| Completeness | All user-specified questions included with correct types |
| Syntax | Uses `var`, `function`, string concatenation — no ES6+ |
| Structure | One main function + one helper per section |
| Grid labels | Row labels ≤15 chars, column labels short |
| URLs | Both `getEditUrl()` and `getPublishedUrl()` logged |
| Validation | Required fields marked, checkbox limits enforced |
| Sections | Multi-section forms use `addPageBreakItem()` with progress bar |
| "Other" option | Enabled on checkboxes/multiple-choice where appropriate |
