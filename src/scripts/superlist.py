
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import sys
import time
import collections
import pprint


class super_list:
    datafiledir = None
    datafilename = None
    haveheader = True
    fileheader = []
    filecontent = []
    filelenth = 0


    def __init__(self, datafiledir=os.path.join('..' + os.sep + 'data'), datafilename='train.csv', haveheader=True):
        self.datafiledir = datafiledir
        self.datafilename = datafilename
        self.haveheader = haveheader

        datafile = open(self.datafiledir + os.sep + self.datafilename)
        fileReader = csv.reader(datafile)
        for row in fileReader:
            row.insert(0, fileReader.line_num)  # insert row number at first column
            if self.haveheader is True and fileReader.line_num is 1:
                self.fileheader = row
            else:
                row[2] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(row[2])))
                self.filecontent.append(row)
        self.filelength = len(self.filecontent)
        datafile.close()

    def get_file_header(self):
        return self.fileheader

    def get_file_content(self):
        return self.filecontent

    def get_top_list(self, skip=0, limit=None, f=lambda row:True):
        filteredlist = list(filter(f,self.filecontent))
        limitedlist = filteredlist[skip:len(filteredlist) if limit is None else limit + skip]
        return limitedlist

    def get_content_len(self):
        return len(self.filecontent)

    def group_by_coulumn(self, columnNum=0):

        a = np.array(self.filecontent)

        d = collections.Counter(self.filecontent)
        for k in d.keys():
            print(k)

    def print_summary_list(self, ls=[]):
        pprint.pprint(ls)
        print('Amount for target list is ' + str(len(ls)))

    # def __del__(self):
        # print('add code to clear')