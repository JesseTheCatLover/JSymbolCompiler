# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.function_symbol import FunctionSymbol
from jsymbolcompiler.models.function_symbol import Param
from jsymbolcompiler.models.base import Location

from .utils import get_text


class FunctionBuilder:

    def build(self, member):

        symbol = FunctionSymbol(
            id=member.attrib.get("id", ""),
            name=get_text(member, "name"),
            kind="function",
            module=""
        )

        symbol.qualifiedName = get_text(
            member,
            "qualifiedname"
        )

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

        for param in member.findall("param"):

            symbol.params.append(
                Param(
                    name=get_text(param, "declname"),
                    type=get_text(param, "type")
                )
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