#!/usr/bin/env python
"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

FEMRESP_DAT="2002FemResp.dat.gz"
FEMRESP_DCT="2002FemResp.dct"

def read_data(dct=FEMRESP_DCT, dat=FEMRESP_DAT, nrows=None):
    dct = thinkstats2.ReadStataDct(dct)
    df = dct.ReadFixedWidth(dat, compression='gzip', nrows=nrows)
    return df


def process_data(data):
    preg = nsfg.ReadFemPreg()

    # make the preg map
    preg_map = nsfg.MakePregMap(preg)

    # loop through pregnum data
    for index, pregnum in data.pregnum.items():
        caseid = data.caseid[index]
        print(f"{caseid = }: {pregnum = }")


def main(script):
    """Tests the functions in this module.

    script: string script name
    print('%s: All tests passed.' % script)
    """


    df = read_data()
    process_data(df)
    

if __name__ == '__main__':
    main(*sys.argv)
