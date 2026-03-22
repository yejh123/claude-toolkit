# FormApp API Reference

Comprehensive reference for the Google Apps Script `FormApp` service used to create and manage Google Forms programmatically.

## Creating a Form

```javascript
var form = FormApp.create("Form Title");
```

Returns a `Form` object. The form is created in the user's Google Drive root folder.

## Form-Level Settings

| Method | Description | Example |
|--------|-------------|---------|
| `setTitle(title)` | Set form title | `form.setTitle("Survey")` |
| `setDescription(text)` | Set form description (shown below title) | `form.setDescription("Please fill out...")` |
| `setIsQuiz(enabled)` | Enable quiz mode (enables point values and feedback) | `form.setIsQuiz(true)` |
| `setProgressBar(enabled)` | Show progress bar (multi-page forms) | `form.setProgressBar(true)` |
| `setAllowResponseEdits(enabled)` | Allow respondents to edit after submission | `form.setAllowResponseEdits(false)` |
| `setLimitOneResponsePerUser(enabled)` | Limit to one response per Google account | `form.setLimitOneResponsePerUser(true)` |
| `setCollectEmail(enabled)` | Collect respondent email addresses | `form.setCollectEmail(true)` |
| `setConfirmationMessage(text)` | Custom message after submission | `form.setConfirmationMessage("Thanks!")` |
| `setAcceptingResponses(enabled)` | Open or close the form | `form.setAcceptingResponses(false)` |
| `setCustomClosedFormMessage(text)` | Message shown when form is closed | `form.setCustomClosedFormMessage("Closed")` |
| `setPublishingSummary(enabled)` | Show response summary to respondents | `form.setPublishingSummary(true)` |
| `setShuffleQuestions(enabled)` | Randomize question order | `form.setShuffleQuestions(true)` |
| `setDestination(type, id)` | Link responses to a spreadsheet | `form.setDestination(FormApp.DestinationType.SPREADSHEET, id)` |

### URL Retrieval

| Method | Returns |
|--------|---------|
| `getEditUrl()` | URL for editing the form in the Forms editor |
| `getPublishedUrl()` | URL for respondents to fill out the form |
| `getSummaryUrl()` | URL for the response summary page |
| `getId()` | The form's unique ID |

## Question Types (14 Total)

### 1. Multiple Choice — `addMultipleChoiceItem()`

Radio buttons — respondent selects exactly one option.

```javascript
var item = form.addMultipleChoiceItem();
item.setTitle("What is your role?");
item.setRequired(true);
item.setChoices([
  item.createChoice("Developer"),
  item.createChoice("Designer"),
  item.createChoice("Manager")
]);
item.showOtherOption(true);
item.setHelpText("Select the role that best describes you");
```

**Key methods:**
- `setChoices(choices)` — array of `Choice` objects via `item.createChoice(text)`
- `createChoice(text)` — create a simple choice
- `createChoice(text, navigationType)` — choice with page navigation (`FormApp.PageNavigationType.CONTINUE`, `SUBMIT`, `GO_TO_PAGE`)
- `createChoice(text, pageBreakItem)` — choice that navigates to a specific page
- `showOtherOption(enabled)` — add free-text "Other" option

### 2. Checkbox — `addCheckboxItem()`

Checkboxes — respondent selects one or more options.

```javascript
var item = form.addCheckboxItem();
item.setTitle("Select all that apply");
item.setRequired(true);
item.setChoices([
  item.createChoice("Option A"),
  item.createChoice("Option B"),
  item.createChoice("Option C")
]);
item.showOtherOption(true);
item.setValidation(
  FormApp.createCheckboxValidation()
    .requireSelectAtLeast(1)
    .build()
);
```

**Key methods:**
- Same as MultipleChoiceItem: `setChoices()`, `createChoice()`, `showOtherOption()`
- `setValidation(validation)` — apply a `CheckboxValidation`

### 3. List (Dropdown) — `addListItem()`

Dropdown menu — respondent selects exactly one option from a dropdown.

```javascript
var item = form.addListItem();
item.setTitle("Select your country");
item.setRequired(true);
item.setChoices([
  item.createChoice("United States"),
  item.createChoice("Canada"),
  item.createChoice("United Kingdom")
]);
```

**Key methods:** Same as MultipleChoiceItem (supports navigation via choices).

### 4. Text (Short Answer) — `addTextItem()`

Single-line text input.

