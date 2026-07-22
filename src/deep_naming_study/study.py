from __future__ import annotations
import json
from pathlib import Path

REQUIRED = ["project", "purpose", "audience", "voice", "source_inspiration", "mechanism", "dead_lanes", "rubric"]
STAGES = ["01-source-notes", "02-theory-passes", "03-merged-slate", "04-blind-critics", "05-collisions", "06-simulations", "07-synthesis"]


def validate_brief(brief: dict) -> list[str]:
    errors = [f"missing brief field: {key}" for key in REQUIRED if not brief.get(key)]
    if not isinstance(brief.get("rubric", []), list) or len(brief.get("rubric", [])) < 3:
        errors.append("rubric must contain at least three criteria")
    if not isinstance(brief.get("dead_lanes", []), list):
        errors.append("dead_lanes must be a list")
    return errors


def scaffold_study(brief: dict, destination: str | Path) -> Path:
    errors = validate_brief(brief)
    if errors:
        raise ValueError("; ".join(errors))
    root = Path(destination)
    root.mkdir(parents=True, exist_ok=False)
    (root / "brief.json").write_text(json.dumps(brief, indent=2) + "\n")
    for stage in STAGES:
        (root / stage).mkdir()
    templates = {
        "01-source-notes/README.md": "# Source notes\n\nRecord primary language, mandate, tensions, and citations.\n",
        "02-theory-passes/README.md": "# Independent theory passes\n\nOne file per theory. Do not expose prior favorites.\n",
        "03-merged-slate/slate.md": "# Merged slate\n\nTrack each candidate and its theory. Do not count votes.\n",
        "04-blind-critics/README.md": "# Blind critics\n\nGive critics the brief and slate without domains or prior rankings.\n",
        "05-collisions/README.md": "# Collisions\n\nCheck exact phrases, phonetics, associations, then domains.\n",
        "06-simulations/template.md": "# Candidate simulation\n\n## Five issue titles\n\n## Descriptor\n\n## About paragraph\n\n## Masthead\n\n## Spoken introduction\n",
        "07-synthesis/final.md": "# Final synthesis\n\n## Judgment: solved | close | wrong field\n\n## Recovered mechanism\n\n## Leads\n\n## Killed lanes\n\n## Next test\n",
    }
    for rel, content in templates.items():
        (root / rel).write_text(content)
    return root


def validate_study(root: str | Path) -> list[str]:
    root = Path(root)
    errors: list[str] = []
    brief_path = root / "brief.json"
    if not brief_path.is_file():
        errors.append("missing brief.json")
    else:
        try:
            errors.extend(validate_brief(json.loads(brief_path.read_text())))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid brief.json: {exc}")
    for stage in STAGES:
        if not (root / stage).is_dir():
            errors.append(f"missing stage directory: {stage}")
    return errors
