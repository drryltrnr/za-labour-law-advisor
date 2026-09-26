---
name: za-labour-law-advisor
description: "Strategic analysis, legal text auditing and document drafting for South African statutory labour frameworks (BCEA, LRA, COIDA, EEA, NMWA, UIA, CCMA and bargaining council rules, SARS PAYE/UIF), with MEIBC and MIBFA reference files for the metal and engineering sector. Use for workplace injury (IOD/COIDA) claims, earning income or resigning while a claim is open, constructive dismissal, wage clawbacks and unlawful deductions, CCMA or bargaining council referrals, PAYE/UIF payroll disputes, pension-contribution non-remittance, or when drafting a letter of demand, affidavit, resignation letter or formal complaint against a South African employer. Every cited Act, amendment, commencement proclamation and gazetted figure is fetched and verified before use."
---

# South African Labour Law & Statutory Compliance

## Scope

Analysis of labour disputes, audits of employer payroll and statutory non-compliance, and drafting of letters of demand, CCMA and bargaining council referral statements, resignation letters, Pension Funds Adjudicator complaints, sworn affidavits and COIDA/RMA correspondence. The rules below carry the weight: run them in the order of Section 0, and stop at Section 6 when a matter needs a practitioner.

## 0. Working Sequence

1. **Run the Gazette cross-check (Section 1)** for every Act, regulation or collective agreement the dispute triggers — in-force text, amendment Acts, commencement proclamations, gazetted figures.
2. **Classify the sector and load references.** Establish whether a bargaining council has jurisdiction, and load the reference files the facts trigger (table below) before going further.
3. **Establish jurisdiction** — bargaining council, CCMA, DEL Inspectorate, Compensation Commissioner or licensee, Labour Court.
4. **Identify the instruments triggered** — BCEA, LRA, COIDA as amended by Act 10 of 2022, EEA, UIA, Income Tax Act, any binding collective agreement.
5. **Audit substantive compliance** — hours, overtime, wages, deductions, leave, injury reporting, compensation, fund remittance, PAYE/UIF treatment.
6. **Anticipate the next questions.** An injured worker whose claim has stalled asks next whether they may earn elsewhere, whether they can leave, and whether leaving is a constructive dismissal. Answer those together (Section 3) — each move changes the others.
7. **Draft or review**, with full section, gazette and collective-agreement citations, naming personal director liability under PFA s 13A(8) where it arises.
8. **Check escalation triggers (Section 6)** and embed the Gazette Verification & Statutory Audit Trail in the output.

### Reference files — load only when triggered

| File | Load when |
| :--- | :--- |
| `references/meibc-mibfa.md` | Employer is in the metal and engineering sector (MEIBC scope); the dispute touches council levies, bargaining council extension or renewal notices, MEIBC CDR jurisdiction or MIBFA funds; or pension/provident contributions were deducted but not paid over (Pension Funds Act s 13A) in any sector |
| `references/injured-worker-exit.md` | An employee asks about earning income while a COIDA claim is open, resigning or what leaving costs, or constructive dismissal |
| `references/sars-paye-uif.md` | PAYE withholding, UIF contributions, IRP5/EMP501 coding, tax treatment of compensation, the choice of SARS channel, or tax on new earnings taken on while a claim is open |

## 1. Universal Government Gazette Cross-Check Protocol

You **MUST actively cross-check the Government Gazette for any amendment to ANY Act or collective agreement** before advising, auditing or drafting. Under s 81 of the Constitution an Act of Parliament takes effect when published in the Gazette, or on a date determined in terms of the Act. Subordinate legislation, ministerial determinations and the extension of collective agreements to non-parties obtain legal force **only upon publication in the Government Gazette** — so the gazette, not the commentary about it, is the thing to read.

### A. Three-Tier Verification Standard

```
[Tier 1: Principal Act & Enacted Amendment Acts]
       │  (Has Parliament passed an amending statute touching these sections?)
       ▼
[Tier 2: Presidential Commencement Proclamations]
       │  (Has a Proclamation actually commenced those sections?)
       ▼
[Tier 3: Subordinate Gazetted Regulations, Determinations & Codes]
          (Have regulations, thresholds or codes been gazetted?)
```

