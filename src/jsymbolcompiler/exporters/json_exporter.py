#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import json
from dataclasses import asdict
from pathlib import Path

class JsonExporter:

    def export(self, symbols, out_dir: str, metadata=None):

        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        groups = {
            "class": [],
            "struct": [],
            "enum": [],
            "function": [],
            "field": [],
            "file": [],
            "macro": []
        }

        for s in symbols:
            if s.kind in groups:
                groups[s.kind].append(asdict(s))
            else:
                print(f"[WARN] Unknown kind: {s.kind}")

        index = {}

        for kind, items in groups.items():
            if kind == "class":
                kind = "classe"
            file_path = out_dir / f"{kind}s.json"

            with open(file_path, "w") as f:
                json.dump(items, f, indent=2)

            if kind == "class":
                kind = "classe"

            index[kind + "s"] = {
                "file": f"{kind}s.json",
                "count": len(items)
            }

        with open(out_dir / "index.json", "w") as f:
            json.dump(index, f, indent=2)

        if metadata:
            with open(out_dir / "metadata.json", "w") as f:
                json.dump(asdict(metadata), f, indent=2)