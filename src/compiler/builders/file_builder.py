# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from models.file_symbol import FileSymbol
from models.base import Location

from .utils import get_text

class FileBuilder:

    def build(self, compound):

        location = compound.find("location")

        symbol = FileSymbol(
            id=compound.attrib.get("id", ""),
            name=get_text(compound, "compoundname"),
            kind="file",
            module=""
        )

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        for include in compound.findall("includes"):
            symbol.includes.append(include.text or "")

        for include in compound.findall("includedby"):
            symbol.includedBy.append(include.text or "")

        return [symbol]