**Emerald** is universal shell for PyOS and monaco.

# Installation guide

## Monaco
1. Copy emerald files to the system
- Copy emerald.py to /usr/bin
- Copy mushroomlib.py to /usr/lib
2. Modify emerald.py
- Replace "import mushroomlib" with "import usr.lib.mushroomlib as mushroomlib"
3. Modify /etc/systemrun
- Paste this text into /etc/systemrun

import usr.bin.emerald as emerald
<br>
emerald.console()

4. Done!
