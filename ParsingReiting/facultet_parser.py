#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Получает список институтов доступных на УМКА ВолГУ """
from lxml import etree
import requests


if __name__ == '__main__':
    r = requests.get("http://umka.volsu.ru/rating/new/rs1.php")
    r.encoding = 'cp1251'
    page = etree.HTML(r.text)
    f = open("name.txt", "w")
    for block in page.xpath("//option"):
        facultet_name =  block.text
        facultet_value = block.attrib['value']
        if facultet_value != "0":
            f.write(facultet_value + ": " + facultet_name.encode('UTF-8') + '\n')
    f.close()