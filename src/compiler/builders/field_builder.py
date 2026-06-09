# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from models.field_symbol import FieldSymbol
from models.base import Location

from .utils import get_text


class FieldBuilder:

    def build(self, member):

        symbol = FieldSymbol(
            id=member.attrib.get("id", ""),
            name=get_text(member, "name"),
            kind="field",
            module=""
        )

        symbol.type = get_text(
            member,
            "type"
        )

        symbol.owner = get_text(
            member,
            "qualifiedname"
        )

        location = member.find("location")

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        return symbol