#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from dataclasses import dataclass

@dataclass
class BuildMetadata:
    engineVersion: str
    documentationVersion: str
    symbolCount: int