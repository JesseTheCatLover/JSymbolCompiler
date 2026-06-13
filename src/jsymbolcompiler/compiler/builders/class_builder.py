# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.class_symbol import ClassSymbol
from jsymbolcompiler.models.base import Location

from .utils import get_text, get_visibility, get_brief_description, get_detailed_description, detect_module, \
    is_deprecated, extract_docs, detect_visibility


class ClassBuilder:

    def build(self, compound, kind):

        symbol = ClassSymbol(
            id=compound.attrib.get("id", ""),
            name=get_text(compound, "compoundname"),
            kind=kind,
            module=""
        )

        symbol.id = get_text(compound,"compoundname")
        location = compound.find("location")

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        symbol.visibility = detect_visibility(symbol.location.file)
        symbol.module = detect_module(symbol.location.file)

        symbol.summary = get_brief_description(compound)
        symbol.detail = get_detailed_description(compound)

        symbol.deprecated = is_deprecated(extract_docs(compound))

        for base in compound.findall("basecompoundref"):

            if base.text:
                symbol.bases.append(base.text.strip())

        for member in compound.findall(".//memberdef"):

            member_kind = member.attrib.get("kind")

            if member_kind == "variable":
                symbol.fields.append(get_text(member, "name"))

            elif member_kind == "function":

                qualified_name = get_text(member,"qualifiedname")

                symbol.methods.append(qualified_name)

        return [symbol]