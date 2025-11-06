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

from pygnition.picts import *
from pygnition.program import Program
from pygnition.lumberjack import info, warn

class HW(Program):
    def __init__(self):
        super().__init__()

    def test(self):
        warn(f'{self.program_name} is under construction!')
        self.dump()

    def run(self):
        super().run()
        print(f'Hello, {GLOBE_AMERICA_PICT.strip()} !')

def main():
    p = HW()
    if p.testing:
        p.test()
    p.run()

if __name__ == '__main__':
    main()