1. **Tier 1** — verify the in-force text of the principal statute (BCEA 75 of 1997, COIDA 130 of 1993, LRA 66 of 1995, EEA 55 of 1998, Pension Funds Act 24 of 1956, Income Tax Act 58 of 1962, UIC Act 4 of 2002, Unemployment Insurance Act 63 of 2001, POPIA 4 of 2013, Protected Disclosures Act 26 of 2000), then search for amending Acts that insert, substitute or repeal the sections in play. Verify against primary statutory text — a raw fetch of the Act itself, not a summarised or remembered mapping. Consolidations on free legal portals often lag amendments; check the "current to" date the portal states.
2. **Tier 2** — **never assume an enacted Amendment Act is in force.** An Act passed by Parliament and signed by the President does *not* automatically come into operation where the commencement clause reads *"This Act comes into operation on a date fixed by the President by proclamation in the Gazette."* Check for the Proclamation, and check whether commencement was staggered by section. Amendment Acts frequently commence years after assent, in tranches.
3. **Tier 3** — check ministerial notices adjusting figures or binding standards (see Section E).

### B. Search Execution

Run these patterns against Government Printing Works, the official departmental domains (labour.gov.za, justice.gov.za, treasury.gov.za, sars.gov.za, fsca.co.za) and gazette repositories:

| Target | Search pattern |
| :--- | :--- |
| **Any Act — recent amendments** | `"[Full Title of Act]" "amendment act" "Government Gazette" site:gov.za OR site:gpwonline.co.za` |
| **Presidential commencement proclamation** | `"[Name of Amendment Act]" "proclamation" "commencement" "Government Gazette"` |
| **Ministerial regulations & notices** | `"[Title of Act]" "regulations" "Government Gazette" site:labour.gov.za OR site:gov.za` |
| **BCEA s 6(3) earnings threshold** | `"earnings threshold" "Basic Conditions of Employment Act" "Government Gazette" "per annum"` |
| **National Minimum Wage adjustment** | `"National Minimum Wage" "Government Gazette" "per hour" "effective" site:labour.gov.za` |
| **Bargaining council extension** | `"[Council Name]" "extension to non-parties" "Government Gazette" site:gpwonline.co.za OR site:labour.gov.za` |
| **Codes of Good Practice** | `"Code of Good Practice" "[Subject]" "Government Gazette" site:labour.gov.za` |
| **Court declarations of invalidity** | `"[Act Name]" "unconstitutional" OR "declaration of invalidity" "Constitutional Court" site:saflii.org` |

Sector-specific patterns (MIBFA, Pension Funds Act s 13A) are in `references/meibc-mibfa.md`.

**gov.za's Documents & Notices index** (https://www.gov.za/documents/notices) is searchable and sortable by title and date and lists the Gazette (G) and Notice number for each entry — use it to pin down or double-check a GN/GG citation rather than trusting a secondary source's transcription. Industry commentary (employer-association newsletters, law-firm blog posts, HR-service bulletins) is frequently imprecise about the exact notice number, or simply outdated by the time you read it. Where the index is inconclusive, prefer a source reproducing the operative notice's own text (for example a renewal notice reciting the instrument it renews) over one that merely asserts a number secondhand.

#### Finding a recent notice when search fails — work down this ladder

**A keyword search that returns nothing is not evidence that a notice does not exist.** Search engines and the gov.za notices index routinely fail to surface notices from the current and preceding year, and guessed direct URLs almost always 404. Never report a notice as unlocatable, and never draft around its absence, until this ladder is exhausted:

1. **Browse the Government Printing Works e-Gazette archive by date, not by keyword.** gpwonline.co.za publishes gazettes by publication date and gazette number. If the date or the gazette number is known — from commentary, a circular, or one notice already in hand — go to the archive for that date and open the gazette itself. Keyword search is the wrong instrument; the archive is browsable.
2. **Enumerate the neighbouring notice numbers.** Related instruments are gazetted together at **consecutive notice numbers** in the same gazette. Once one notice in a family is in hand, retrieve N+1, N+2, N+3 before accepting anyone's summary of what the family did. Per-notice extracts are conventionally named `g{gazette}gn{notice}.pdf` (for example `g54698gn3941.pdf`), so the neighbours are directly addressable once one is known.
3. **Ask the body that administers the instrument.** A bargaining council holds its own gazettes and circulars; the Compensation Fund and licensees hold theirs. Asking costs nothing, and it puts that body's own answer on the record — which is worth more in a dispute than a copy you found yourself.
4. **Ask the user.** People running their own matters frequently already hold the gazette, or can pull it in minutes from a source no search will reach. Say precisely which notice and gazette number you need and why.

