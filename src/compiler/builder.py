#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import xml.etree.ElementTree as ET

class SymbolBuilder:

    def build(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        symbols = []

        for compound in root.findall("compounddef"):
            kind = compound.attrib.get("kind")

            if kind == "class":
                symbols.append(self._build_class(compound))

            elif kind == "function":
                symbols.append(self._build_function(compound))

        return symbols