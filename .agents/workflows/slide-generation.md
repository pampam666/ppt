# Workflow — Slide Generation
# Location: <workspace>/.agents/workflows/slide-generation.md
# Trigger: User requests slide/deck/presentation generation using power-design skill

---

## Workflow Identity

```
name: slide-generation
skill: power-design
version: 1.0.0
model_recommendation: claude-sonnet-4
trigger_phrases:
  - "use power-design"
  - "make me a deck"
  - "generate slides"
  - "create a presentation"
  - "build a slide deck"
rules_file: .agents/rules/power-design.md
```

---

## Execution Flow

```
START
  │
  ├─ STEP 1: Load Skill & Rules
  │
  ├─ STEP 2: Resolve Brand Source
  │
  ├─ STEP 3: Load Design Principles
  │
  ├─ STEP 4: Gather Content Brief
  │
  ├─ STEP 5: Plan Slide Architecture
  │
  ├─ STEP 6: Generate slides.html
  │
  ├─ STEP 7: Self-Validate Against 20 Rules
  │
  ├─ STEP 8: Deliver Output
  │
  └─ STEP 9: Enter Refinement Loop → (back to STEP 6 on change)
```

---

## STEP 1 — Load Skill & Rules

**Action:** Read the following files before any other operation:

```
READ: <workspace>/.agents/skills/power-design/SKILL.md
READ: <workspace>/.agents/rules/power-design.md
```

**Observation:** Confirm both files loaded successfully.

**Fallback:** If either file is missing:
> Halt execution. Output: "Required skill files not found. Please run the installation guide at `.agents/skills/power-design/INSTALL.md`."

**State after step:**
```json
{
  "step": "load-skill",
  "status": "completed",
  "skill_loaded": true,
  "rules_loaded": true
}
```

---

## STEP 2 — Resolve Brand Source

**Action:** Determine brand DNA source using this decision tree:

```
Did user provide a URL?
  YES → Call Firecrawl with URL → Extract: colors, fonts, voice, logo style
         └── On API error → Fallback to Step 2b
  NO  → Did user name a brand?
          YES → Load: .agents/skills/power-design/brands/<brand-name>.md
                └── File not found → List 5 closest matches → Ask user to pick
          NO  → Load: .agents/skills/power-design/brands/_template.md
```

**Brand DNA object to extract:**
```json
{
  "brand_name": "string",
  "primary_color": "#hex",
  "secondary_color": "#hex",
  "accent_color": "#hex",
  "background_color": "#hex",
  "font_display": "font name",
  "font_body": "font name",
  "brand_voice": "string (e.g. precise, minimal, bold)",
  "logo_style": "string (optional)",
  "source": "url | library | template"
}
```

**Observation:** Log which brand was resolved and from which source.

**State after step:**
```json
{
  "step": "resolve-brand",
  "status": "completed",
  "brand": { "...brand DNA object..." }
}
```

---

## STEP 3 — Load Design Principles

**Action:** Read the full design principles file:

```
READ: <workspace>/.agents/skills/power-design/principles/design-principles.md
```

**Internalize all 20 rules.** These are applied silently during generation — do not narrate rule-checking to the user.

**20-Rule Checklist (internal reference):**

| # | Rule | Hard Limit |
|---|---|---|
| 1 | One idea per slide | Split if violated |
| 2 | Glanceable in ≤3 seconds | Remove clutter |
| 3 | ≤7±2 chunks (ideal 3–5) | Trim or split |
| 4 | ≥40% whitespace | Enforce |
| 5 | 5% edge safe-zone all sides | Enforce |
| 6 | Type on modular scale 1.25–1.618 | Enforce |
| 7 | Max 4 type sizes per slide | Enforce |
| 8 | Body ≥24px, title ≥48px | Enforce |
| 9 | Line-height 1.4–1.6 body, 1.05–1.2 display | Enforce |
| 10 | Line length ≤60 chars | Enforce |
| 11 | WCAG contrast ≥4.5:1 body | Enforce |
| 12 | 60-30-10 color split | Enforce |
| 13 | One accent per slide | Enforce |
| 14 | No hue-only encoding | Enforce |
| 15 | 8pt grid for all spacing | Enforce |
| 16 | Align everything to one grid | Enforce |
| 17 | Related ≤16px, unrelated ≥48px spacing | Enforce |
| 18 | Data-ink ratio ≥80% (charts) | Enforce |
| 19 | F-pattern: headline + key visual top-left | Enforce |
| 20 | Two valid modes — pick ONE and stay | Commit once |

---

## STEP 4 — Gather Content Brief

**Action:** Ask the user for content input. Use a MAXIMUM of 3 questions:

```
Questions (ask in a single message, all at once):

1. What is the presentation about?
   (headline + 3–5 key points is sufficient; full content optional)

2. How many slides? (or say "you decide")

3. Any specific slide types needed?
   (e.g., title slide, data chart, timeline, comparison, quote, CTA)
```

**If user already provided content in their initial request:** Skip this step entirely.
Extract content from the request and proceed.

**Observation:** Content brief is complete when:
- A topic/headline exists
- At least 3 key points are defined (or user approves agent-generated points)
- Slide count is determined (agent defaults to 5–7 if not specified)

---

