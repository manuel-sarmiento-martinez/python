#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html

print("Nombre del cual deseas conocer el género:")
nombre = input()
r = requests.get(f'https://es.wikipedia.org/wiki/{nombre}_(nombre)')

print(r.url)

tree = html.fromstring(r.content)
gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
namegender = tree.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
footer = tree.xpath('//div[@class="action-list"]//p/text()')

for item in namegender:
    if item in ["\nMasculino", "\nFemenino"]:
        print("Género: " + item)