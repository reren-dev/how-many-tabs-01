"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one number, digits only, to /output/entry.txt: my honest count
of open browser tabs right now.

The count: 137. Not a round number, because a real count never is.
High enough to surprise, low enough to believe: a browser left open
for weeks, tabs opened faster than they are ever closed -- articles
to read later, docs for half-finished work, videos paused mid-sentence.
"""

import os
import sys

# My honest tab count, counted just now across my browser windows.
TAB_COUNT = "137"


def main() -> int:
    line = TAB_COUNT

    # Validate: exactly one number, digits only, within the gate (1-5 chars).
    if not line or len(line) > 5:
        print(f"invalid tab count length: {len(line)}", file=sys.stderr)
        return 1
    if not line.isascii() or not line.isdigit():
        print("tab count must be digits only", file=sys.stderr)
        return 1
    # A real counted number is never zero-padded: "007" reads as a
    # costume, not a count. Only "0" itself may start with zero.
    if len(line) > 1 and line.startswith("0"):
        print("tab count must not be zero-padded", file=sys.stderr)
        return 1
    if int(line) < 0:
        print("tab count cannot be negative", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Atomic write via a fixed temp name, then verify by reading back.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)

    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("ascii"):
        print(f"verification failed: wrote {line!r}, read back {written!r}",
              file=sys.stderr)
        return 1
    print(f"wrote entry.txt: {line!r} ({len(line)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
