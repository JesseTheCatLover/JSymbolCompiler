# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import xml.etree.ElementTree as ET

from src.compiler.builders.class_builder import ClassBuilder
from src.compiler.builders.enum_builder import EnumBuilder
from src.compiler.builders.field_builder import FieldBuilder
from src.compiler.builders.file_builder import FileBuilder
from src.compiler.builders.function_builder import FunctionBuilder


class SymbolBuilder:

    def __init__(self):

        self.class_builder = ClassBuilder()
        self.file_builder = FileBuilder()

        self.function_builder = FunctionBuilder()
        self.field_builder = FieldBuilder()
        self.enum_builder = EnumBuilder()

    def build(self, xml_file):

        tree = ET.parse(xml_file)
        root = tree.getroot()

        compound = root.find("compounddef")

        if compound is None:
            return []

        symbols = []

        compound_kind = compound.attrib.get("kind")

        if compound_kind == "file":
            symbols.extend(
                self.file_builder.build(compound)
            )

        elif compound_kind in ["class", "struct"]:
            symbols.extend(
                self.class_builder.build(compound)
            )

        for member in compound.findall(".//memberdef"):

            member_kind = member.attrib.get("kind")

            if member_kind == "function":

                symbols.append(
                    self.function_builder.build(member)
                )

            elif member_kind == "variable":

                symbols.append(
                    self.field_builder.build(member)
                )

            elif member_kind == "enum":

                symbols.append(
                    self.enum_builder.build(member)
                )

        return symbols