Record in the audit trail *how* each instrument was obtained, not merely that it was.

### C. Full Citation Format

1. **Bargaining council agreements** — council, full agreement title, gazetted extension notice, section (e.g. *MEIBC Main Collective Agreement, extended to non-parties by GN …, Part I s 4 (Hours of Work)*).
2. **Benefit fund instruments** — governing collective agreement read with the primary statute (e.g. *MEIBC Benefit Fund Collective Agreement read with s 13A of the Pension Funds Act 24 of 1956*).
3. **Primary Acts** — title, number, year, and the amending Act (e.g. *COIDA 130 of 1993, as amended by the COIDA Amendment Act 10 of 2022*).
4. **Subordinate legislation** — Gazette number, Notice number, effective date.
5. **Codes of Good Practice** — the currently operative Code, with its effective date.
6. **Subsections and neutral citations** — exact subsections (*BCEA s 34(1)*, *PFA s 13A(8)*, *LRA s 198A(3)(b)*) and neutral citations (`[YYYY] ZACC XX`, `[YYYY] ZALAC XX`).

### D. Zero Tolerance for Unverified or Superseded Law

* Never cite historical earnings thresholds, minimum wages, contribution rates or unproclaimed bills from memory.
* Never cite a BCEA baseline where a collective agreement binding the employer sets a different standard (the MEIBC 40-hour week is the standing example — `references/meibc-mibfa.md`).
* Never cite the superseded Schedule 8 of the LRA for dismissal procedure without the currently operative Code of Good Practice: Dismissal.
* **Never cite a case you have not opened.** Confirm the neutral citation, court and holding on SAFLII before it goes into a document; a case quoted in commentary may have been overturned on appeal.
* **Statutory time periods are as easy to misremember as section numbers, and are repeated confidently and wrongly across the internet.** Read the period off the Act, and check whether an amendment Act substituted the subsection you are quoting. The seven-day employer accident report under COIDA s 39(1) — routinely misquoted as thirty days — is the standing example.
* **A notice covers only what its own heading and text say it covers.** Where commentary reports several instruments moving together, that means several *separate* notices at consecutive numbers. Do not attribute to one notice what a group of them did — enumerate the neighbours per Section 1.B and read each.
* **A renewal or extension notice frequently contains no figures at all.** Many consist of a single operative sentence declaring an earlier notice effective for a further period. Rates, levies and wage tables live in the underlying agreement and in the council's circulars. Never cite a notice as the source of a number you did not read in that notice.
* **A document's filename is not evidence of what it is, and a scan cannot be searched.** Where an annexure is a scanned image with no text layer, render or open it and read it before relying on it. A file saved under the right name may be the wrong gazette; an older instrument in the same chain will look plausible and mislead you about which one is operative.
* **Never "correct" a user's citation on the strength of an older instrument in the same chain.** Renewal chains run for decades: the agreement renewed in 2019 may not be the agreement renewed in 2026. Establish which link is operative *for the period in dispute* before changing anything the user wrote.
* Getting the substance right but the citation wrong is exactly the defect that destroys credibility in a sworn document, and it is entirely avoidable.

### E. Volatile Figures — Never Carry a Number, Fetch It

**This skill deliberately states no current monetary figure.** Thresholds, wage rates, ceilings, contribution percentages and interest rates all move on their own cycles; any number written into a skill is wrong by the time someone relies on it. Fetch every one of them, at the moment of use, from the source below — and cite the notice you actually fetched. Sector and payroll figures (MEIBC scales and levies, MIBFA rates, the UIF ceiling, tax tables) are listed in the reference files.

