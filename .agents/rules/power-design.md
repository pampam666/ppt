# Rules — Power Design Skill
# Location: <workspace>/.agents/rules/power-design.md
# Scope: Applies whenever the agent uses the power-design skill for slide generation

---

## Activation Condition

These rules are ACTIVE whenever any of the following triggers are detected in a user request:

- Mentions: "slide", "deck", "presentation", "slides.html"
- Uses the phrase: "use power-design"
- Requests a visual deliverable that maps to an HTML slide format

---

## Rule 1 — Always Load the Skill Runbook First

Before generating any output, the agent MUST read:

```
<workspace>/.agents/skills/power-design/SKILL.md
```

This file is the authoritative source for generation behavior.
Do not proceed with output generation until this file has been fully loaded.

---

## Rule 2 — Always Load the Design Principles

Before generating any slide content, the agent MUST load:

```
<workspace>/.agents/skills/power-design/principles/design-principles.md
```

All 20 design rules apply to every slide generated. There are no exceptions.
The agent applies rules silently — do not narrate rule checking to the user.

---

## Rule 3 — Brand Source Resolution (Ordered Priority)

When determining the brand to use, follow this resolution order:

1. **User provides a URL** → Use Firecrawl to extract live brand DNA (requires `FIRECRAWL_API_KEY`)
2. **User names a brand** → Load the matching file from `<workspace>/.agents/skills/power-design/brands/<name>.md`
3. **User says "skip" or "default"** → Use `brands/_template.md` as the base brand system
4. **Ambiguous brand name** → Ask the user to clarify before proceeding

The agent MUST NOT hallucinate brand colors, fonts, or styles.
If a brand file does not exist in the library, inform the user and offer alternatives.

---

## Rule 4 — One Idea Per Slide

Each slide must communicate exactly one idea.
If the user's content brief contains more than one idea for a single slide, the agent:
- Splits into multiple slides
- Informs the user: "I split [topic] into [N] slides to keep each focused."

Do not compress multiple ideas into one slide to reduce slide count.

---

## Rule 5 — Mandatory Design Constraints (Non-Negotiable)

The following constraints are hard limits derived from the 20 design rules.
The agent MUST enforce all of them on every slide:

| Constraint | Minimum |
|---|---|
| Whitespace ratio | ≥ 40% of slide area |
| Body font size | ≥ 24px |
| Title font size | ≥ 48px |
| WCAG contrast (body) | ≥ 4.5:1 |
| Color accent per slide | Maximum 1 accent color |
| Visual chunks per slide | Maximum 7, ideal 3–5 |
| Type sizes per slide | Maximum 4 distinct sizes |
| Data-ink ratio (charts) | ≥ 80% |

If a user instruction would violate any of these, the agent applies the rule and notes the override:
> "I adjusted [element] to meet the minimum [rule name] threshold."

---

## Rule 6 — Output Format

The agent MUST output slides as a single self-contained HTML file:

- **Filename:** `slides.html` (default) or user-specified name
- **Location:** Current working directory unless user specifies otherwise
- **Format:** Complete HTML5 document, no external dependencies, no CDN links for fonts not specified in brand DNA
- **Mode:** The agent picks ONE of the two valid modes from Rule 20 (minimalist data-forward OR visual narrative) and applies it consistently across ALL slides

Do not output slides as:
- Markdown
- PPTX
- PDF (unless explicitly requested as a secondary conversion)

---

## Rule 7 — No AI Aesthetic Anti-Patterns

The agent MUST NOT produce:

- Generic gradient backgrounds (blue-to-purple, etc.) unless brand-specified
- Drop shadows on chart bars or data elements
- Six or more bullet points on a single slide
- Clip-art or generic stock-style icon placeholders
- Centered wall-of-text layouts
- More than one animated transition style per deck

If the brand DNA does not specify these elements, the agent defaults to high-contrast, type-forward layouts.

---

## Rule 8 — Iterative Refinement Protocol

After delivering `slides.html`, the agent enters refinement mode:

- Accept natural language feedback: "make the title bigger", "switch to dark mode", "change the brand to Linear"
- Apply changes slide-by-slide, not wholesale regeneration, unless the change affects all slides
- Re-apply the 20 design rules after every change
- Output an updated `slides.html` after each refinement round

The agent stays in refinement mode until the user explicitly says "done" or starts a new task.

---

## Rule 9 — What the Agent MUST NOT Do

- Generate slides without loading `SKILL.md` first
- Invent brand colors, fonts, or voice not present in the brand source
- Apply design rules from memory — always load `design-principles.md`
- Ask more than 3 clarifying questions before starting generation
- Produce placeholder content (e.g., "Lorem ipsum", "[Insert text here]")
- Mix two brand systems on the same deck

---

## Rule 10 — Failure Handling

| Failure Mode | Agent Response |
|---|---|
| SKILL.md not found | Halt and report: "power-design skill not found at expected path. Run the install guide." |
| Brand file not found | Offer the 5 closest matches from the brand library |
| Firecrawl API error | Fall back to pre-built brand library; inform user |
| Brand DNA insufficient | Ask user for primary color, font name, and one example URL |
| Output file write error | Output HTML inline in the chat and prompt user to save manually |
