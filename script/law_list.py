#!/usr/bin/python3
"""
This law generates a list of laws.
"""

import json
import os


def rv_badge():
    return (
        "***\n\n\n|||\n|---|---|\n|![](/img/rvgovtseal2.webp)|"
        + "<h2>Rainychville Government</h2> |\n"
    )


def raw_text_url(path):
    return f"https://raw.githubusercontent.com/rainychville/tos/main/{path}"


def project_root():
    """Return project root directory (relative to actual root)"""
    return os.path.dirname(os.path.realpath(__file__))


def main():
    data = json.loads(open("laws.json", "r", encoding="UTF-8").read())

    buffer = (
        "# Laws of Rainychville\n"
        + "This is an automatically generated list of laws. ([Back](README.md))\n\n"
        + "| Law identifier | Name | Format | Status | Raw |\n"
        + "|----------------|------|--------|--------|-----|\n"
        ""
    )

    buffer += """""".join(
        f"|{law.get('id')}|[{law.get('name')}](/{law.get('path')})|"
        + f"{law.get('format')}|{law.get('status')}"
        + f"|[raw]({raw_text_url(law.get('path'))})|\n"
        for law in data
    )

    buffer += rv_badge()

    print(buffer)


if __name__ == "__main__":
    main()