```javascript
var item = form.addTextItem();
item.setTitle("Your email address");
item.setRequired(true);
item.setValidation(
  FormApp.createTextValidation()
    .requireTextIsEmail()
    .build()
);
```

**Key methods:**
- `setValidation(validation)` — apply a `TextValidation`

### 5. Paragraph Text — `addParagraphTextItem()`

Multi-line text input for longer responses.

```javascript
var item = form.addParagraphTextItem();
item.setTitle("Describe your experience");
item.setRequired(true);
item.setHelpText("Please provide at least 50 words");
item.setValidation(
  FormApp.createParagraphTextValidation()
    .requireTextLengthGreaterThan(50)
    .build()
);
```

**Key methods:**
- `setValidation(validation)` — apply a `ParagraphTextValidation`

### 6. Scale (Linear Scale) — `addScaleItem()`

Numeric scale with labeled endpoints.

```javascript
var item = form.addScaleItem();
item.setTitle("How satisfied are you?");
item.setRequired(true);
item.setBounds(1, 5);
item.setLabels("Very unsatisfied", "Very satisfied");
```

**Key methods:**
- `setBounds(low, high)` — set numeric range (low: 0 or 1, high: 3 to 10)
- `setLabels(lowLabel, highLabel)` — label the endpoints

### 7. Grid — `addGridItem()`

Matrix of radio buttons — one selection per row.

```javascript
var item = form.addGridItem();
item.setTitle("Rate each feature (1-5)");
item.setRequired(true);
item.setRows(["Speed", "Accuracy", "UI Design"]);
item.setColumns(["1", "2", "3", "4", "5"]);
```

**Key methods:**
- `setRows(rows)` — array of row label strings
- `setColumns(columns)` — array of column label strings
- Keep row labels ≤15 characters and column labels short to avoid truncation

### 8. Checkbox Grid — `addCheckboxGridItem()`

Matrix of checkboxes — multiple selections per row.

```javascript
var item = form.addCheckboxGridItem();
item.setTitle("Select all times you are available");
item.setRequired(true);
item.setRows(["Monday", "Tuesday", "Wednesday"]);
item.setColumns(["Morning", "Afternoon", "Evening"]);
```

**Key methods:** Same as GridItem: `setRows()`, `setColumns()`.

### 9. Date — `addDateItem()`

Date picker.

```javascript
var item = form.addDateItem();
item.setTitle("Event date");
item.setRequired(true);
item.setIncludesYear(true);
```

**Key methods:**
- `setIncludesYear(enabled)` — include year in the date picker

### 10. Time — `addTimeItem()`

Time picker.

```javascript
var item = form.addTimeItem();
item.setTitle("Preferred meeting time");
item.setRequired(true);
```

### 11. Duration — `addDurationItem()`

Duration input (hours, minutes, seconds).

```javascript
var item = form.addDurationItem();
item.setTitle("How long did the task take?");
item.setRequired(true);
```

### 12. Date-Time — `addDateTimeItem()`

Combined date and time picker.

```javascript
var item = form.addDateTimeItem();
item.setTitle("Appointment date and time");
item.setRequired(true);
item.setIncludesYear(true);
```

### 13. Rating — `addRatingItem()`

Star or other icon-based rating.

```javascript
var item = form.addRatingItem();
item.setTitle("Rate your experience");
item.setRequired(true);
item.setRatingScaleLevel(5);
item.setRatingIcon(FormApp.RatingIconType.STAR);
```

**Key methods:**
- `setRatingScaleLevel(level)` — number of rating levels (3 to 10)
- `setRatingIcon(iconType)` — icon type (see RatingIconType enum)

### 14. File Upload — `addFileUploadItem()`

File upload field. Requires respondents to be signed in to Google.

```javascript
var item = form.addFileUploadItem();
item.setTitle("Upload your resume");
item.setRequired(true);
item.setMaxFiles(1);
item.setMaxFileSize(10);  // MB
item.setAcceptedFileTypes([
  FormApp.FileType.DOCUMENT,
  FormApp.FileType.PDF
]);
```

**Key methods:**
- `setMaxFiles(max)` — maximum number of files (1 to 10)
- `setMaxFileSize(mb)` — maximum file size in MB (1, 10, 100, or 1000)
- `setAcceptedFileTypes(types)` — array of `FormApp.FileType` values

## Layout Types (4 Total)

### Page Break — `addPageBreakItem()`

Creates a new page in the form. Essential for multi-section forms.

```javascript
var page = form.addPageBreakItem();
page.setTitle("Section 2: Details");
page.setHelpText("Please provide detailed information below");
```

