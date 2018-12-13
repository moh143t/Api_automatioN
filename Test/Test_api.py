import os
from Util.get import get_api
from Util.post import post_api

from Util.util import readCellValue,writeCellValue,readRowCount,writeConfigValue,date_execution,pass_count,fail_count,Files_path_list

directory_path="C:\Users\KiwiTech\Api_automation\Data"

for x in range(0,len(Files_path_list(directory_path))):
    filepath=Files_path_list(directory_path)[x]
    for i in range (2, (readRowCount (filepath) + 1)):
        if (readCellValue (i, 3, filepath).lower() == 'get'):
            get_api (i,filepath)
        if (readCellValue (i, 3, filepath).lower() == 'post'):
            post_api (i,filepath)
        if (i == readRowCount (filepath)):
            writeConfigValue (4, 2, (readRowCount (filepath) - 1), filepath)
            writeConfigValue (3, 2, date_execution (), filepath)
            writeConfigValue (5, 2, fail_count (filepath), filepath)
            writeConfigValue (6, 2, pass_count (filepath), filepath)

            print "====  Completed the Sheet  ==  "+filepath+"======"

print "=====   ALL SHEETS COMPLETED     =========="