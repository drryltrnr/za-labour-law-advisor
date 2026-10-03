# Gazette Verification — Search, Sources, Citation and Figures (SKILL.md Sections 1.B, 1.C, 1.E)

**Load when:** Fetching any figure, notice, proclamation or Act text; a search comes back empty; setting out citations in a document.

Section numbers are the skill's section identifiers; SKILL.md Section 0.C shows which file holds each. This file records the law as last verified (`watch-list.md` lists what moves on known dates). Run SKILL.md Section 1 on everything in it before relying on it.

## B. Search Execution

Run these patterns against Government Printing Works, the official departmental domains (labour.gov.za, justice.gov.za, treasury.gov.za, sars.gov.za, fsca.co.za) and gazette repositories:

| Target | Search pattern |
| :--- | :--- |
| **Any Act — recent amendments** | `"[Full Title of Act]" "amendment act" "Government Gazette" site:gov.za OR site:gpwonline.co.za` |
| **Presidential commencement proclamation** | `"[Name of Amendment Act]" "proclamation" "commencement" "Government Gazette"` |
| **Ministerial regulations & notices** | `"[Title of Act]" "regulations" "Government Gazette" site:labour.gov.za OR site:gov.za` |
| **BCEA s 6(3) earnings threshold** | `"earnings threshold" "Basic Conditions of Employment Act" "Government Gazette" "per annum"` |
| **National Minimum Wage adjustment** | `"National Minimum Wage" "Government Gazette" "per hour" "effective" site:labour.gov.za` |
| **Bargaining council extension** | `"[Council Name]" "extension to non-parties" "Government Gazette" site:gpwonline.co.za OR site:labour.gov.za` |
| **Benefit fund contribution rates & changes** | `"[Fund name]" "contribution rate" "Circular" OR "Government Gazette"` — for the MEIBC funds add `site:mibfa.co.za OR site:meibc.co.za` |
| **Pension Funds Act s 13A / regulations** | `"Pension Funds Act" "Section 13A" "Government Gazette" OR "FSCA" site:fsca.co.za` |
| **Codes of Good Practice** | `"Code of Good Practice" "[Subject]" "Government Gazette" site:labour.gov.za` |
| **Court declarations of invalidity** | `"[Act Name]" "unconstitutional" OR "declaration of invalidity" "Constitutional Court" site:saflii.org` |

**gov.za's Documents & Notices index** (https://www.gov.za/documents/notices) is searchable and sortable by title and date and lists the Gazette (G) and Notice number for each entry — use it to pin down or double-check a GN/GG citation rather than trusting a secondary source's transcription. Industry commentary (employer-association newsletters, law-firm blog posts, HR-service bulletins) is frequently imprecise about the exact notice number, or simply outdated by the time you read it. Where the index is inconclusive, prefer a source reproducing the operative notice's own text (for example a renewal notice reciting the instrument it renews) over one that merely asserts a number secondhand.

## Where to read primary text

| Need | Read it at | Watch for |
| :--- | :--- | :--- |
| An Act as currently in force, or as at a past date | lawlibrary.org.za (consolidated Acts with point-in-time versions) | The version's "as at" date — then check for amending Acts after it |
| As-enacted Acts and amending Acts | gov.za Acts pages; for tax Acts, SARS's Amendment Acts page | gov.za's "Amended by" lists and attached consolidations can lag (Section 1.A) |
| Current gazettes | gpwonline.co.za e-Gazettes, browsable by publication date and gazette number | Recent gazettes rarely surface in keyword search — browse by date |
| Older gazettes | archive.opengazettes.org.za, browsable by year | Thin coverage of the latest months; OCR can garble headings |
| Gazette and notice numbers | gov.za Documents & Notices index | Use it to pin a citation, then read the instrument itself |
| Judgments | saflii.org; lawlibrary.org.za | Open the judgment and check for a later appeal before citing it |

* Where a legal-research tool or connector indexing South African legislation, case law or gazettes is available in the session, search it first with the jurisdiction set to South Africa. Treat its hits as pointers: open the document itself before citing it.
* Where a fetch tool refuses a site, do not work around the refusal by another route. Go down the ladder in SKILL.md Section 1.B instead, and record in the audit trail what could not be fetched.

## C. Full Citation Format

