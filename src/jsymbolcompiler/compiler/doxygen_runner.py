# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import subprocess
from pathlib import Path

class DoxygenRunner:
    def _generate_doxyfile(
            self,
            engine_root: str,
            output_dir: Path
    ):
        template_path = (
                Path(__file__).parent.parent.parent.parent
                / "templates"
                / "Doxyfile.in"
        )

        text = template_path.read_text()

        text = text.replace(
            "@ENGINE_ROOT@",
            engine_root
        )

        text = text.replace(
            "@OUTPUT_DIR@",
            str(output_dir)
        )

        (output_dir / "Doxyfile").write_text(text)

    def run(
            self,
            engine_root: str,
            output_dir: str
    ) -> str:

        output_dir = Path(output_dir)

        xml_dir = output_dir / "xml"

        xml_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self._generate_doxyfile(
            engine_root,
            output_dir
        )

        subprocess.run(
            [
                "doxygen",
                str(output_dir / "Doxyfile")
            ],
            check=True
        )

        return str(xml_dir)