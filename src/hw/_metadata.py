#!/usr/bin/env python3

from pathlib import Path

MODULE_NAME = Path(__file__).stem

from datetime import datetime
from importlib import resources
from pathlib import Path
import subprocess
import sys

from pygnition._data_tools import is_valid_data_line
from pygnition._imports import pkg_path
from pygnition._last_saved_date import last_saved_datetime
from pygnition._read_lines import read_lines

PROJECT_NAME = "hw"  # your package name
PACKAGE_PATH = pkg_path(PROJECT_NAME)
print(f'{PACKAGE_PATH=}')
VERSION = '1.2.0b'
AUTHOR = 'Russell Klein'
LAST_SAVED_DATE = last_saved_datetime(__file__).date()
PROJECT_DATA_DIR = PACKAGE_PATH / 'data'
DESCRIPTION = (PROJECT_DATA_DIR / 'description.txt').read_text()
REQ_FILE = PROJECT_DATA_DIR / 'requirements.txt'
# if not REQ_FILE.exists(): REQ_FILE = PROJECT_DATA_DIR / 'requirements.in'
if not REQ_FILE.exists(): REQ_FILE.touch()
REQUIREMENTS = '\n'.join([f'* {s}' for s in read_lines(REQ_FILE) if is_valid_data_line(s)])

__doc__ = f"""Provides metadata for the project, notably the `PROJECT_NAME`.

========== ⚠️  WARNING! ⚠️  ==========
This project is currently under construction.
Stay tuned for updates.

Package: 🔥  pygnition 🔥
Module: {MODULE_NAME}
Version: {VERSION}
Author: {AUTHOR}
Date: {LAST_SAVED_DATE}

## Description

This module defines the Workshop class.

## Typical Use
```python
args = parse_arguments()

## Notes

You can include implementation notes, dependencies, or version-specific
details here.

"""

