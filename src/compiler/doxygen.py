#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.


from pathlib import Path

class DoxygenLoader:
    def __init__(self, xml_dir: str):
        self.xml_dir = Path(xml_dir)

    def load_files(self):
        return list(self.xml_dir.glob("*.xml"))