# Grimoire

**Grimoire** is a small Python source-code keyword scanner for reviewing repositories you own or are authorized to assess.

It searches local source files for the word `password` (case-insensitive) and reports matching file paths and line numbers. It does **not** crawl GitHub accounts, download repositories, or collect credentials.

## Requirements

- Python 3.9+
- No third-party packages required

## Usage

1. Download or clone a repository you own or have permission to review.
2. Open a terminal in this project folder.
3. Run:

   ```bash
   python grimoire.py /path/to/your/repository
   ```

   Example on Windows:

   ```powershell
   python grimoire.py "C:\Users\YourName\Projects\my-repo"
   ```

   Example on Linux:

   ```bash
   python3 grimoire.py ~/projects/my-repo
   ```

The scanner checks common source/configuration file types and skips common generated folders such as `.git`, `node_modules`, and virtual environments.

## Example output

```text
[!] Possible keyword match: src/auth.py:18
    password = input("Password: ")
Scan complete. 1 matching line(s).
```

A match is only a keyword hit—not proof that a real password or secret is present. Review results manually and avoid printing, sharing, or committing actual secrets.

## Scope and responsible use

Use this tool only on code you own or are explicitly authorized to assess. It performs a local text scan and does not attempt to log in, exploit systems, or access private repositories.

## Project files

- `grimoire.py` — scanner
- `requirements.txt` — no external dependencies
- `.gitignore` — ignores Python caches and local output
- `output/.gitkeep` — keeps the output folder in Git