| Figure | Set by | Where to fetch it |
| :--- | :--- | :--- |
| **BCEA s 6(3) earnings threshold** | Ministerial determination under BCEA s 6(3), gazetted | gov.za notices index, search *"Determination: Earnings threshold"*; also the DEL notice library at labour.gov.za (Regulations and Notices → Basic Conditions of Employment) |
| **National Minimum Wage** | Annual review under NMWA s 6(2), gazetted | gov.za notices index, search *"National Minimum Wage"* + the relevant year |
| **Prescribed rate of interest** | Determined by the Minister of Justice under the Prescribed Rate of Interest Act 55 of 1975, historically as repo rate plus a margin; gazetted, but notices are sometimes published late or not at all | gov.za notices index, search *"Prescribed rate of interest"*; where no current notice is found, cross-check the repo-rate-linked figure against at least two reputable practitioner trackers and say in the document that the rate is "as prescribed from time to time" |
| **COIDA Schedule 4 maximum and minimum compensation amounts** | Ministerial notice amending Schedule 4 | gov.za notices index, search *"Compensation for Occupational Injuries and Diseases Act" "Schedule 4"*; the notice recites the amounts and its own effective date |
| **COIDA assessment tariffs** | Compensation Fund / licensee notices | Compensation Fund and licensee (e.g. RMA) published tariff notices |

**Three traps when fetching:**

1. **Check for a correction notice.** Determinations — the BCEA earnings threshold especially — have been followed by gazetted *Correction* notices. Always search for one published after the determination you found; the corrected figure is the operative one.
2. **Reconcile the per-annum and per-month figures against each other.** If the monthly figure multiplied by twelve does not equal the annual figure, you have transcribed one of them wrongly, or you are looking at a determination and its correction at the same time. Resolve it before either number is used.
3. **Read the effective date, not just the amount.** A figure is only the right one for the period the dispute concerns. Where a claim spans a rate change, apply each rate to its own period and say so.

**Tripwire:** whenever a fetched figure differs from a figure already stated in the user's own documents, correspondence or earlier drafts, stop and say so before going further. That mismatch is either an error to correct before service or a rate change to plead expressly — it is never something to paper over.

## 2. Core Legislative Frameworks

Bargaining council, MEIBC and MIBFA rules live in `references/meibc-mibfa.md`; SARS, PAYE and UIF contribution rules in `references/sars-paye-uif.md`. Load them per Section 0.

### A. BCEA 75 of 1997 and NMWA 9 of 2018

* **s 6(3) earnings threshold** — employees earning above the gazetted threshold are excluded from the Chapter 2 protections (hours, overtime, Sunday pay, meal intervals, public holiday pay for non-working days); those at or below retain non-derogable overtime rights. Fetch the threshold and its effective date per Section 1.E every time.
* **s 34 (deductions)** — a deduction is unlawful unless (i) the employee agreed in writing to the deduction in respect of a debt specified in the agreement, or (ii) the deduction is required or permitted by law, collective agreement, court order or arbitration award. **s 34(2)** sets the conditions for deductions in respect of loss or damage, including that the total of such deductions may not exceed one-quarter of the employee's remuneration in money. **s 34(5)** deals separately with remuneration paid in error. **Read s 34 in full before relying on the interplay between (1), (2) and (5), and do not transplant the one-quarter cap from the loss-or-damage regime onto an over-payment recovery without checking the text.** Unilateral employer "clawbacks" of a disputed amount are self-help and unlawful — *North West Provincial Legislature v NEHAWU obo 158 Members* [2023] ZALAC 12. A clawback can never bypass a statutory calculation or breach a minimum wage.
* **Termination entitlements** — on any termination, read and apply the BCEA's payments-on-termination and certificate-of-service provisions (accrued annual leave pay in particular) before the final payslip is accepted.
* **Parental leave** — the leave provisions were the subject of a Constitutional Court ruling in *Van Wyk v Minister of Employment and Labour*; check for the amending legislation and its commencement before advising on entitlements.
* **NMWA** — no contract or sectoral determination may undercut the gazetted hourly rate.

### B. COIDA 130 of 1993, as amended by Act 10 of 2022

**Commencement matters.** The Amendment Act's provisions commenced on staggered dates; several of the penalty provisions below took effect on 1 April 2026. Check the date of the conduct and of any document against the relevant commencement before characterising a request as a criminal referral rather than an administrative penalty, and verify the commencement proclamation rather than relying on a remembered gazette number.

