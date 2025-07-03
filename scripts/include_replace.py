import re
import sys
from pathlib import Path

# Usage: python scripts/include_replace.py README.md

def replace_include_blocks(target_path: str):
    target_file = Path(target_path)
    if not target_file.exists():
        print(f"File not found: {target_path}")
        sys.exit(1)

    content = target_file.read_text(encoding="utf-8")

    def replacer(match):
        include_path = match.group(1).strip()
        include_file = Path(include_path)
        if not include_file.exists():
            return f"<!-- INCLUDE {include_path} -->\n*File not found: {include_path}*\n<!-- /INCLUDE -->"
        include_content = include_file.read_text(encoding="utf-8").strip()
        return f"<!-- INCLUDE {include_path} -->\n{include_content}\n<!-- /INCLUDE -->"

    pattern = re.compile(r"<!-- INCLUDE ([^>]+) -->.*?<!-- /INCLUDE -->", re.DOTALL)
    new_content = pattern.sub(replacer, content)
    target_file.write_text(new_content, encoding="utf-8")
    print(f"Updated {target_path} with included content.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/include_replace.py <target_file>")
        sys.exit(1)
    replace_include_blocks(sys.argv[1])
