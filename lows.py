#-*- coding:utf-8-*-
import csv
from matplotlib import pyplot as plt

filename = 'sitka.csv'
with open(filename) as f:
    #将文件全部读取出来
    reader = csv.reader(f)
    #next读取下一行，调用了一次，读取第一行
    head_row = next(reader)
    # print(head_row)
    # print('-----------------------')
    # for number in reader:
    #     print(number)
    # print('=========================================')
    # #enumerate函数获取每个元素的索引以及对应的值，跟字典中的items相似获取对应的键值
    # for index,column_header in enumerate(head_row):
    #     print(index,column_header)
    # print('`````````````````````````````````````````````')
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')
plt.title('Daily high temperatures',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()