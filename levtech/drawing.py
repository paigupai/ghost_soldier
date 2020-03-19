# coding:utf-8
# import numpy as np
# import matplotlib.pyplot as plt 
import levtechDB
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')
# end date
endDate = datetime.now(JST)
print(endDate)

startDate = endDate - timedelta(days=7)

languageDataList = levtechDB.get_language_data(startDate,endDate)
languageNameList = [] 
languageCountList = []
for languageData in languageDataList:
    languageNameList.append(languageData[1])
    languageCountList.append(languageData[2])
plt.bar(range(len(languageCountList)), languageCountList, tick_label=languageNameList)
plt.title("今週:" + endDate.strftime("%m/%d/%Y, %H:%M:%S"))
plt.xlabel("言語")
plt.ylabel("案件数")
plt.savefig("levtech/examples.png")