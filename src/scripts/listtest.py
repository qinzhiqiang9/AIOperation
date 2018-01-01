
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import sys
import time


class DataArray:
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

    def get_top_list(self, include_header=True, skip=0, limit=None):
        topList = []
        if include_header is True and self.haveheader is True:
            topList.append(self.fileheader)

        topList += self.filecontent[skip:self.filelength if limit is None else limit + skip]
        return topList

    def __del__(self):
        print('add code to clear')