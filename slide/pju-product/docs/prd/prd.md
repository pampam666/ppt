---

# PRD: 60W 3-in-1 Solar Street Light Package

---

## 1. Goal Presentation

### 1.1 Strategic Objectives

The primary goal of this presentation is to position the **60W 3-in-1 Solar Street Light (PJU Tenaga Surya)** package as the definitive, turnkey off-grid public lighting solution for infrastructure projects across Indonesia — particularly in areas underserved by the national grid (PLN). The presentation must accomplish three strategic outcomes:

- **Build confidence in technical completeness:** Demonstrate that all four components (solar panel, battery, LED luminaire, and charge controller) are pre-validated for compatibility, eliminating integration risk for the buyer.
- **Justify investment through lifecycle economics:** Shift the procurement conversation from upfront cost to total cost of ownership (TCO), highlighting zero monthly electricity spend, a 10-year battery calendar life, and a 50,000-hour lamp lifetime (L70).
- **Accelerate decision-making for field and project teams:** Provide enough specification depth — wattages, voltages, IP ratings, certifications — that contractors and technical leads can evaluate the package without requiring additional vendor consultations.

### 1.2 Technical Goals

The presentation must communicate the following technical value propositions, derived exclusively from component datasheets:

- **Energy generation:** The ICA Solar ICA200-72M monocrystalline panel (200Wp, 22.44% efficiency, Voc 50.53V) directly drives the SRNE SES60 controller within its ≤55V PV input limit, forming a coherent 24V system architecture.
- **Energy storage adequacy:** The RITAR LFP25.6V50AH battery (1,280Wh total energy, >2,000–4,000 cycles, IP65) provides full-night reserve capacity, with BMS protection against overcharge, over-discharge, overcurrent, short circuit, and thermal extremes — reducing field failure risk.
- **Illumination quality:** The OSRAM LEDENVO 60W DC luminaire (7,200 lm at 4000K/5700K, 120 lm/W efficacy, 150°×70° beam angle, IP66, 5KV surge protection) meets ME3–ME5 road classification standards, suitable for residential, rural, and industrial road applications.
- **Intelligent load management:** The SRNE SR-SES60 Gen4 PWM controller (IP67, 10-period programmable dimming, PIR/microwave motion sensing, SOC-based automatic power modes, infrared wireless configuration) enables adaptive energy use, extending battery life on low-traffic nights without manual intervention.
- **System autonomy:** The fully automatic operation cycle — solar charging by day, photocell-triggered illumination by night, motion-adaptive dimming during off-peak hours — requires zero human intervention after commissioning.

### 1.3 Presentation Success Criteria

The deck will be considered successful if a field contractor or procurement officer, after viewing it, can:

1. Understand the complete energy flow from PV panel to luminaire without referencing external documents.
2. Identify all critical electrical parameters (voltages, currents, IP ratings, certifications) required for a site compatibility assessment.
3. Articulate the 3–5 key differentiators of this package versus a conventional grid-tied (PLN) street light installation.
4. Feel confident enough to proceed to a quotation or site survey request.

---

## 2. Target Audience

### 2.1 Primary Audience — Field Contractors & Installation Teams

**Profile:** Electrical or civil contractors responsible for physical installation, commissioning, and handover of public lighting infrastructure. Typically operate at the project execution level, not the procurement decision-making level.

**Expertise level:** Technically literate — comfortable with wiring diagrams, IP ratings, and component specs, but not necessarily familiar with solar-specific terminology (e.g., Voc, NOCT, PWM charging, SOC-based dimming).

**Pain points addressed by this package:**

- **No grid trenching required:** Eliminates the most labor-intensive and cost-escalating element of conventional PJU installation — underground cable runs.
- **Single-vendor component set:** All four components arrive as a validated system, reducing sourcing complexity and on-site compatibility troubleshooting.
- **Self-contained controller logic:** The SRNE SES60 Gen4 handles all charge regulation, load switching, and dimming automatically; no external PLCs or timers are required.
- **Robust weatherproofing:** IP65 (battery), IP66 (luminaire), and IP67 (controller) ratings reduce rework calls from weather-related failures.
- **Fast commissioning:** Pole-mounted, plug-and-play wiring topology allows a small team to install and commission a unit in a single site visit.

### 2.2 Secondary Audience — Technical Procurement Officers & Project Managers

**Profile:** Government agency procurement officers (PUPR, Dinas PU), private infrastructure developers, and project managers evaluating solar PJU packages for tender compliance and value-for-money assessment.

**Expertise level:** Moderate technical understanding. Primarily focused on compliance documentation, certification status, lifecycle cost, and vendor accountability.

**Pain points addressed by this package:**

- **SNI & international certification coverage:** The ICA200-72M carries SNI IEC 61215 & IEC 61730, satisfying Indonesian government procurement standards. The RITAR battery holds UN38.3 and CE; the OSRAM luminaire holds CB, CQC, and RoHS.
- **Quantifiable ROI narrative:** Zero monthly electricity cost vs. PLN-tariff-dependent conventional systems; 10-year battery life and 50,000-hour lamp life directly reduce maintenance budget line items.
- **Scalability proof:** Battery parallelism (up to 4 units) and the controller's 12V/24V system voltage flexibility demonstrate the platform can be scaled to higher-demand installations without a full redesign.
- **Reputable brand anchoring:** OSRAM luminaire and SRNE controller are globally recognized brands, reducing perceived procurement risk in tender evaluations.
- **Off-grid deployment suitability:** Designed explicitly for locations without PLN grid access — rural roads, industrial estates, plantation access roads — expanding project scope to geographies previously excluded from conventional PJU programs.

### 2.3 Audience Communication Implications

| Audience Segment | Presentation Priority | Technical Depth Required |
|---|---|---|
| Field Contractors | System wiring, IP ratings, installation steps, controller programming | High — include Voc, Vmp, charge voltages |
| Procurement Officers | Certifications, brand credibility, lifecycle cost, scalability | Medium — comparative ROI table + certification summary |
| Project Managers | System autonomy, maintenance reduction, deployment flexibility | Medium — energy flow diagram + uptime reliability narrative |

All slide content must be delivered in **Bahasa Indonesia** to ensure accessibility for both field-level and office-level stakeholders across all Indonesian project regions.

---

*PRD Version: 1.0 | Prepared for: Slide Deck Generation — 60W PJU Tenaga Surya 3-in-1*
*Source: ICA Solar ICA200-72M · RITAR LFP25.6V50AH · OSRAM LEDENVO 60W · SRNE SR-SES60 Gen4 datasheets + presentation brief*

---

A few things worth noting about what this PRD captures that your previous prompt didn't make fully explicit:

**System voltage coherence** — the datasheets confirm this is a 24V system: the RITAR battery is 25.6V nominal, the SRNE SES60 supports 12V/24V with a ≤55V PV input (which accommodates the panel's 50.53V Voc), and the OSRAM LEDENVO 60W DC has a 15V–60V load voltage range on the controller side. This is worth emphasizing in Slide 8 (the energy flow diagram) since it validates the system as genuinely engineered rather than just assembled.

**One correction on the controller model** — the datasheet labels the product as **SR-SES Series / SES60 Gen4**, and the IP rating in the spec table is **IP67** (not IP65 as sometimes cited in the previous prompt). Worth updating that in the slide deck.