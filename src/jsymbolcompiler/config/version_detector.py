#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import re
from pathlib import Path

from jsymbolcompiler.config.build_context import BuildContext


class VersionDetector:

    def detect(self, engine_root: str) -> BuildContext:

        cmake_file = (
            Path(engine_root)
            / "CMakeLists.txt"
        )

        text = cmake_file.read_text()

        engine_version = "0.0.0"
        documentation_version = "v1"

        match = re.search(
            r"REDLEAF_DOC_VERSION\s+\"([^\"]+)\"",
            text
        )

        if match:
            documentation_version = match.group(1)

        match = re.search(
            r"project\s*\(.*?VERSION\s+([0-9]+(?:\.[0-9]+){1,3})",
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            engine_version = match.group(1)

        return BuildContext(
            engineVersion=engine_version,
            documentationVersion=documentation_version
        )