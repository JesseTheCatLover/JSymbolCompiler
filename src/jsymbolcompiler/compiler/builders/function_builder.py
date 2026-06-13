# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.function_symbol import FunctionSymbol
from jsymbolcompiler.models.function_symbol import Param
from jsymbolcompiler.models.base import Location

from .utils import get_text, get_visibility, get_brief_description, get_detailed_description, detect_module, \
    is_deprecated, extract_docs, normalize_type


class FunctionBuilder:

    def build(self, member):

        symbol = FunctionSymbol(
            id=member.attrib.get("id", ""),
            name=get_text(member, "name"),
            kind="function",
            module=""
        )

        qualified_name = get_text(
            member,
            "qualifiedname"
        )

        if qualified_name:
            symbol.qualifiedName = qualified_name

            if "::" in qualified_name:
                symbol.owner = qualified_name.rsplit(
                    "::",
                    1
                )[0]

        else:
            symbol.qualifiedName = symbol.name

        symbol.returnType = get_text(
            member,
            "type"
        )

        location = member.find("location")

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("bodyfile",
                                         location.attrib.get("file", "")),
                line=int(location.attrib.get("bodystart",
                                             location.attrib.get("line", -1)))
            )

        symbol.module = detect_module(symbol.location.file)
        symbol.visibility = get_visibility(member)
        symbol.summary = get_brief_description(member)
        symbol.detail = get_detailed_description(member)

        symbol.deprecated = is_deprecated(extract_docs(member))

        for param in member.findall("param"):
            symbol.params.append(
                Param(
                    name=get_text(param, "declname"),
                    type=get_text(param, "type")
                )
            )

        param_types = ",".join(
            normalize_type(param.type)
            for param in symbol.params
        )

        symbol.id = (
            f"{symbol.qualifiedName}"
            f"({param_types})"
        )

        for ref in member.findall("references"):
            symbol.calls.append(
                "".join(ref.itertext()).strip()
            )

        for ref in member.findall("referencedby"):
            symbol.calledBy.append(
                "".join(ref.itertext()).strip()
            )

        return symbol