import csv
import numpy as np
import math
import pathlib
from math import log
import pandas as pd

datafile = pathlib.Path(__file__).parent.absolute().joinpath("datafile1.csv")
xL = np.linspace(1,100,100)
nData = 12
rng = np.random.default_rng(0)
dataDict = {'X':xL}
for iData in range(nData):
  data_str = "data{}".format(iData+1)
  # y = i + a* x^{-b}
  a = rng.uniform(2,5)
  b = rng.uniform(-2,-0.5)
  c = (iData%4) 
  yL = [ c+rng.uniform(-0.04,0.04) + a*(x**b) for x in xL]
  dataDict[data_str] = yL
  upbnd = rng.uniform(0.2,0.5)
  dataDict[data_str+"l"] = [y-rng.uniform(upbnd-0.1,upbnd) for y in yL] 
  dataDict[data_str+"u"] = [y+rng.uniform(upbnd-0.1,upbnd) for y in yL] 
  
df = pd.DataFrame(dataDict)
df.to_csv(datafile,index=False)
print("done")