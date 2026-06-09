# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from jsymbolcompiler.models.class_symbol import ClassSymbol
from jsymbolcompiler.models.base import Location

from .utils import get_text


class ClassBuilder:

    def build(self, compound):

        symbol = ClassSymbol(
            id=compound.attrib.get("id", ""),
            name=get_text(compound, "compoundname"),
            kind="class",
            module=""
        )

        location = compound.find("location")

        if location is not None:
            symbol.location = Location(
                file=location.attrib.get("file", ""),
                line=int(location.attrib.get("line", -1))
            )

        for base in compound.findall("basecompoundref"):
            symbol.bases.append("".join(base.itertext()).strip())

        for member in compound.findall(".//memberdef"):

            member_kind = member.attrib.get("kind")

            if member_kind == "variable":
                symbol.fields.append(
                    get_text(member, "name")
                )

            elif member_kind == "function":
                symbol.methods.append(
                    get_text(member, "name")
                )

        return [symbol]