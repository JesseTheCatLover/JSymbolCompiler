# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from pathlib import Path


class DoxygenRunner:

    def run(self,
            engine_root: str,
            output_dir: str) -> str:

        xml_dir = Path(output_dir) / "xml"

        xml_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        return str(xml_dir)