1. **Bargaining council agreements** — council, full agreement title, gazetted extension notice, section (e.g. *MEIBC Main Collective Agreement, extended to non-parties by GN …, Part I s 4 (Hours of Work)*).
2. **Benefit fund instruments** — governing collective agreement read with the primary statute (e.g. *MEIBC Benefit Fund Collective Agreement read with s 13A of the Pension Funds Act 24 of 1956*).
3. **Primary Acts** — title, number, year, and the amending Act (e.g. *COIDA 130 of 1993, as amended by the COIDA Amendment Act 10 of 2022*).
4. **Subordinate legislation** — Gazette number, Notice number, effective date.
5. **Codes of Good Practice** — the currently operative Code, with its effective date.
6. **Subsections and neutral citations** — exact subsections (*BCEA s 34(1)*, *PFA s 13A(8)*, *LRA s 198A(3)(b)*) and neutral citations (`[YYYY] ZACC XX`, `[YYYY] ZALAC XX`).

## E. Volatile Figures — the Fetch Table

**This skill states no current monetary figure.** Fetch every one at the moment of use from the source below, and cite the notice actually fetched.

| Figure | Set by | Where to fetch it |
| :--- | :--- | :--- |
| **BCEA s 6(3) earnings threshold** | Ministerial determination under BCEA s 6(3), gazetted | gov.za notices index, search *"Determination: Earnings threshold"*; also the DEL notice library at labour.gov.za (Regulations and Notices → Basic Conditions of Employment) |
| **National Minimum Wage** | Annual review under NMWA s 6(2), gazetted | gov.za notices index, search *"National Minimum Wage"* + the relevant year |
| **Prescribed rate of interest** | Determined by the Minister of Justice under the Prescribed Rate of Interest Act 55 of 1975, historically as repo rate plus a margin; gazetted, but notices are sometimes published late or not at all | gov.za notices index, search *"Prescribed rate of interest"*; where no current notice is found, cross-check the repo-rate-linked figure against at least two reputable practitioner trackers and say in the document that the rate is "as prescribed from time to time" |
| **COIDA Schedule 4 maximum and minimum compensation amounts** | Ministerial notice amending Schedule 4 | gov.za notices index, search *"Compensation for Occupational Injuries and Diseases Act" "Schedule 4"*; the notice recites the amounts and its own effective date |
| **COIDA assessment tariffs** | Compensation Fund / licensee notices | Compensation Fund and licensee (e.g. RMA) published tariff notices |
| **UIF contribution ceiling** | Ministerial notice under the UIC Act | gov.za notices index, search *"Unemployment Insurance Contributions Act" "contribution"*; cross-check against the current SARS *Guide for Employers in respect of Unemployment Insurance Fund* |
| **Tax tables and rebates** | Annual Budget / Rates and Monetary Amounts Act for the year | sars.gov.za tax rates pages for the year of assessment in issue |
| **Benefit fund contribution percentages** (employer and employee, by fund) | The fund's rules or the bargaining council's benefit fund collective agreement (the MEIBC funds revise on a 1 July cycle) | The fund administrator and the council circular for the period in issue (for the MEIBC funds, mibfa.co.za); confirm against the governing rules or agreement as extended |
| **Bargaining council wage scales, shift and overtime schedules** (e.g. MEIBC Rates A–H) | The council's main collective agreement wage schedules and circulars | The council's circulars (for the MEIBC, meibc.co.za), read with the gazetted extension notice for the period in issue |
| **Bargaining council administration and dispute resolution levies** | The council's levy agreements as renewed (for the MEIBC, the Registration and Administration Expenses and Dispute Resolution Collective Agreements); rates published in council circulars | The council's circulars for the period in issue — **not** a renewal notice, which often carries no rates (Section 1.D) |

**Three traps when fetching:**

1. **Check for a correction notice.** Determinations — the BCEA earnings threshold especially — have been followed by gazetted *Correction* notices. Always search for one published after the determination you found; the corrected figure is the operative one.
2. **Reconcile the per-annum and per-month figures against each other.** If the monthly figure multiplied by twelve does not equal the annual figure, you have transcribed one of them wrongly, or you are looking at a determination and its correction at the same time. Resolve it before either number is used.
3. **Read the effective date, not just the amount.** A figure is only the right one for the period the dispute concerns. Where a claim spans a rate change, apply each rate to its own period and say so.
