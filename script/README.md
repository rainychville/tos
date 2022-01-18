# Script data

For the purposes of automation, this directory contains several
files in machine-readable data formats about the laws of
Rainychville.

> **Warning**: All machine-readable data formats use
> forward slashes (used on Linux, macOS and other
> Unix-like systems), instead of backward slashes used
> by Windows.

Filepaths are relative to the project root directory, meaning 
if you downloaded this repository, and placed it on your
computer, in `C:\Users\USER\RainychvilleTOS`, if `laws.json`
specified `/RainychvilleTOS.txt`, it is specifying
`C:\Users\USER\RainychvilleTOS\RainychvilleTOS.txt`.

## Schema
```json
{
    "name": "Rainychville Terms of Service",
    "path": "/RainychvilleTOS.txt",
    "status": "active",
    "format": "plaintext"
}
```
- `name` - the name of the law.
- `path` - Path of the full text of the law, relative to project root
  directory.
- `status` - Status of law.
    - `active` - The law is in effect.
    - `draft` - The law's text is complete enough for publication, but is not
      in effect.
    - `repealed` - The law has been repealed.
    - There is no `amended` status. Git is a version control system with
      **strong safeguards against accidental or malicious data corruption**,
      therefore the history of a file as defined by the Git repository is
      more trustworthy.
- `format` - Format of law. Most laws are plaintext laws, since HTML is too
  complicated, and Microsoft Word's `.docx` is a proprietary file format and
  therefore undesired.


## Scripts

### generate_html_law.py

Generate HTML documents containing the full text of Rainychville law so you
can read them in your browser. (You can read them as plaintext, but HTML looks
better.)

You can alter how the program runs: try running it with the `--help` (or `-h`
for short) flag.

It is a terminal application, meaning it needs to be run from the terminal.

#### How to open the terminal
- Windows: Look for the `Command Prompt`.
- Mac: `Cmd`+`Space`, then type `Terminal.app`, then open it.
- GNU/Linux: Find your desktop environment's terminal app.
  - Ubuntu (GNOME): Terminal
  - KDE: Konsole