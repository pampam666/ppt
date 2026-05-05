# Power Design User Guide

Welcome to the **Power Design** skill! This guide will teach you how to effortlessly generate beautiful, brand-aligned HTML presentation slides using Antigravity.

## How to Trigger the Skill
To start generating a slide deck, use one of the following trigger phrases in your request to the agent:
- "Use power-design"
- "Make me a deck"
- "Generate slides"
- "Create a presentation"
- "Build a slide deck"

## Step 1: Define the Brand
When the workflow starts, the agent needs to know the brand identity for the deck. You have three options:
1. **Provide a URL**: Simply paste a company URL (e.g., "Use Stripe's brand from stripe.com"). The agent will use Firecrawl to extract the live brand DNA (colors, fonts, voice).
2. **Use the Pre-built Library**: Name a well-known brand (e.g., "Use the Apple brand"). The agent will load the styling from our local library of 72+ brand systems.
3. **Use the Default**: If you say "skip" or don't specify a brand, the agent will use a clean, neutral template.

## Step 2: Structure Your Content Brief
Keep it simple. You don't need to write out every word. Provide the agent with a brief containing:
- **A Headline/Topic**: What is the presentation about?
- **3-5 Key Points**: The core ideas you want to communicate.
- **Audience (Optional)**: Who will be viewing this?
- **Slide Count (Optional)**: How many slides you want.

*Example Brief:*
> "Make me a deck about our Q3 Marketing Strategy. Key points: 1) We exceeded lead generation targets by 20%. 2) The new ad campaign launches next month. 3) We need to improve customer retention. Target audience is the executive team. 5 slides."

The agent will take this and architect a complete slide plan (One idea per slide, respecting the 20 design principles) before generating the final HTML.

## Step 3: The Refinement Loop
Once the agent delivers your `slides.html`, open it in your browser. If you want changes, just ask! The agent will enter a refinement loop:
- **Typography/Color**: "Make the title bigger" or "Make the background darker."
- **Layout**: "I want a full-bleed image on slide 3."
- **Content**: "Add a slide about our budget."
- **Brand Swap**: "Actually, let's see how this looks in the Linear brand style."

The agent will apply the changes slide-by-slide, re-validate against the design principles, and output a new `slides.html`. When you're happy with the result, just say **"Done"** or **"Ship it"**.
