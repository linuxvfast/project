#-*- coding:utf-8-*-
import json
from country_codes import get_country_code

#将数据加载到列表
filename = 'population_json.json'
with open(filename) as f:
    datas = json.load(f)   #将数据转换为Python可以处理的格式

#打印1990年每个国家的人口数量
for person_data in datas:
    if person_data['Year'] == 1990:
        country_name = person_data['Country Name']
        population = int(float(person_data['Value']))
        print(country_name + ":" + str(population))