## STEP 5 — Plan Slide Architecture

**Action:** Before writing any HTML, plan the slide sequence:

```
Think through this structure:

Slide 1:  Title Slide — [Headline] + [Brand logo position] + [Subtitle]
Slide 2:  Problem / Context — [Key insight or opening statement]
Slide N:  [Content slides — one idea each]
Slide N+1: Data / Evidence — [Chart or key stat, if applicable]
Last Slide: CTA / Summary — [Single clear action or takeaway]
```

Output the plan to the user as a numbered list:
> "Here's the slide plan I'll build. Reply to adjust before I generate:"
> 1. Title — [headline]
> 2. [etc.]

**Wait for user confirmation OR proceed after 5 seconds with no response.**

---

## STEP 6 — Generate slides.html

**Action:** Generate a single, complete, self-contained HTML5 file.

**Technical requirements:**
- All CSS inline or in `<style>` block — no external stylesheets
- All fonts loaded via `@import` or `<link>` from Google Fonts (brand-specified fonts only)
- No JavaScript frameworks — vanilla JS only for navigation if needed
- Slide dimensions: 1280×720px (16:9) as the base viewport
- Navigation: keyboard arrow keys + optional prev/next buttons
- Print-friendly: `@media print` shows all slides as pages

**Per-slide generation checklist:**
```
For each slide:
  [ ] Apply brand colors (60-30-10 split)
  [ ] Apply brand fonts (display for titles, body for text)
  [ ] One idea only — split if needed
  [ ] Enforce whitespace ≥40%
  [ ] Body ≥24px, title ≥48px
  [ ] One accent color max
  [ ] Align to 8pt grid
  [ ] F-pattern layout (headline top-left or top-center)
  [ ] WCAG contrast verified
```

**Mode selection (Rule 20) — pick ONE before starting:**
- **Tufte mode:** Data-forward, minimal decoration, high information density
- **Reynolds mode:** Visual narrative, full-bleed imagery, one key phrase per slide

State the chosen mode to the user once: "I'm using [mode] for this deck."

---

## STEP 7 — Self-Validate Against 20 Rules

**Action:** After generation is complete, run an internal audit pass.

For each slide, verify:

```
AUDIT PASS:
  Rule 1  — Only one idea? YES / NO (fix: split slide)
  Rule 4  — Whitespace ≥40%? YES / NO (fix: remove elements)
  Rule 8  — Body ≥24px, title ≥48px? YES / NO (fix: increase font size)
  Rule 11 — Contrast ≥4.5:1? YES / NO (fix: darken/lighten text)
  Rule 13 — Only 1 accent per slide? YES / NO (fix: remove extra accents)
  Rule 20 — Consistent mode throughout? YES / NO (fix: normalize mode)
```

**Fix any violations before delivering output.**
Do not deliver a slide that fails any audit check.

---

## STEP 8 — Deliver Output

**Action:** Write the final HTML to disk and confirm delivery:

```
OUTPUT: slides.html → current working directory
```

Deliver to user with this summary:
```
✅ slides.html generated

Brand: [brand name] ([source: URL | library | template])
Mode: [Tufte | Reynolds]
Slides: [N] slides
Design rules: 20/20 applied

Open slides.html in any browser. Use ← → arrow keys to navigate.

Tell me what to change and I'll update it.
```

---

## STEP 9 — Refinement Loop

**Trigger:** User provides feedback after delivery.

**Action per feedback type:**

| Feedback Type | Agent Action |
|---|---|
| Typography change ("bigger title") | Update CSS for affected slides; re-audit Rule 8 |
| Color change ("darker background") | Update brand color token; re-audit Rule 11 |
| Brand switch ("use Linear instead") | Return to STEP 2 with new brand; regenerate |
| Content edit ("add a slide about X") | Add slide; re-audit Rules 1, 3 |
| Layout change ("full-bleed image") | Switch to Reynolds mode if not already set |
| "Start over" | Return to STEP 4 |
| "Done" / "Ship it" | Exit workflow |

**Output updated `slides.html` after every refinement round.**

---

## State Schema (Full)

The following JSON object tracks state across workflow steps:

```json
{
  "workflow": "slide-generation",
  "step": "current step name",
  "status": "in_progress | waiting_input | completed | failed",
  "brand": {
    "name": "string",
    "primary_color": "#hex",
    "secondary_color": "#hex",
    "accent_color": "#hex",
    "background_color": "#hex",
    "font_display": "string",
    "font_body": "string",
    "brand_voice": "string",
    "source": "url | library | template"
  },
  "design_mode": "tufte | reynolds | null",
  "content_brief": {
    "headline": "string",
    "key_points": ["string"],
    "slide_count": 0,
    "slide_types": ["string"]
  },
  "slide_plan": ["string"],
  "output_file": "slides.html",
  "audit_passed": true,
  "refinement_round": 0,
  "errors": [],
  "next_step": "string | null"
}
```

---

## Termination Conditions

The workflow ends when any of the following occur:

1. User says "done", "ship it", "looks good", or equivalent
2. A new unrelated task is started
3. An unrecoverable error occurs after 2 retry attempts
4. User explicitly cancels: "stop", "cancel", "start over from scratch"

On termination, the agent outputs a final delivery summary and exits the workflow context.
