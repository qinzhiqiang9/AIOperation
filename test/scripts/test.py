
from src.scripts.listtest import DataArray

dataList = DataArray()

rows = dataList.get_top_list(skip=100, limit=100)
for row in rows:
    print(row)