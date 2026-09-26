# ZA Labour Law Advisor

A Claude skill for navigating South African statutory labour disputes: workplace injury (IOD/COIDA) claims, unlawful wage deductions or clawbacks, CCMA and bargaining council referrals, PAYE/UIF payroll disputes, and drafting the correspondence that goes with them (letters of demand, affidavits, formal complaints).

## What it does

The skill loads whenever a conversation touches South African labour law — even if the user doesn't name the specific Act. It cross-references:

- **BCEA / NMWA** — deductions and clawbacks, working hours, termination entitlements, minimum wage
- **COIDA** (as amended by Act 10 of 2022) — injury-on-duty compensation, employer obligations, unlawful clawbacks, penalties, enforcement channels
- **LRA / CCMA** — jurisdiction, forms, referral timelines, and the full constructive dismissal procedure
- **UIA** — what an injured worker keeps or loses by resigning, including UIF unemployment benefits
- **SARS / UIF** — PAYE and UIF misclassification, statutory tax exemptions on injury compensation
- **MEIBC / MIBFA** — bargaining council extension notices, levies, benefit funds and Pension Funds Act s 13A, for the metal and engineering sector

It also answers the three questions an injured worker asks once a claim stalls — can I earn elsewhere, can I leave, and is leaving a constructive dismissal — as one plan, and tells the user plainly when a matter needs a practitioner (Legal Aid SA, SASLAW Pro Bono, law clinics).

It's built around a verification discipline: statutory section numbers are easy to cite confidently and wrongly, so the skill instructs Claude to check every citation against primary text before it goes into anything a person will actually sign or serve — and it documents several specific, easy-to-make citation mistakes (e.g. COIDA Section 63 vs. Section 47(1)(a)/Schedule 4, Section 64's narrow scope) so they aren't repeated.

## Who it's for

Anyone dealing with a South African employer dispute who wants Claude to reason like a specialist advisor rather than a generalist — strategic, document-focused, and willing to flag the weak point in your own filing before an opposing attorney does.

## Installing

Download `za-labour-law-advisor.plugin` from the [latest release](https://github.com/drryltrnr/za-labour-law-advisor/releases/latest) and install it in Claude Cowork or Claude Code. Once installed, the skill activates automatically when a conversation matches its domain — no slash command needed.

## Disclaimer

This skill provides legal information and drafting assistance, not legal advice from a qualified attorney. Statutory references should always be independently verified, and users with high-stakes matters should consult a South African labour law attorney.

## License

MIT
