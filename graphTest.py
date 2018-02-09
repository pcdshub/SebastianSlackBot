from archapp.interactive import EpicsArchive
import matplotlib.pyplot as plt
import pandas as pd
import xarray

arch = EpicsArchive(hostname="pscaa01-dev")
command = "find GDET:FEE1:241:ENRC 1 1.5"

split = command.split()
pv = split[1]
start = split[2]
end = float(split[3])

print(split)
 
   
getPV = arch.get(pv, xarray=True, start=start, end=end)
array = getPV[pv]
panda = array.to_pandas()
transpose = panda.transpose()
vals = transpose.get('vals')
print(vals)

sortVals = vals.sort_values()
minVal = sortVals[0]
print(minVal)
lenOfVals = len(vals)
maxVal = sortVals[(lenOfVals-1)]
print(maxVal)
plt.figure(figsize=(12,7))
plot = plt.plot(vals)
plt.ylabel('PV values')
plt.xlabel('time')
plt.ylim([(minVal-0.5),(maxVal+0.5)])
plt.show(plot)


