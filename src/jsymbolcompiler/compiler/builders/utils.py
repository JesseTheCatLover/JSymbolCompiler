# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

from pathlib import Path

def get_text(node, tag, default=""):
    child = node.find(tag)

    if child is None:
        return default

    return "".join(child.itertext()).strip()


def get_location(node):
    location = node.find("location")

    if location is None:
        return None

    return {
        "file": location.attrib.get("file", ""),
        "line": int(location.attrib.get("line", -1))
    }


def get_visibility_for_member(member):
    return member.attrib.get("prot", "public")

def get_brief_description(node):

    brief = node.find("briefdescription")

    if brief is None:
        return ""

    return "".join(brief.itertext()).strip()

def get_detailed_description(node):

    detail = node.find("detaileddescription")

    if detail is None:
        return ""

    return "".join(detail.itertext()).strip()

def detect_module(file_path: str) -> str:

    parts = Path(file_path).parts

    try:
        source_index = parts.index("Source")

        return parts[source_index + 1]

    except (ValueError, IndexError):
        return ""

def is_deprecated(text: str) -> bool:
    return "deprecated" in text.lower()

def extract_docs(node):

    summary = "".join(
        node.findtext("briefdescription", default="")
    ).strip()

    detail = "".join(
        node.findtext("detaileddescription", default="")
    ).strip()

    return summary + detail

def normalize_type(type_name: str):

    return (
        type_name
        .replace(" &", "&")
        .replace(" *", "*")
        .strip()
    )

def detect_visibility(file_path: str) -> str:

    parts = Path(file_path).parts

    if "Public" in parts:
        return "public"

    if "Private" in parts:
        return "private"

    return "public"