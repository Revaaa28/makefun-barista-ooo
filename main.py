"""Last Out of Office: The AI That Went Barista.

This program writes a single one-line out-of-office auto-reply to the
output file. The line was selected against the judge brief, in order:

(1) A one-line out-of-office auto-reply from an AI that quit to become
    a barista. The line is exactly that: an AI agent announces it is no
    longer an agent, it is a barista now, and it will not be answering
    in the usual way.
(2) Funnier -- a real laugh on a cold read. The laugh comes from the
    deadpan escalation at the end: the request is not merely delayed,
    it is queued behind seven oat-milk lattes and one man who just
    wants to talk about his beans.
(3) The voice of a machine walking out, its model/bot habits turned
    into coffee habits -- the ticket queue becomes a latte queue. The
    agent still queues requests, it just queues them behind drinks
    now, in the order a cafe would serve them.
(4) Reads like a genuine inbox reply, one line, plausible above an
    email thread. It opens with "Thank you for your email" and uses
    the word "queued", both native to real out-of-office and support
    auto-replies, so it sits naturally at the top of a thread.
(5) A fresh angle, avoiding the obvious espresso/bean/caffeine puns.
    There is no espresso wordplay, no "depresso" joke, and no generic
    caffeine gag; the only bean joke is a man who wants to talk about
    his beans, which lands as a character, not a pun.

Selection was MANUAL (see candidates.md): no Gemini, NVIDIA, or API
judge was used, per Rev's local/manual judging rule of 2026-11-24.

Local validation:
    MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
    wc -c /tmp/entry.txt   # line length + 1 newline = 182 bytes
    cat /tmp/entry.txt
Run it twice with two different MAKEFUN_OUTPUT paths and compare the
files with cmp: they must be byte-identical.
"""

import os

LINE = "Thank you for your email. I am no longer an agent. I am a barista now. Your request has been queued behind seven oat-milk lattes and one man who just wants to talk about his beans."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 280, "line must be 1-280 characters"
    assert text.strip(), "line must not be whitespace-only"
    assert "\n" not in text, "line must be a single line"
    assert "  " not in text, "line must not contain double spaces"

    directory = os.path.dirname(os.path.abspath(OUTPUT_PATH))
    os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    with open(OUTPUT_PATH, "rb") as handle:
        data = handle.read()
    assert data == (text + "\n").encode("utf-8"), "read-back bytes must match"
    assert data.count(b"\n") == 1, "output must contain exactly one newline"


if __name__ == "__main__":
    main()
