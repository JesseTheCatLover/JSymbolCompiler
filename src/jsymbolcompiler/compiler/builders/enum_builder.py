# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.enum_symbol import EnumSymbol
from jsymbolcompiler.models.base import Location

from .utils import get_text, get_visibility, get_brief_description, get_detailed_description, detect_module, \
    is_deprecated, extract_docs, detect_visibility


class EnumBuilder:

    def build(self, member):

        symbol = EnumSymbol(
            id=member.attrib.get("id", ""),
            name=get_text(member, "name"),
            kind="enum",
            module=""
        )

        symbol.id = symbol.name

        location = member.find("location")


        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        symbol.module = detect_module(symbol.location.file)

        symbol.visibility = detect_visibility(symbol.location.file)
        symbol.summary = get_brief_description(member)
        symbol.detail = get_detailed_description(member)

        symbol.deprecated = is_deprecated(extract_docs(member))

        for value in member.findall("enumvalue"):
            symbol.values.append(
                get_text(value, "name")
            )

        return symbol