#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import json
from dataclasses import asdict

class JsonExporter:

    def export(self, symbols, out_path):
        data = [asdict(s) for s in symbols]

        with open(out_path, "w") as f:
            json.dump(data, f, indent=2)