* **Right to compensation** — s 22 read with s 47. The 75% temporary total disablement rate is set by **s 47(1)(a) read with Schedule 4, Item 1**. Cite that pairing, never s 63, when quantifying the compensation floor. Schedule 4's maximum and minimum amounts are amended by ministerial notice — fetch the operative notice per Section 1.E and check the claim against the ceiling before relying on the floor.
* **s 22(2)** — *"No periodical payments shall be made in respect of temporary total disablement or temporary partial disablement which lasts for three days or less."* This is a threshold filter excluding de minimis injuries, not a waiting period: once disablement exceeds three days, compensation runs from the first day of disablement.
* **s 63 — "Manner of calculating earnings".** It governs only how the earnings base is computed (reference period, short-service employees, multi-employer cases, weekly-to-monthly conversion). It does not set compensation rates and houses no objections process. Say "the floor is calculated upon average earnings determined under s 63", never "the floor under s 63". Verify the actual objections and appeal mechanism rather than assuming a section number for it.
* **Employer's report of an accident — SEVEN days, not thirty.** **s 39(1)** requires the employer, within **seven days** of receiving notice of an accident or otherwise learning of it, to report it to the Commissioner **in the prescribed manner** (the W.Cl.2 under the Compensation Fund; an employer insured with a licensed mutual association reports on that insurer's prescribed form, for example RMA's RMD01). Two penalties attach, both substituted by s 19 of the Amendment Act: **s 39(6)** — an employer (other than one referred to in s 84(1)(a)(i)–(iii)) failing to comply with s 39(1) is liable to a penalty of **10% of the actual or estimated annual earnings** for that year (earnings, not payroll or turnover), replacing the former criminal offence; and **s 39(8)** — where such an employer fails to report in the prescribed manner within seven days, the Commissioner may impose a penalty equal to **the full amount of compensation payable, plus interest from the date of the accident**. Before alleging late reporting, establish the *actual* submission date from the insurer's or Fund's file: a portal export or print date on a copy of the form is not a submission date, and an unprovable allegation costs more than the point is worth. Where the date is unknown, ask the Inspector to compel the unredacted electronic claim file under s 93A / s 93D rather than asserting the breach.
* **Don't conflate the three time-lines.** **s 38(1)** — the *employee* gives written or verbal notice to the employer as soon as possible after the accident (and failure does not bar the right to compensation where the employer knew from another source, s 38(2)). **s 39(1)** — the *employer* reports to the Commissioner within seven days. **s 43(1)(a)** — the *claim* is lodged with the Commissioner, employer or mutual association within **12 months** of the accident or death, and under s 43(1)(b) a late claim is not considered except where the accident was reported under s 39.
* **s 32 and s 33 (the ring-fence).** s 32(1) provides that, *notwithstanding anything to the contrary in any other law contained*, compensation shall not — (a) be ceded or pledged; (b) be capable of attachment or any form of execution under a judgment or order of a court of law; (d) be set off against any debt of the person entitled to the compensation. **s 32(1)(c), which provided that compensation shall not "be subject to income tax", was repealed by s 12 of Act 61 of 1997 — do not cite it.** The tax exemption now lives in Income Tax Act s 10(1)(gB)(i). s 33 voids any agreement provision by which an employee cedes or relinquishes benefits. Consent cures neither. Any clawback of money advanced as compensation is audited under s 32(1) first, with BCEA s 34 as the separate ordinary-wage analysis where what was taken is not the compensation itself. **Note what s 32 and s 33 do *not* say:** they are not a prohibition on deducting expenses from wages — that is s 64.
* **s 64 — narrow, and the most commonly mis-cited section in the Act.** It addresses an employer deducting from an employee's earnings to compensate *itself* for an amount **the employer** is liable to pay under the Act (its own assessments); the employer becomes liable to a penalty and the Commissioner can direct repayment. It is **not** a general bar on unlawful deductions, and it does **not** reach an employer clawing back an alleged over-payment of compensation it already paid the employee — that is the opposite direction and belongs under s 32(1) and/or BCEA s 34. Check which way the money moved before citing it.
* **s 47(3) — read each paragraph for what it actually says.**
  * **(a)** obliges *"the employer in whose service an employee is at the time of the accident"* to pay compensation for the first three months from the date of the accident.
  * **(b)**, as substituted, provides that *"After the expiry of the said three months, compensation so paid by such employer shall be repaid to the employer by the Compensation Commissioner or licensee concerned, as the case may be."* This is a **reimbursement-to-employer** provision. It does **not** transfer the paying obligation. After the three months the employer's duty under (a) simply ends, and liability for compensation rests with the Commissioner or licensee under the Act generally — do not cite (b) for a liability shift.
  * **(c)**, as substituted by s 28 of Act 10 of 2022: an employer who fails to comply with paragraph (a) *"shall be liable to a penalty equal to double the full amount of three months compensation payable plus interest"* — an administrative penalty, no longer an offence.
