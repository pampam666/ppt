---
description: The Slide Preparation Flow automates deck creation by extracting PDF data, analyzing PRD context, generating three structure options, gathering relevant visuals via Tavily or attachments, and invoking the Power Design skill for final HTML output.
---

# Workflow — Slide Preparation Flow
# Location: <workspace>/.agents/workflows/slide-preparation-flow.md
# Trigger: /slide-preparation-flow
# Scope: End-to-end orchestration from raw attachments to final slide deck

---

## Overview

This workflow coordinates four specialized skills (filesystem, pdf, tavily-search, power-design)
across six sequential phases to transform raw documents and a PRD into a branded HTML presentation.

**Prerequisite check:** Before starting Phase 1, verify all skills from Rule 4 of
`.agents/rules/slide-preparation.md` are installed. If any are missing, halt and report.

**Workspace token:** Throughout this document, `<title>` refers to the `<presentation-title>`
provided by the user at invocation time.

---

## Phase 1 — Data Ingestion

**Goal:** Extract all raw PDF content from the attachment folder and persist it as
structured Markdown for downstream analysis.

### Step 1.1 — Scan the attachment folder

Use the **File System skill** to list all files in:
```
<workspace>/slide/<title>/src/attachment/
```

- If the folder is empty or does not exist → notify the user and ask if they want to continue
  on PRD context alone. If yes, skip to Phase 2. If no, halt.
- Log each file found: name, type, size.

### Step 1.2 — Extract PDF content

For each `.pdf` file found in `src/attachment/`:

Use the **PDF skill (Composio)** to extract the full text and all tables:

```python
import pdfplumber

with pdfplumber.open("<file_path>") as pdf:
    extracted_text = ""
    for i, page in enumerate(pdf.pages):
        extracted_text += f"\n\n## Page {i + 1}\n\n"
        page_text = page.extract_text()
        if page_text:
            extracted_text += page_text
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            extracted_text += f"\n\n### Table {j + 1} (Page {i + 1})\n\n"
            for row in table:
                extracted_text += "| " + " | ".join(str(cell or "") for cell in row) + " |\n"
```

### Step 1.3 — Write Markdown output

Use the **File System skill** to write the extracted content as a Markdown file:

- Path: `<workspace>/slide/<title>/docs/product/<filename-without-extension>.md`
- Format: Clean Markdown with H2 page headers and pipe tables for extracted tables
- Append a metadata header to each file:

```markdown
---
source_file: <original_filename>.pdf
extracted_at: <ISO 8601 timestamp>
pages_extracted: <N>
---
```

Repeat Steps 1.2–1.3 for every PDF in the attachment folder.

---

## Phase 2 — Context Analysis

**Goal:** Extract the presentation's strategic context from the PRD to inform all
subsequent decisions.

### Step 2.1 — Read the PRD

Use the **File System skill** to read all files in:
```
<workspace>/slide/<title>/docs/prd/
```

- If the folder is empty or no file exists → halt. Report:
  > "No PRD found at `slide/<title>/docs/prd/`. Please add a PRD document before continuing."

### Step 2.2 — Extract structured context

Parse and extract the following from the PRD:

| Field | Description |
|-------|-------------|
| **Presentation Goal** | The primary objective the slides must achieve |
| **Target Audience** | Who will view the slides (role, sector, expertise level) |
| **Key Messages** | The 3–7 core points the audience must remember |
| **Tone & Voice** | Formal / conversational / technical / inspirational |
| **Success Criteria** | How the presenter defines a successful outcome |

Store this context in memory for use in Phases 3, 5, and 6.

### Step 2.3 — Cross-reference with product details

If `docs/product/` files exist (from Phase 1), identify which product details
are directly relevant to the PRD goals. Flag irrelevant content to be excluded.

---

## Phase 3 — Structure Generation

**Goal:** Generate 3 distinct presentation structure options that each align with
the PRD context and product details extracted in Phases 1–2.

### Step 3.1 — Generate 3 structure options

Each option must differ meaningfully in at least one of:
- Narrative arc (problem-solution vs. story-driven vs. data-first)
- Number of slides (compact: 8–12 / standard: 13–18 / detailed: 19–25)
- Emphasis (audience pain points / product capabilities / ROI & proof)

For each option, generate a slide-by-slide outline:

```
Option <N>: <Option Title>
Narrative arc: <Brief description>
Slide count: <N>

Slide 1: [Title Slide] — <Title text>
Slide 2: [Section] — <Section name>
Slide 3: [Content] — <Key point>
...
Slide N: [CTA / Close] — <Closing message>
```

Each slide entry must specify: slide type (Title / Section / Content / Data / Quote / CTA),
the single idea it communicates, and the PRD section it traces back to.

### Step 3.2 — Save structure drafts

Use the **File System skill** to write each option to its own file:

```
<workspace>/slide/<title>/src/structure/option-1.md
<workspace>/slide/<title>/src/structure/option-2.md
<workspace>/slide/<title>/src/structure/option-3.md
```

Each file must include:
- Full slide outline (from Step 3.1)
- PRD alignment notes per slide
- Suggested brand mood (e.g., "authoritative and data-forward" or "warm and conversational")

---

## Phase 4 — Pause & Validate (Authorization Gate)

**MANDATORY STOP — Do not proceed until user confirms.**

