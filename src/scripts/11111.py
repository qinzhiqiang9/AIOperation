import numpy as np
from src.scripts.superlist import SuperList

dataList = SuperList()
dataList.load()
#exceptions = dataList.get_top_list(f=lambda r: r[4] == str(1))
#dataList.print_summary_list(exceptions)

# print(dataList.__len__())
print(len(dataList))

#dataList.print_summary_list(np.array(dataList.filecontent)[:,1:2])
#print(allException)
# print(dataList.get_content_len())
# dataList.group_by_coulumn()
