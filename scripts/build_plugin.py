#!/usr/bin/env python3
"""Build dist/<name>.plugin: a zip of the plugin manifest, README, LICENSE and
every file under skills/, so reference files ship with the skill. Also builds
dist/<skill>.skill for each skill folder (the folder zipped with its files,
the format a Claude "Save skill" upload takes).

Fails if a SKILL.md points at a references/ file that is not in its skill folder.
"""
import json
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]

    missing = []
    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        for ref in sorted(set(re.findall(r"references/[\w.-]+\.md", skill_md.read_text(encoding="utf-8")))):
            if not (skill_md.parent / ref).is_file():
                missing.append(f"{skill_md.relative_to(ROOT)} -> {ref}")
    if missing:
        print("Referenced files missing from the skill folder:", *missing, sep="\n  ")
        return 1

    files = [ROOT / ".claude-plugin" / "plugin.json", ROOT / "LICENSE", ROOT / "README.md"]
    files += sorted(p for p in (ROOT / "skills").rglob("*") if p.is_file())

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / f"{name}.plugin"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        dirs = sorted({d.as_posix() + "/" for f in files for d in f.relative_to(ROOT).parents if d.as_posix() != "."})
        for d in dirs:
            zf.writestr(d, "")
        for f in files:
            zf.write(f, f.relative_to(ROOT).as_posix())

    print(f"Built {out.relative_to(ROOT)} ({name} {version}):")
    for info in zipfile.ZipFile(out).infolist():
        print(f"  {info.file_size:>8}  {info.filename}")

    for skill_dir in sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md")):
        skill_out = dist / f"{skill_dir.name}.skill"
        with zipfile.ZipFile(skill_out, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in sorted(p for p in skill_dir.rglob("*") if p.is_file()):
                zf.write(f, f.relative_to(skill_dir.parent).as_posix())
        print(f"Built {skill_out.relative_to(ROOT)}:")
        for info in zipfile.ZipFile(skill_out).infolist():
            print(f"  {info.file_size:>8}  {info.filename}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
