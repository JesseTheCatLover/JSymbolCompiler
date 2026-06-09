# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.enum_symbol import EnumSymbol
from jsymbolcompiler.models.base import Location

from .utils import get_text


class EnumBuilder:

    def build(self, member):

        symbol = EnumSymbol(
            id=member.attrib.get("id", ""),
            name=get_text(member, "name"),
            kind="enum",
            module=""
        )

        location = member.find("location")

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        for value in member.findall("enumvalue"):
            symbol.values.append(
                get_text(value, "name")
            )

        return symbol