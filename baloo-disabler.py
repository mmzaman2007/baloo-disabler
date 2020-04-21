#!/usr/bin/python3
import os
filepath = os.environ['HOME'] + "/.config/autostart-scripts/baloo-disabler.sh"
file = open(filepath, "w")
file.write("""#!/bin/sh
balooctl disable
""")
file.close()
os.chmod(filepath, 0o775)
print("\nSuccess! Restart to activate...\n")
