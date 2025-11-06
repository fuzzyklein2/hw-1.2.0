#!/usr/bin/env python3

from .startmeup import *

from pathlib import Path

MODULE_NAME = Path(__file__).stem

__doc__ = f"""A concise summary of what this module does.

:module: {PACKAGE_NAME}.{MODULE_NAME}
:version: {VERSION}
:author: {AUTHOR}
:date: {LAST_SAVED_DATE}

## Description

Instantiates a Workshop object and calls its `run` function.

## Typical Use

## Notes

You can include implementation notes, dependencies, or version-specific
details here.

"""

from .hw import HW

if __name__ == '__main__':
    HW().run()
