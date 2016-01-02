#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Получает список всех зачёток доступных на УМКА ВолГУ """
""" TODO: надо реализовать функционал """
from lxml import etree
import requests


if __name__ == '__main__':
    f = open("parse_rez_fac.txt", "r")
    for line in f.readlines():
        r = requests.post("http://umka.volsu.ru/rating/new/rs1.php", data={"Fak":line.split(': ')[0]})
        r.encoding = 'cp1251'
        page = etree.HTML(r.text)
        for block in page.xpath("//option"):
            print block.text
            print block.attrib['value']
