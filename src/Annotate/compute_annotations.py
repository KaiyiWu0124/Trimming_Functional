"""
This file takes a ppi file with integer labels, and a json mapping that maps integer label to string labels, and returns a new ppi file with string labels, representing the actual name of the nodes in the PPI file.
"""

from annotations import *
import argparse
import json

parser = argparse.ArgumentParser()

"""
infile       : The input ppi file with integer annotated nodes
--dictname   : A dictionary mapping from integer to string labels
--outfile    : Output ppi file with string labels
"""

parser.add_argument("infile", help = "Input file to be annotated.")
parser.add_argument("-d", "--dictname", help = "Annotation dictionary name.")
parser.add_argument("-o", "--outfile", help = "Output annotated file.")

args = parser.parse_args()

ifile = args.infile
dname = args.dictname
ofile = args.outfile

with open(dname, "r") as df:
    adict = json.load(df)

annotate(ifile, adict, ofile)
