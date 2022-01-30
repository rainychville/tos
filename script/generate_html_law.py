"""
This is a Python script to generate HTML documents containing the
full text of Rainychville law.
"""

import json
import os
import argparse as ap
import textwrap as tw
import webbrowser as wb


def law_html(law_name, law_text):
    """Return a HTML document containing full-text of a law."""
    html_js = tw.dedent(
           'window.onload=main();function main(){console.log("Hello there!");'
          +'console.log("Rainychville: https://discord.gg/rainychville");}')
    html_css = tw.dedent(
           "body{background-color: black;} .law {margin: 0px 400px 0px 400px;"
           +"background-color: rgb(255, 228, 156);color: black;padding: 10px;"
           +"outline: solid;} .left-notice{position:fixed;padding:10px;"
           +"background-color: rgb(187, 187, 187);outline: solid;}")
    html = (
    """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Rainychville Law: """+law_name+"""</title>
        <style>"""+html_css+"""</style>
        <meta charset="utf-8">
    </head>

    <body>
        <div class="left-notice">
            <p>Courtesy of RandomFan#3511<br>Rainychville Law Services</p>
            <ul>
                <li><a href="https://discord.gg/rainychville">Rainychville discord server</a></li>
                <li><a href="https://github.com/rainychville/tos">Rainychville law (GitHub repository)</a></li>
            </ul>
        </div>
        <div class="law">
            <h1>"""+law_name+"""</h1>
            <div class="law-text">
                <pre>\n\n"""+law_text+"""\n\n
                </pre>
            </div>

            <p>
                This is an automatically generated document.<br><br>
            </p>
            <div class="disclaimer">
                <h4>Disclaimer</h4>
                <p>This is not a real law. This document is distributed solely for the purposes of parody. RandomFan#3511
                    Rainychville Law Services is a completely <b>FICTIONAL</b> organization. The author of this parody
                    "law", RandomFan#3511 does not practice law.</p>
            </div>
            <div class="scripting">
            <script type="text/javascript">"""+html_js+"""</script>
            </div>
        </div>
    </body>
    </html>
    """
    )

    return tw.dedent(html)


def projdir():
    """Return directory where this script has been placed."""
    return os.path.realpath(os.path.realpath(__file__))


def dirclean(path):
    """dc: Directory path cleaner.

    This script uses the Unix directory separator (`/`).

    If this script is being run on Windows, this returns
    a path with the Unix directory separator (`/`) replaced
    with the Windows directory separator (`\\`)."""
    return path.replace("/", os.path.sep)


def main(args):
    """Main function."""

    out_folder = args.output

    if out_folder in os.listdir():
        print(
            tw.dedent(f"""
        Warning: "{out_folder}" directory already exists."""))

    law_json_path = "laws.json"

    if "laws.json" in os.listdir():
        law_json_path = "laws.json"
    else:
        law_json_path = dirclean("script/laws.json")

    generate_laws(law_json_path=law_json_path, out_folder=out_folder)

    print(f"""
    HTML files have been written to the {out_folder} directory.

    Feel free to open them in your browser.
    """)


def generate_laws(law_json_path, out_folder):
    """Generate all law documents by calling law_html()
    for each law listed in laws.json."""
    with open(law_json_path,encoding='UTF-8') as lawfile:
        laws = json.loads(lawfile.read())

        if out_folder not in os.listdir():
            os.mkdir(out_folder)

        for law in laws:
            lawtxt = open(law.get("path"),encoding='UTF-8').read()
            lawname = law.get("name")

            filename = dirclean(
                f"{out_folder}/{lawname.replace(' ','_')}.html")

            mode = "x"

            if os.path.exists(filename):
                mode = "w"

                print(f"Warning: file {os.path.abspath(filename)} already exists, overwriting!")

            with open(
                filename, mode,
                encoding='UTF-8'
            ) as htmlfile:
                htmlfile.write(law_html(lawname, lawtxt))

                if args.verbose:
                    print(tw.dedent(f"Generated HTML for {law.get('name')},"
                                + f" wrote it to {os.path.realpath(filename)}")
                         )


if __name__ == "__main__":
    parser = ap.ArgumentParser(
        description="Generate Rainychville law documents in HTML format"
    )

    parser.add_argument(
        "-o","--output", help="Output folder for HTML documents")
    parser.add_argument(
        "-v", "--verbose", help="Be verbose", action="store_true"
    )
    parser.add_argument(
        "-b", "--browser", help="Open the folder containing the"+
                                " HTML documents in your browser",
                                action="store_true"
    )

    args = parser.parse_args()

    if args.output is None:
        args.output = "generated_html_laws"

    main(args)

    if args.browser:
        wb.open(os.path.realpath(args.output))
