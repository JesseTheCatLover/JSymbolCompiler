# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.field_symbol import FieldSymbol
from jsymbolcompiler.models.base import Location

from .utils import get_text, get_visibility_for_member, get_brief_description, get_detailed_description, detect_module, \
    is_deprecated, extract_docs


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

        qualified_name = get_text(
            member,
            "qualifiedname"
        )

        symbol.id = qualified_name

        symbol.owner = qualified_name.rsplit(
            "::",
            1
        )[0]

        location = member.find("location")

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        symbol.module = detect_module(symbol.location.file)

        symbol.visibility = get_visibility_for_member(member)
        symbol.summary = get_brief_description(member)
        symbol.detail = get_detailed_description(member)

        symbol.deprecated = is_deprecated(extract_docs(member))

        return symbol