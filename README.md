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

The core `SKILL.md` holds the method — the working sequence, the verification rules, the traps carried into every matter, escalation and output formats — in about 5,000 words, roughly 60% lighter than v0.3.1. The statute-by-statute detail lives in `skills/za-labour-law-advisor/references/` and is loaded only when a matter triggers it:

| File | Covers |
| :--- | :--- |
| `gazette-verification.md` | Search patterns, where to read primary text, citation format, the fetch table for volatile figures |
| `bcea-nmwa.md` | Hours, pay, deductions and clawbacks, s 34A fund remittance, leave, termination, money-claim forums, minimum wage |
| `coida.md` | COIDA as amended by Act 10 of 2022 and its 2026 commencement and regulations |
| `lra-ccma.md` | Dismissal, retrenchment, unfair labour practices, referrals, awards, review, TES |
| `eea.md` | Discrimination, equal pay, harassment |
| `meibc-mibfa.md` | MEIBC sector module, MIBFA funds, Pension Funds Act s 13A |
| `sars-paye-uif.md` | PAYE, UIF, SARS channels |
| `prescription.md` | When money claims prescribe and what interrupts them |
| `leaving-employment.md` | Stay, resign or claim constructive dismissal; earning during a COIDA claim |
| `pleading-hygiene.md` | Checks for anything signed, sworn, filed or served |
| `watch-list.md` | Items that change on known dates, and points not yet confirmed against primary text |

They are part of the skill: the package must contain the whole skill folder (see Installing). `evals/evals.json` holds test prompts with known answers for checking the skill after an edit; it is not packaged.

It also plans a worker's exit — stay, resign, or claim constructive dismissal — with each consequence for UIF, the onus of proof and any open claim, and tells the user plainly when a matter needs a practitioner (Legal Aid SA, SASLAW Pro Bono, law clinics).

It's built around a verification discipline: statutory section numbers are easy to cite confidently and wrongly, so the skill instructs Claude to check every citation against primary text before it goes into anything a person will actually sign or serve — and it documents specific, easy-to-make citation mistakes (e.g. COIDA s 63 vs s 47(1)(a)/Schedule 4, the repealed UIA ss 38–41, an unlawful deduction pleaded as an unfair labour practice) so they aren't repeated.

## Who it's for

Any worker dealing with a South African employer dispute who wants Claude to reason like a specialist advisor rather than a generalist — strategic, document-focused, and willing to flag the weak point in your own filing before an opposing attorney does.

## Installing

Plugins need a paid Claude plan. Once installed, the skill activates automatically when a conversation matches its domain — no slash command needed.

**Recommended: add this repo as a marketplace.** You get updates as they are pushed.

- **Claude Cowork / claude.ai:** open **Customize → Plugins → Add → Add marketplace → Add from a repository**, enter `drryltrnr/za-labour-law-advisor`, then install **za-labour-law-advisor**. Turn on **Sync automatically** to receive updates.
- **Claude Code:**

  ```
  /plugin marketplace add drryltrnr/za-labour-law-advisor
  /plugin install za-labour-law-advisor@drryltrnr
  ```

**Alternative: install from a file.** Download `za-labour-law-advisor.plugin` from the [latest release](https://github.com/drryltrnr/za-labour-law-advisor/releases/latest) and upload it under **Customize → Plugins** in Claude Cowork, or install it in Claude Code. A file install does not update itself; download the next release to upgrade.

If you previously saved this as a standalone skill (the `.skill` package), turn that skill off after installing the plugin so the two copies don't compete.

To build the packages yourself, run `python3 scripts/build_plugin.py`. It writes `dist/za-labour-law-advisor.plugin` (manifest, README, LICENSE and every file under `skills/`) and `dist/za-labour-law-advisor.skill` (the skill folder alone — `SKILL.md` plus `references/` — for a Claude **Save skill** upload), and refuses to build if `SKILL.md` points to a reference file that is missing.

Releases are published by `.github/workflows/release.yml`, which builds both packages and attaches them to a GitHub release. Run it from the Actions tab with the tag (e.g. `v0.3.0`) to create that tag at the commit it runs on, or push a `v*` tag. The notes come from `release-notes/<tag>.md` if it exists, else the tag message. The tag must match the version in `.claude-plugin/plugin.json`, and an existing tag must point at the commit the workflow runs on.

## Disclaimer

This skill provides legal information and drafting assistance, not legal advice from a qualified attorney. Statutory references should always be independently verified, and users with high-stakes matters should consult a South African labour law attorney.

## License

MIT