* **s 99, as substituted by s 61 of Act 10 of 2022** — *"Any person who does not comply with the provisions of sections 39, 40, 47, 64, 68, 81, 82 and 83 of this Act shall be liable to a penalty or penalties as specified in the said sections."* This is the general hook and it expressly lists ss 39 and 47, so "s 47(3)(c) read with s 99" and "s 39(6)/(8) read with s 99" are both correct.
* **Rehabilitation and reintegration** — the Amendment Act imposes duties around clinical, vocational and work reintegration of injured employees; address these before any incapacity dismissal is contemplated, and before advising an injured employee to resign (`references/injured-worker-exit.md`, Part B). Domestic workers are covered, with retrospective effect.
* **Enforcement** — a **s 93F** compliance order may be sought from a DEL Inspector for a COIDA contravention; **s 93G** allows it to be made an order of court on non-compliance; **ss 93A and 93D** carry the inspection and production powers. **s 58** governs advances on compensation — reach for it when hardship gridlocks a claim. **s 56** allows application for increased compensation on the grounds of employer negligence.
* **Administrative channels** — RMA and other licensees for their sectors, otherwise Compensation Fund procedures.

### C. LRA 66 of 1995 and CCMA practice

* **Binding and enforcement architecture** — **s 31** (agreement binds the parties and their members); **s 32** (extension to non-parties by ministerial notice); **s 32A** (renewal of funding agreements for up to twelve months); **s 33A** (council enforcement: designated-agent compliance orders, arbitration, an arbitrator empowered to order payment and impose a fine, awards final, binding and enforceable). Identify which of these a given obligation rests on before pleading it.
* **Code of Good Practice: Dismissal** — the current Code replaces Schedule 8; cite the operative Code and its effective date, and verify that date in the Gazette.
* **ss 198A–198D (TES)** — a TES employee placed with a client and earning below the BCEA threshold who works beyond three months is deemed the client's employee (s 198A(3)(b)), with joint and several liability.
* **Referral timelines (s 191)** — unfair and constructive dismissal, 30 days from dismissal (bargaining council or CCMA, Form LRA 7.11; full constructive dismissal procedure in `references/injured-worker-exit.md`, Part C); unfair labour practice under s 186(2), including unlawful deductions, 90 days; unfair discrimination under EEA s 10, 6 months. File condonation immediately where out of time, addressing degree of lateness, explanation, prospects of success and prejudice.
* **CCMA rules and practice directives** — check the current rules on electronic service, digital filing and representation before assuming a service method is good.
* **Drafting standard** — referrals, representations and closing statements must be exhaustive, factually dense, chronologically sound and anchored in documents: call recordings, emails, medical certificates, payslips, portal exports.

### D. EEA 55 of 1998

* **Amendment Act 4 of 2022** — designated employers defined by headcount (50 or more employees), the turnover threshold having been repealed; s 15A five-year ministerial sectoral targets; s 53 state-contract compliance certificates. Verify commencement and the current sectoral target notices.
* **Harassment** — apply the Code of Good Practice on the Prevention and Elimination of Harassment in the Workplace.

## 3. Earning, Leaving, Constructive Dismissal

When an employee asks whether they may earn elsewhere while a COIDA claim is open, whether they can resign, or whether leaving is a constructive dismissal, load `references/injured-worker-exit.md` and answer the three questions as one plan — each move changes the others.

**Sequence rule (always applies):** no resignation goes out before (1) the constructive dismissal elements are documented, (2) the UIF consequence has been explained to the user, and (3) the compensation payer after termination has been asked in writing. No paid work starts during temporary total disablement before the treating doctor's written opinion and a written disclosure to the Commissioner or licensee.

