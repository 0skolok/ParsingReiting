#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Получает список групп доступных на УМКА ВолГУ """
from lxml import etree
import requests


if __name__ == '__main__':
    f = open("parse_rez_fac.txt", "r")
    facultet_dic = dict([i.split(': ') for i in f.readlines()])
    f.close()
    wf = open("name.txt", "w")
    for key in facultet_dic:
        wf.write(">>> " + key + ": " + facultet_dic.get(key))
        r = requests.post("http://umka.volsu.ru/rating/new/rs1.php", data={"Fak":key.split(': ')[0]})
        r.encoding = 'cp1251'
        page = etree.HTML(r.text)
        for block in page.xpath("//option"):
            group_name =  block.text
            group_value = block.attrib['value']
            if group_value != "0" and group_value not in facultet_dic.keys():
                wf.write(group_value + ": " + group_name.encode('UTF-8') + '\n')
    wf.close()