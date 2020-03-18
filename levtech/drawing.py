# coding:utf-8
# import numpy as np
# import matplotlib.pyplot as plt 
import levtechDB
from datetime import datetime, timedelta, timezone


# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')
# end date
endDate = datetime.now(JST).date

startDate = datetime.now(JST) - datetime.timedelta(days=10)

languageDataList = levtechDB.get_language_data(startDate,endDate)