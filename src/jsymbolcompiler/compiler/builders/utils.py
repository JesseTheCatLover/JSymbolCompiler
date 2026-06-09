# Copyright 2025-2026 JesseTheCatLover. All Rights Reserved.

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


def get_visibility(member):
    return member.attrib.get("prot", "public")