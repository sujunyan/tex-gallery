import csv
import numpy as np
import math
import pathlib
from math import log

datafile = pathlib.Path(__file__).parent.absolute().joinpath("datafile.csv")
with open(datafile,"w",newline="") as f:
    f_csv = csv.writer(f,delimiter=" ") 
    xv = np.linspace(0,120)
    rows = []
    for i in range(len(xv)):
        xi = xv[i]
        row = [xi]
        for j in range(6):
            mul = 2*j+1
            row.append((log(mul*xi+1)))
        row.append(7.5)
        rows.append(row)
    f_csv.writerows(rows)
    