**Key methods:**
- `setTitle(title)` — section heading
- `setHelpText(text)` — description below the heading
- `setGoToPage(pageBreakItem)` — redirect to another page after this one
- `getPageNavigationType()` / implicit via choices — control flow

**Navigation:** Use with `MultipleChoiceItem` or `ListItem` choices to create conditional branching:

```javascript
var page2 = form.addPageBreakItem().setTitle("Page 2");
var page3 = form.addPageBreakItem().setTitle("Page 3");

var branchQuestion = form.addMultipleChoiceItem();
branchQuestion.setTitle("Which path?");
branchQuestion.setChoices([
  branchQuestion.createChoice("Path A", page2),
  branchQuestion.createChoice("Path B", page3)
]);
```

### Section Header — `addSectionHeaderItem()`

Visual divider within a page. Does NOT create a new page.

```javascript
var header = form.addSectionHeaderItem();
header.setTitle("Additional Details");
header.setHelpText("The following questions are optional");
```

Use `addPageBreakItem()` instead if you want a separate page with navigation.

### Image — `addImageItem()`

Embed an image in the form.

```javascript
var img = form.addImageItem();
img.setTitle("Reference diagram");
img.setImage(UrlFetchApp.fetch("https://example.com/image.png").getBlob());
img.setAlignment(FormApp.Alignment.CENTER);
img.setWidth(400);
```

**Key methods:**
- `setImage(blob)` — set image from a Blob
- `setAlignment(alignment)` — `FormApp.Alignment.LEFT`, `CENTER`, `RIGHT`
- `setWidth(width)` — width in pixels

### Video — `addVideoItem()`

Embed a YouTube video.

```javascript
var video = form.addVideoItem();
video.setTitle("Watch this introduction");
video.setVideoUrl("https://www.youtube.com/watch?v=VIDEO_ID");
video.setAlignment(FormApp.Alignment.CENTER);
video.setWidth(640);
```

**Key methods:**
- `setVideoUrl(url)` — YouTube URL only
- `setAlignment(alignment)` — same as ImageItem
- `setWidth(width)` — width in pixels

## Common Methods (All Item Types)

These methods are available on all question and layout items:

| Method | Description |
|--------|-------------|
| `setTitle(title)` | Set the question text or section heading |
| `setHelpText(text)` | Set helper text (gray text below the question) |
| `setRequired(required)` | Make the question required |
| `getIndex()` | Get the item's position in the form |
| `getId()` | Get the item's unique ID |
| `getType()` | Get the item type as `ItemType` enum |
| `duplicate()` | Create a copy of the item |

## Validation Builders

### Text Validation — `FormApp.createTextValidation()`

For `TextItem` (short answer).

| Method | Description |
|--------|-------------|
| `requireTextIsEmail()` | Must be a valid email |
| `requireTextIsUrl()` | Must be a valid URL |
| `requireNumber()` | Must be a number |
| `requireNumberBetween(low, high)` | Number in range |
| `requireNumberGreaterThan(value)` | Number > value |
| `requireNumberLessThan(value)` | Number < value |
| `requireNumberEqualTo(value)` | Number == value |
| `requireNumberNotBetween(low, high)` | Number outside range |
| `requireTextContains(pattern)` | Text contains string |
| `requireTextDoesNotContain(pattern)` | Text does not contain string |
| `requireTextMatchesPattern(pattern)` | Text matches regex |
| `requireTextDoesNotMatchPattern(pattern)` | Text does not match regex |
| `requireTextLengthGreaterThanOrEqualTo(length)` | Minimum length |
| `requireTextLengthLessThanOrEqualTo(length)` | Maximum length |
| `build()` | Build the validation object |

### Paragraph Text Validation — `FormApp.createParagraphTextValidation()`

For `ParagraphTextItem` (long answer).

| Method | Description |
|--------|-------------|
| `requireTextContains(pattern)` | Text contains string |
| `requireTextDoesNotContain(pattern)` | Text does not contain string |
| `requireTextMatchesPattern(pattern)` | Text matches regex |
| `requireTextDoesNotMatchPattern(pattern)` | Text does not match regex |
| `requireTextLengthGreaterThan(length)` | Text length > value |
| `requireTextLengthGreaterThanOrEqualTo(length)` | Text length >= value |
| `requireTextLengthLessThan(length)` | Text length < value |
| `requireTextLengthLessThanOrEqualTo(length)` | Text length <= value |
| `build()` | Build the validation object |

