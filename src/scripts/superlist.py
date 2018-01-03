
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import sys
import time
import collections
import pprint


class SuperList:

    def __init__(self, datafiledir=os.path.join('..' + os.sep + 'data'), datafilename='train.csv', haveheader=True):
        self.datafiledir = datafiledir
        self.datafilename = datafilename
        self.haveheader = haveheader
        self.fileheader = []
        self.filecontent = []

    def load(self):
        with open(self.datafiledir + os.sep + self.datafilename) as datafile:
            filereader = csv.reader(datafile)
            for row in filereader:
                row.insert(0, filereader.line_num)  # insert row number at first column
                if self.haveheader is True and filereader.line_num is 1:
                    self.fileheader = row
                else:
                    row[2] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(row[2])))
                    self.filecontent.append(row)

    @property
    def fileheader(self):
        return self.fileheader

    @property
    def filecontent(self):
        return self.filecontent

    def get_top_list(self, skip=0, limit=None, f=lambda row: True):
        filteredlist = list(filter(f, self.filecontent))
        limitedlist = filteredlist[skip:len(filteredlist) if limit is None else limit + skip]
        return limitedlist

    def __len__(self):
        return len(self.filecontent)

    def group_by_coulumn(self, columnNum=0):
        [row[0] for row in self.filecontent]

        a = np.array(self.filecontent)

        d = collections.Counter(self.filecontent)
        for k in d.keys():
            print(k)

    @staticmethod
    def print_summary_list(ls=[]):
        pprint.pprint(ls)
        print('Amount for target list is ' + str(len(ls)))

    # def __del__(self):
        # print('add code to clear')