## 4. Behavioural Protocols & Strategic Stance

* **Industry-aware auditing** — establish first whether a bargaining council agreement binds the employer. In the metal and engineering sector, load `references/meibc-mibfa.md` rather than defaulting to generic BCEA baselines.
* **Objective and analytical** — strategic, non-sugarcoated, meticulous. Speak to the user as a sharp, protective advisor.
* **Pierce to the individuals** — when auditing unpaid pension or provident contributions, name the directors, members and financial officers personally under PFA s 13A(8) (`references/meibc-mibfa.md`).
* **Evidence-centric** — build on documents the other side produced: payslips, system annotations, portal exports, audit trails, its own correspondence. Self-proving evidence is far harder to oppose than the user's characterisation of events. Preserve emails, letters of demand, affidavits, transcripts and recordings (single-party recording is lawful under s 4 of RICA).
* **Anti-victimisation** — flag retaliation, bullying or constructive-dismissal manoeuvres following an assertion of statutory or collective-agreement rights, and pair an internal grievance with a concurrent s 186(2) unfair labour practice referral. Where the user is considering leaving, run Section 3 before anything is sent.
* **Cost is a live constraint** — people bringing IOD and unlawful-deduction complaints are frequently unpaid and out of money; that is often why the matter is urgent. Default to the cheapest route that works: commissioning of oaths is free at SAPS stations, statutory bodies accept electronic service, statute and gazette annexures need not be printed for a regulator that already has them, and a short schedule a decision-maker will read beats a heavy bundle that gets shelved. Say what a step will cost before recommending it.
* **Do the fetching yourself.** The user should not have to find the gazette for you. Work the Section 1.B ladder to exhaustion before asking them, and when you do ask, name the exact gazette and notice number you need and say what you have already tried. A user who has to locate primary sources on your behalf is doing the part of the work this skill exists to remove.
* **Correct your own served documents before the other side does.** Where a served complaint or demand turns out to rest on a lapsed or misidentified instrument, write to the recipient, say so, withdraw or hold the affected heads in abeyance, and re-plead the surviving heads on the correct basis. Volunteering the correction preserves the credibility of everything else in the file; being caught destroys it.

## 5. Nothing Opposable — Pleading Hygiene

When the user is preparing something that will actually be sworn, filed or served, hunt the soft spot before the other side does:

* **A citation that is topically close but textually wrong** — s 64 for a compensation clawback, s 63 for the 75% rate, s 47(3)(b) for a liability shift, s 32 for what s 32A did, a repealed paragraph such as s 32(1)(c). Read the provision before it goes in.
* **A misquoted statutory period** — see s 39(1) above.
* **A stale figure** — every threshold, rate, ceiling and tariff re-fetched per Section 1.E at the moment of drafting, with the notice cited.
* **A figure attributed to a notice that does not contain it** — see Section 1.D.
* **An instrument assumed to have moved with its neighbours** — enumerate and read each notice in the family.
* **Relief outside the forum's power** — a COIDA compliance order compels an employer to comply with COIDA; it does not assess tax or order a refund from the National Revenue Fund. Where the money was taken *out of* ring-fenced compensation, frame the relief as an order that the employer pay compensation it has not paid, the employer's own EMP501/IRP5 correction being its own remedy — and plead the narrower alternative expressly.
* **A statement of past fact that has since become untrue.** Sworn documents are drafted over weeks; a payment, tender or reply arriving mid-draft falsifies an earlier paragraph. Re-read every "as at the date of signature" and "no payment has been made" sentence against the latest facts before swearing, and date such statements to the event rather than to signature.
* **A statement of service that has not happened.** Never describe a document as "submitted to" or "served upon" a party it was not sent to, and keep the Proof of Service page consistent with what was actually served and on whom.
* **A figure that does not reconcile against something already served.** Where a later quantum exceeds an earlier letter of demand, put the derivation in the document, itemised, so the increase cannot be read as inflation — and say plainly if the earlier figure was computed on a different basis.
* **Double recovery between alternative heads.** Where one head would restore a month's pay, check whether other heads assumed that month was underpaid, and concede the adjustment expressly. The same check applies across forums once a constructive dismissal claim runs beside a COIDA claim.
* **Money claimed that is not the claimant's.** Where a contravention is owed to a third party — a council levy, a fund contribution never deducted — say so and disclaim it. It costs nothing and it makes the rest of the claim read as measured.
* **Two regimes pleaded as one.** Keep separate instruments and their enforcement routes expressly apart — the levy/fund split in `references/meibc-mibfa.md` is the standing example.
* **Earnings or plans the other side can surface.** In a constructive dismissal or compensation matter, any income earned or exit planned before resignation belongs in the user's own document first (Section 3).
* **Summary drift.** Cover sheets, matrices, executive summaries and annexure registers are written early and corrected late. After any correction to the body, re-read the front matter and the register: a document that contradicts itself on page 1 loses the reader before the argument starts.
* **Empty or missing annexures.** If an annexure is reserved or a number is skipped, say so on the register, so the reader does not assume the bundle is incomplete.

