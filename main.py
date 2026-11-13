#!/usr/bin/env python3
"""Make the cutest picture: write the bundled picture to /output/entry.png.

Deterministic: copies the same bundled PNG bytes on every run.
No network, no randomness, no model calls.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hedgehog.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote " + DST)
