# Starless #

Modern Python sanity checkers choke on star imports, e.g.

```
from sys import *

stdin.write("foo")
```

wouldn't it be nicer to have the code look like:


```
from sys import stdin

stdin.write("foo")
```

automatically? This is what this tool is all about.

```
# pip3 install starless
```

to get started, and run just `starless *.py` or something.

This is primarily personal amusement tool that I needed when I used it to
convert some old PyQt code to PySide2. I hope someone else finds it useful
too.
