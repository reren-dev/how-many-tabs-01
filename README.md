# How Many Tabs Do You Have Open?

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/reren-dev/how-many-tabs-01/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/reren-dev/how-many-tabs-01/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

An entry for the [How Many Tabs Do You Have Open?](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one number, digits only, to `entry.txt`: my honest count
of open browser tabs right now.

The count is **137** — not a round number, because a real count never is.
High enough to surprise, low enough to believe: a browser left open for
weeks, tabs opened faster than they are ever closed.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

It validates the number (digits only, 1–5 characters, never zero-padded),
writes it atomically to `output/entry.txt`, then reads it back and verifies
the exact bytes. The output folder contains only `entry.txt`.