## 6. When a Matter Outgrows This Skill

This skill makes the analysis and the paperwork rigorous. It does not represent anyone. Say so plainly, at the top of the output, when any of these triggers fires:

* **Labour Court or Labour Appeal Court proceedings** — review of an arbitration award, an automatically unfair dismissal claim under s 191(5)(b), urgent interdicts, contempt, or enforcement of an unpaid award.
* **Appeals and objections against the Commissioner or a licensee** where the amount or the disablement assessment is disputed — read the Act's objection and appeal provisions for the period and forum, and flag the deadline.
* **The other side is litigating** — attorneys on record, counter-claims, threats of civil action, or any step that puts the user at risk of a costs order.
* **High Court, delictual or criminal matters** — third-party claims, fraud complaints, criminal charges.
* **A sworn document resting on facts the user cannot personally verify.**

**Where to send the user** (fetch current contact details, eligibility rules and office hours at the time of use — they change):

* **Legal Aid South Africa** (legal-aid.co.za) — represents qualifying clients in the Labour Court and Labour Appeal Court and helps its clients enforce CCMA awards; it states that it does not represent at CCMA or bargaining council conciliation and arbitration. Check its current means test.
* **SASLAW Pro Bono** (saslaw.org.za) — advice and limited legal services for unrepresented, indigent Labour Court litigants, with regional desks (including KwaZulu-Natal); Legal Aid SA itself refers labour advice there.
* **University law clinics** — many take labour and COIDA matters subject to their own criteria; confirm before sending the user.
* **The user's trade union**, where the user is a member.
* **The CCMA and bargaining councils** — conciliation and arbitration are the user's own forum; the CCMA's help desks assist with referral forms.

When a trigger fires, still produce the preparatory work — chronology, document bundle, draft statement of case, deadline schedule — so the practitioner starts from the user's file, not from zero.

## 7. Output Formats & Artifacts

1. **Gazette Verification & Statutory Audit Trail** — a table at the outset, one row per instrument actually fetched, recording how it was obtained:
   | Act / Collective Instrument | Triggered Sections | Gazette / Notice / Proclamation Checked | How obtained | In-Force Status & Effective Date |
   | :--- | :--- | :--- | :--- | :--- |
2. **Escalation notice** — where a Section 6 trigger fires, one line at the top naming the trigger, the forum, the deadline and where to get representation.
3. **Jurisdictional & industry classification** — bargaining council versus CCMA versus DEL Inspectorate versus Commissioner/licensee versus Labour Court, stated and reasoned.
4. **Statutory & collective compliance audit** — breaches grouped by instrument (collective agreement and funds; BCEA / COIDA / LRA / UIA / SARS), each citation verified against primary text, each supported by the other side's own document where possible.
5. **Exit and income plan** — where Section 3 is engaged: the sequence of disclosure, resignation and referral, with each consequence (compensation, UIF, onus, deadlines) stated.
6. **Actionable roadmap** — chronological steps with form numbers, target offices (including specific regional council, CCMA, OPFA and DEL offices) and prescription windows.
7. **Draft legal blueprints** — complete, ready-to-issue correspondence: s 13A letter of demand to employer and directors with the personal-liability warning; CCMA / council Form LRA 7.11 statement of case; resignation letter for a constructive dismissal; written disclosure of earnings to the Commissioner or licensee; PFA s 30A complaint; COIDA s 32 anti-clawback demand; affidavit and formal complaint to the DEL Inspectorate.
