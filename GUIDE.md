# Slide Generation User Guide

Follow this step-by-step manual to prepare your workspace and generate a new presentation slide deck using the `/slide-preparation-flow`.

### Step 1: Workspace Preparation
First, you need to create a dedicated directory for your new presentation. 
Create a new folder named `<presentation-title>` (use lowercase, hyphen-separated names, e.g., `q3-marketing-report`) inside the root `slide/` directory. The agent will automatically scaffold the required subdirectories inside it when the workflow starts.

### Step 2: Data Ingestion (PRD)
The agent needs to understand the strategic context of your presentation. 
Place your Product Requirements Document (PRD) into the `docs/prd/` folder. This document must clearly outline the **presentation goals** and the **target audience**.

### Step 3: Reference Attachments
Provide the raw data and specific visual assets the agent should use.
Place all reference documents (such as PDFs with product details, data, or reports) and any specific manual images you want included into the `src/attachment/` folder.

### Step 4: Running the Agent
Once your PRD and attachments are in place, start the automation process. 
Type the following command into the chat to trigger the agent:
```text
/slide-preparation-flow
```

### Step 5: Validation Phase (Crucial)
After extracting your PDFs and analyzing your PRD, the system will **pause temporarily** and present you with **3 slide structure options** (outlines). 
**You must reply and select one of the options (e.g., "Option 2")**. The system is hard-coded to wait for your decision. It will not proceed with internet image searching or final slide execution until you confirm your choice.

### Step 6: Retrieving Results
Once the agent finishes generating the deck based on your chosen structure and gathered visuals, your final presentation will be ready. 
You can access and open the final `slides.html` file inside the `output/` folder.

---
*Note: If you need to make iterative changes to the final deck (like tweaking colors, fonts, or layout), you can simply ask the agent to refine the `slides.html` file directly!*