### Checkbox Validation — `FormApp.createCheckboxValidation()`

For `CheckboxItem`.

| Method | Description |
|--------|-------------|
| `requireSelectAtLeast(count)` | Minimum selections |
| `requireSelectAtMost(count)` | Maximum selections |
| `requireSelectExactly(count)` | Exact number of selections |
| `build()` | Build the validation object |

### Grid Validation — `FormApp.createGridValidation()`

For `GridItem`.

| Method | Description |
|--------|-------------|
| `requireLimitOneResponsePerColumn()` | Each column can only be selected once across rows |
| `build()` | Build the validation object |

### Checkbox Grid Validation — `FormApp.createCheckboxGridValidation()`

For `CheckboxGridItem`.

| Method | Description |
|--------|-------------|
| `requireLimitOneResponsePerColumn()` | Each column can only be selected once per row |
| `build()` | Build the validation object |

## Enumerations

### `FormApp.ItemType`

Used by `getType()` to identify item types.

| Value | Description |
|-------|-------------|
| `CHECKBOX` | Checkbox item |
| `CHECKBOX_GRID` | Checkbox grid item |
| `DATE` | Date item |
| `DATETIME` | Date-time item |
| `DURATION` | Duration item |
| `FILE_UPLOAD` | File upload item |
| `GRID` | Grid item |
| `IMAGE` | Image item |
| `LIST` | List (dropdown) item |
| `MULTIPLE_CHOICE` | Multiple choice item |
| `PAGE_BREAK` | Page break item |
| `PARAGRAPH_TEXT` | Paragraph text item |
| `RATING` | Rating item |
| `SCALE` | Scale item |
| `SECTION_HEADER` | Section header item |
| `TEXT` | Text (short answer) item |
| `TIME` | Time item |
| `VIDEO` | Video item |

### `FormApp.PageNavigationType`

Controls form navigation after a page.

| Value | Description |
|-------|-------------|
| `CONTINUE` | Go to the next page (default) |
| `GO_TO_PAGE` | Go to a specific page |
| `RESTART` | Restart the form from the beginning |
| `SUBMIT` | Submit the form immediately |

### `FormApp.RatingIconType`

Icon types for `RatingItem`.

| Value | Description |
|-------|-------------|
| `STAR` | Star icon (default) |
| `HEART` | Heart icon |
| `THUMB_UP` | Thumbs up icon |

### `FormApp.Alignment`

Alignment for images and videos.

| Value | Description |
|-------|-------------|
| `LEFT` | Left-aligned |
| `CENTER` | Center-aligned |
| `RIGHT` | Right-aligned |

### `FormApp.DestinationType`

Destination for form responses.

| Value | Description |
|-------|-------------|
| `SPREADSHEET` | Google Sheets spreadsheet |

### `FormApp.FileType`

Accepted file types for `FileUploadItem`.

| Value | Description |
|-------|-------------|
| `DOCUMENT` | Google Docs |
| `DRAWING` | Google Drawings |
| `FOLDER` | Google Drive folder |
| `FORM` | Google Forms |
| `PDF` | PDF files |
| `PHOTO` | Image files |
| `PRESENTATION` | Google Slides |
| `SPREADSHEET` | Google Sheets |
| `VIDEO` | Video files |

## Known Limitations

| Limitation | Details |
|------------|---------|
| Grid text truncation | Row and column labels in Grid/CheckboxGrid items are truncated in the UI if too long. Keep row labels ≤15 chars and column labels short. |
| File upload requires sign-in | Forms with `FileUploadItem` require respondents to be signed in to Google. Anonymous file upload is not supported. |
| No conditional visibility | Individual questions cannot be shown/hidden based on answers. Use page branching via `createChoice(text, pageBreakItem)` as a workaround. |
| No answer pre-fill via API | `FormApp` cannot pre-populate answers. Use URL pre-fill parameters instead. |
| Video: YouTube only | `VideoItem` only supports YouTube URLs. |
| No custom themes via API | Form theme/color cannot be set programmatically. Must be changed in the Forms UI. |
| RatingItem is newer API | `addRatingItem()` may not be available in older Apps Script runtimes. |
| Max 200 items per form | Google Forms enforces a limit of 200 items (questions + layout elements) per form. |
| No reordering via API | Items are added in sequence. To reorder, you must `moveItem(fromIndex, toIndex)`. |
| Checkbox "Other" not counted | `showOtherOption(true)` on checkboxes — the "Other" response is not counted toward `requireSelectExactly()` validation. |
