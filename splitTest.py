from archapp.interactive import EpicsArchive
import matplotlib.pyplot as plt
import pandas as pd
import xarray

arch = EpicsArchive(hostname="pscaa01-dev")
command = "find GDET:FEE1:241:ENRC start=0,4,13,48 end=2,12,30,45"

split = command.split()
pv = split[1]
start = split[2]
end = split[3]

if start.startswith("start="):
    start1=start.replace('start=', ' ')
    start2=start1.replace(',', ' ')
    start3 = start2.split()
    startDay = float(start3[0]) * 1
    startHour = float(start3[1])
    if startHour >= 24:
        print("Not more than 24 hours in a day")
    else:
        decSHour = startHour/24
 
    startMin = float(start3[2])
    if startMin >= 60:
        print("Not more than 60 minutes in a hour")
    else:
        decSMin = ((startMin/60)/24)
 
    startSec = float(start3[3])
    if startSec >= 60:
        print("Not more than 60 seconds in a hour")
    else:
        decSSec = (((startSec/60)/60)/24)
 
    stDec = startDay + decSHour + decSMin + decSSec
    print(stDec)


if end.startswith("end="):
    end1=end.replace('end=', ' ')
    end2=end1.replace(',', ' ')
    end3 = end2.split()
    endDay = float(end3[0]) * 1
    endHour = float(end3[1])
    if endHour >= 24:
        print("Not more than 24 hours in a day")
    else:
        decHour = endHour/24

    endMin = float(end3[2])
    if endMin >= 60:
        print("Not more than 60 minutes in a hour")
    else:
        decMin = ((endMin/60)/24)

    endSec = float(end3[3])
    if endSec >= 60:
        print("Not more than 60 seconds in a hour")
    else:
        decSec = (((endSec/60)/60)/24)

    etDec = endDay + decHour + decMin + decSec
    print(etDec)  

print(split)
 
#   
#getPV = arch.get(pv, xarray=True, start=start, end=end)
#array = getPV[pv]
#panda = array.to_pandas()
#transpose = panda.transpose()
#vals = transpose.get('vals')
#print(vals)
#
#sortVals = vals.sort_values()
#minVal = sortVals[0]
#print(minVal)
#lenOfVals = len(vals)
#maxVal = sortVals[(lenOfVals-1)]
#print(maxVal)
#plt.figure(figsize=(12,7))
#plot = plt.plot(vals)
#plt.ylabel('PV values')
#plt.xlabel('time')
#plt.ylim([(minVal-0.5),(maxVal+0.5)])
#plt.show(plot)
#

