#-*- coding:utf-8-*-

#字典COUNTRIES 包含的键和值分别为两个字母的国别码和国家名
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    '''根据国家的名称返回pygal使用的两个字母的国别码'''
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果给出的国家名没有找见对应的code，返回None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('China'))