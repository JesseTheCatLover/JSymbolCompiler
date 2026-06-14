# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

import argparse

from jsymbolcompiler.compiler.doxygen_runner import DoxygenRunner
from jsymbolcompiler.compiler.doxygen_loader import DoxygenLoader
from jsymbolcompiler.compiler.builder import SymbolBuilder
from jsymbolcompiler.compiler.resolver import SymbolResolver
from jsymbolcompiler.config.metadata import BuildMetadata
from jsymbolcompiler.config.version_detector import VersionDetector
from jsymbolcompiler.exporters.json_exporter import JsonExporter

def main(engine_root: str, output_dir: str):

    xml_dir = DoxygenRunner().run(
        engine_root=engine_root,
        output_dir=output_dir
    )

    loader = DoxygenLoader(xml_dir)
    builder = SymbolBuilder()
    resolver = SymbolResolver()
    exporter = JsonExporter()

    symbols = []

    context = VersionDetector().detect(engine_root)

    print(
        f"[JSymbolCompiler]: "
        f"Engine={context.engineVersion} "
        f"Docs={context.documentationVersion}"
    )

    for xml_file in loader.load_files():
        symbols.extend(builder.build(xml_file))

    symbols = resolver.link(symbols)

    metadata = BuildMetadata(
        engineVersion=context.engineVersion,
        documentationVersion=context.documentationVersion,
        symbolCount=len(symbols)
    )

    exporter.export(
        symbols,
        f"{output_dir}/{context.documentationVersion}/symbols",
        metadata
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--engine-root",
        required=True,
        help="Path to RedleafEngine repository"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output artifact directory"
    )

    args = parser.parse_args()

    main(
        args.engine_root,
        args.output
    )