Present a summary of the 3 options to the user:

```
Three presentation structure options are ready:

Option 1 — <Title>
<3-sentence summary of narrative arc, slide count, and emphasis>
PRD alignment: <quoted PRD goal it best serves>

Option 2 — <Title>
<3-sentence summary>
PRD alignment: <quoted PRD goal it best serves>

Option 3 — <Title>
<3-sentence summary>
PRD alignment: <quoted PRD goal it best serves>

Full outlines saved to: slide/<title>/src/structure/

Please select option 1, 2, or 3 to continue.
```

**HALT.** Wait for the user's explicit numeric selection.

- If the user requests modifications to a draft → apply changes, save to `src/structure/`,
  re-present the updated option, and re-ask for selection.
- Do NOT proceed to Phase 5 under any circumstances until a clear "1", "2", or "3"
  (or equivalent affirmation) is received.

---

## Phase 5 — Visual Gathering

**Goal:** Identify and curate all images that will appear in the final deck.
Triggered only after Phase 4 authorization is complete.

### Step 5.1 — Read the selected structure

Load the confirmed structure file from `src/structure/option-<N>.md`.
Build a list of slides that require supporting imagery (typically: section openers,
data context slides, CTA slides).

### Step 5.2 — Scan user-supplied attachments for images

Use the **File System skill** to list image files in:
```
<workspace>/slide/<title>/src/attachment/
```

Supported formats: `.jpg`, `.jpeg`, `.png`, `.svg`, `.webp`, `.gif`

For each image found, assess relevance against:
1. The PRD's target audience and tone
2. The specific slide it could illustrate

Document each accepted image:
```
- File: <filename>
- Assigned to: Slide <N> — <Slide title>
- Justification: <One sentence referencing the PRD>
```

Rejected images (not relevant) should be logged but not included.

### Step 5.3 — Search the internet for supporting images

Use the **Tavily Dynamic Search skill** to find contextually relevant images
for slides that lack user-supplied visuals.

For each search query:
- Derive the query from the PRD's key messages and target audience
- Use specific, descriptive queries — not generic ones
- Example: *"Indonesian government procurement data dashboard 2024"* not *"business chart"*

```
tavily-dynamic-search query: "<specific, PRD-derived image search query>"
include_images: true
search_depth: "advanced"
```

For each result image, apply the three-criteria relevance check from Rule 3 of
`.agents/rules/slide-preparation.md` before accepting it.

Document accepted web images:
```
- URL: <image_url>
- Assigned to: Slide <N> — <Slide title>
- Justification: <One sentence referencing the PRD>
```

### Step 5.4 — Compile image manifest

Write the full image manifest to:
```
<workspace>/slide/<title>/src/structure/image-manifest.md
```

Format:
```markdown
# Image Manifest — <presentation-title>
Generated: <ISO 8601 timestamp>
Selected structure: Option <N>

## Slide-by-Slide Image Assignments

| Slide | Title | Source | File/URL | Justification |
|-------|-------|--------|----------|---------------|
| 1 | ... | attachment | logo.png | Brand identity per PRD §1.2 |
| 4 | ... | web | https://... | Supports key message on ... per PRD §3.1 |
```

---

## Phase 6 — Execution

**Goal:** Trigger the main slide generation workflow with all context loaded.

### Step 6.1 — Assemble the generation brief

Compile the following inputs into a structured brief:

```
Brand: <from PRD or user preference>
Deck topic: <Presentation Goal from PRD>
Audience: <Target Audience from PRD>
Key points: <Key Messages from PRD>
Structure: <Selected option outline from src/structure/option-N.md>
Images: <Image manifest from src/structure/image-manifest.md>
Product context: <Relevant extracts from docs/product/>
Output path: <workspace>/slide/<title>/output/slides.html
```

### Step 6.2 — Invoke `/slide-generation`

Trigger the `/slide-generation` workflow with the assembled brief.

Pass all context directly — do not ask the user to re-enter information already
captured in Phases 1–5.

The `/slide-generation` workflow will:
1. Resolve brand DNA (from URL, library, or default)
2. Apply all 20 design principles from `power-design/principles/design-principles.md`
3. Emit a self-contained `slides.html`

### Step 6.3 — Save and confirm output

Use the **File System skill** to confirm `slides.html` has been written to:
```
<workspace>/slide/<title>/output/slides.html
```

Report to the user:
```
✅ Slide deck generated successfully.
Output: slide/<title>/output/slides.html
Slides: <N>
Structure used: Option <selected>
Images included: <N> (attachment: <N>, web: <N>)

Open slides.html in your browser to preview.
Want any changes? Describe them and I'll update the deck.
```

Enter refinement mode as defined in `.agents/rules/power-design.md` Rule 8.

---

## Error Recovery

| Phase | Failure | Recovery Action |
|-------|---------|-----------------|
| 1 | PDF extraction fails | Log error; continue with remaining PDFs; notify user |
| 2 | PRD missing | Halt; ask user to provide PRD |
| 3 | Cannot generate 3 distinct options | Generate 2 + ask user for direction on third |
| 4 | User is ambiguous | Re-present summary and ask again; do not guess |
| 5 | All Tavily results irrelevant | Present top 3 results to user and ask them to choose |
| 6 | `/slide-generation` not found | Halt; report path and ask user to verify skill installation |
