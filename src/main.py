#  Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from compiler.doxygen import DoxygenLoader
from compiler.builder import SymbolBuilder
from compiler.resolver import SymbolResolver
from exporters.json_exporter import JsonExporter
import argparse

def main(xml, out):

    loader = DoxygenLoader(xml)
    builder = SymbolBuilder()
    resolver = SymbolResolver()
    exporter = JsonExporter()

    all_symbols = []

    for file in loader.load_files():
        all_symbols += builder.build(file)

    all_symbols = resolver.link(all_symbols)

    exporter.export(all_symbols, out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--xml", required=True)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()

    main(args.xml, args.out)