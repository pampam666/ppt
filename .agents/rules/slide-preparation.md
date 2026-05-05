---
trigger: always_on
---

# Rules — Slide Preparation
# Location: <workspace>/.agents/rules/slide-preparation.md
# Scope: Applies to every agent operating within the slide-preparation-flow workflow

---

## Activation Condition

These rules are ACTIVE whenever any of the following triggers are detected in a user request:

- Uses the phrase: "prepare slides", "prepare presentation", "slide preparation"
- Invokes the workflow: `/slide-preparation-flow`
- Requests work inside the `slide/<presentation-title>/` directory tree

---

## Rule 1 — Mandatory Directory Structure

Every presentation MUST follow this canonical folder layout.
The agent MUST create all directories before writing any file into them.

```
<workspace>/slide/<presentation-title>/
├── docs/
│   ├── prd/               ← PRD (Goals & Target Audience)
│   └── product/           ← Product Details (PDF extraction results as Markdown)
├── src/
│   ├── attachment/        ← User-uploaded raw files (PDFs, images, assets)
│   └── structure/         ← Structure draft options (3 files, one per option)
└── output/                ← Final slides.html deliverable
```

**Naming convention for `<presentation-title>`:** lowercase, hyphen-separated, no spaces.
Example: `annual-report-2025`, `product-launch-q3`.

The agent MUST NOT write files to any path outside this tree for a given presentation.

---

## Rule 2 — Authorization Gate (Wait for User Decision)

This is a hard stop. The agent MUST NOT proceed to Phase 5 (Visual Gathering) or Phase 6
(Execution) until the user has explicitly confirmed their structure choice.

After delivering 3 structure drafts:

1. Present a numbered summary of each draft (title + 3-sentence description)
2. Ask: *"Please select structure option 1, 2, or 3 to continue."*
3. **HALT** — do not process images, search the web, or call `/slide-generation` until a
   selection is received.

If the user asks to modify a draft before selecting, apply the modification, save the
updated file to `src/structure/`, and re-ask for confirmation. Do not skip the gate.

---

## Rule 3 — Image Relevance Standard

Images sourced from both the internet (Tavily) and the user's `src/attachment/` folder
MUST satisfy all three criteria before inclusion:

| Criterion | Requirement |
|-----------|-------------|
| **PRD alignment** | The image directly supports a goal stated in the PRD document |
| **Audience fit** | The visual tone matches the target audience (e.g., formal for B2G, modern for tech startups) |
| **Slide relevance** | The image is placed on the specific slide it illustrates — no decorative fillers |

The agent MUST document each selected image with:
- Source (URL or filename)
- Mapped slide number / section
- One-sentence justification referencing the PRD

Generic stock imagery (handshakes, generic city skylines, abstract blurs) is **prohibited**
unless the PRD explicitly calls for it.

---

## Rule 4 — Skill Dependency Declaration

Before executing any phase, the agent MUST verify that the following skills are available:

| Skill | Source | Required For |
|-------|--------|--------------|
| `filesystem` | `npx skillfish add csheng/dot-claude filesystem` | All phases |
| `pdf` (Composio) | `ComposioHQ/awesome-claude-skills/document-skills/pdf` | Phase 1 |
| `tavily-search` | `tavily-ai/skills/skills/tavily-search` | Phase 5 |
| `tavily-dynamic-search` | `tavily-ai/skills/skills/tavily-dynamic-search` | Phase 5 |
| `power-design` | Local `.agents/skills/power-design/` | Phase 6 |

If a required skill is unavailable, the agent MUST halt and report:
> "Required skill `<name>` is not installed. Install it before continuing."

---

## Rule 5 — PRD is the Single Source of Truth

All decisions — structure options, image selection, tone, language — must trace back to
the PRD document located at `<workspace>/slide/<presentation-title>/docs/prd/`.

The agent MUST quote the specific PRD section that justifies each structural decision
when presenting the 3 draft options to the user.

If no PRD exists, the agent MUST halt and ask the user to provide one before proceeding.
Do not infer or hallucinate PRD content.

---

## Rule 6 — Output Integrity

- The final output file MUST be saved to `<workspace>/slide/<presentation-title>/output/slides.html`
- The agent MUST NOT overwrite `slides.html` without user confirmation if the file already exists
- All intermediate files (Markdown extractions, structure drafts) MUST be preserved after output generation

---

## Rule 7 — What the Agent MUST NOT Do

- Process images or call Tavily before receiving structure selection from the user (Rule 2)
- Place output files outside the `output/` folder
- Infer or fabricate PRD goals, target audience, or product details
- Use images that are not directly relevant to the PRD and target audience (Rule 3)
- Skip the Authorization Gate under any circumstances, even if the user seems to imply urgency
- Mix content from different presentations in the same folder tree

---

## Rule 8 — Failure Handling

| Failure Mode | Agent Response |
|---|---|
| PRD file missing | Halt. Ask user to provide PRD before continuing |
| Attachment folder empty | Notify user; offer to proceed on PRD + manual input only |
| PDF extraction fails | Fall back to manual copy-paste from user; log the failure |
| Tavily returns irrelevant images | Retry with a refined query; if still irrelevant, flag for user review |
| `/slide-generation` workflow not found | Halt and report: "slide-generation workflow not found at `.agents/workflows/slide-generation.md`" |
| Output file already exists | Ask user: "slides.html already exists. Overwrite?" — never auto-overwrite |
