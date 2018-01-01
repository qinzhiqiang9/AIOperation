#! python3

import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

# ./data/
defaultDir = os.path.join('.' + os.sep + 'data' + os.sep)
defaultFileName = 'train.csv'
haveHeader = True

fileContent = open(defaultDir + defaultFileName)
contentReader = csv.reader(fileContent)

trainNormals = []
trainErrors = []
for row in contentReader:
    if haveHeader and contentReader.line_num == 1:
        continue
    elif contentReader.line_num < 100:
    #else:
        if row[3] == str(0):
            print(row[1])
            print(dt.time.strftime(row[1]))
            trainNormals.append(row)
        else:
            trainErrors.append(row)

timesNormals = [row[1] for row in trainNormals]
valuesNormals = [row[2] for row in trainNormals]

timesErrors = [row[1] for row in trainErrors]
valuesErrors = [row[2] for row in trainErrors]

# plt.plot(timesNormals,valuesNormals,'o')
# plt.plot(timesErrors,valuesErrors,'r')

#fig = plt.figure(figsize=(20,15), dpi=80)
#ax = fig.add_subplot(111)

#type1 = ax.scatter(timesErrors, valuesErrors, s=0.001, c='red')
#type2 = ax.scatter(timesNormals, valuesNormals, s=2, c='blue')

plt.scatter(timesNormals, valuesNormals, edgecolors='none', c='blue', s=3)
plt.scatter(timesErrors, valuesErrors, edgecolors='none', c='red', s=3)

#minx = np.min(timesNormals)
#maxx = np.max(timesNormals)
#miny = np.min(valuesNormals)
#maxy = np.max(valuesNormals)

xlabels = [0, 1493568000, 1493578000, 1493588000, 1493598000]
ylabels = [0, 1, 2, 3, 4]

# plt.xticks(timesNormals, xlabels, rotation='vertical')
# plt.yticks(valuesNormals, ylabels, rotation='vertical')

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.savefig('./charts' + os.sep + 'chart.pdf', bbox_inches='tight')

#plt.savefig('./charts' + os.sep + 'chart.png')