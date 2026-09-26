# ZA Labour Law Advisor

A Claude skill for workers in South African employment disputes: dismissals and retrenchments, unfair labour practices, unpaid wages and unlawful deductions, leave and termination pay, discrimination and harassment, workplace injury (IOD/COIDA) claims, UIF and PAYE errors — and the correspondence, referrals and affidavits that go with them.

## What it does

The skill loads whenever a conversation touches South African labour law — even if the user doesn't name the specific Act. It cross-references:

- **BCEA / NMWA** — hours and overtime, leave, pay and payslips, deductions and clawbacks, notice, severance and termination pay, the earnings threshold, which forum hears a money claim, the national minimum wage
- **LRA / CCMA** — what counts as a dismissal, automatically unfair dismissals, the 2025 Code of Good Practice: Dismissal, retrenchment (ss 189 and 189A), unfair labour practices, referral routes and time limits, remedies, and enforcing, rescinding or reviewing awards
- **EEA** — unfair discrimination, equal pay for work of equal value, burden of proof, the harassment code, and where a discrimination dispute goes
- **COIDA** (as amended by Act 10 of 2022) — compensation, employer reporting duties, unlawful clawbacks, penalties, enforcement channels
- **UIA / UIC Act** — benefit entitlements and appeals, and enforcement through the BCEA's inspectorate machinery
- **SARS** — PAYE and UIF payroll errors, the tax exemption on injury compensation, and which SARS channel fits which complaint
- **Prescription Act** — when a money claim prescribes and what interrupts it
- **MEIBC / MIBFA** — sector modules for the metal and engineering industries: bargaining council extension notices, levies, benefit funds and Pension Funds Act s 13A

The MEIBC/MIBFA/Pension Funds Act s 13A detail and the SARS/PAYE/UIF detail live in `skills/za-labour-law-advisor/references/`, loaded only when a matter triggers them, which keeps the core `SKILL.md` about 16% lighter. They are part of the skill: the package must contain the whole skill folder (see Installing).

It also plans a worker's exit — stay, resign, or claim constructive dismissal — with each consequence for UIF, the onus of proof and any open claim, and tells the user plainly when a matter needs a practitioner (Legal Aid SA, SASLAW Pro Bono, law clinics).

It's built around a verification discipline: statutory section numbers are easy to cite confidently and wrongly, so the skill instructs Claude to check every citation against primary text before it goes into anything a person will actually sign or serve — and it documents specific, easy-to-make citation mistakes (e.g. COIDA s 63 vs s 47(1)(a)/Schedule 4, the repealed UIA ss 38–41, an unlawful deduction pleaded as an unfair labour practice) so they aren't repeated.

## Who it's for

Any worker dealing with a South African employer dispute who wants Claude to reason like a specialist advisor rather than a generalist — strategic, document-focused, and willing to flag the weak point in your own filing before an opposing attorney does.

## Installing

Download `za-labour-law-advisor.plugin` from the [latest release](https://github.com/drryltrnr/za-labour-law-advisor/releases/latest) and install it in Claude Cowork or Claude Code. Once installed, the skill activates automatically when a conversation matches its domain — no slash command needed.

To build the package yourself, run `python3 scripts/build_plugin.py`. It writes `dist/za-labour-law-advisor.plugin` containing the manifest, README, LICENSE and every file under `skills/` — `SKILL.md` and its `references/` — and refuses to build if `SKILL.md` points to a reference file that is missing.

## Disclaimer

This skill provides legal information and drafting assistance, not legal advice from a qualified attorney. Statutory references should always be independently verified, and users with high-stakes matters should consult a South African labour law attorney.

## License

MIT
