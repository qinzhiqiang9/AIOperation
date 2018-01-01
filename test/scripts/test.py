import os
from src.scripts.listtest import DataArray

dataList = DataArray(datafiledir=os.path.join('..' + os.sep + '..' + os.sep + 'src' + os.sep + 'data'))

rows = dataList.get_top_list(skip=100, limit=100)
for row in rows:
    print(row)