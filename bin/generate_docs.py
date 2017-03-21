#!/usr/bin/env python
import os
from lxml import etree, html
import glob
from datetime import datetime
import re


def readhtml(source):
    with open(source, 'r') as f:
        content = f.read()

    return html.fromstring(content)

PWD = os.getcwd()
dest_path = '_docs'

os.system('git clone https://github.com/ncss-tech/aqp.git /tmp/aqp')
os.system('git clone git@github.com:spadarian/aqp.git /tmp/aqp_site')

os.system('cd /tmp/aqp && Rscript -e "pkgdown::build_reference(examples=F, path=\'{}/{}\')"'.format(PWD, dest_path))

tree = readhtml('{}/{}/index.html'.format(PWD, dest_path))
row = tree.xpath('//div[@class="row"]')[0]
row = etree.tostring(row, method='html')

text = """---
layout: page
title: Documentation
header: Documentation
group: navigation
scripts: [jquery.sticky-kit.min.js, pkgdown.js]
permalink: /docs/
---
{% include JB/setup %}

"""

with open('{}/documentation.html'.format(PWD), 'w') as f:
    f.write(text)
    f.write(row.decode("utf-8"))


os.remove('{}/{}/index.html'.format(PWD, dest_path))

version = tree.xpath('//div[@class="page-header"]')[0]
version = etree.tostring(version)
version = re.findall('(?<=;).*(?=<)', version.decode("utf-8"))[0]

files = glob.glob('{}/*.html'.format(dest_path))

text_doc = u"""---
layout: doc
title: "{}"
aqp_version: {}
date: {}
scripts: [jquery.sticky-kit.min.js, pkgdown.js]
---

"""
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')

for f in files:
    tree = readhtml(f)
    title = tree.xpath('//title')[0].text[:-6]
    row = tree.xpath('//div[@class="row"]')[0]
    row = etree.tostring(row, method='html')
    with open(f, 'w') as wf:
        wf.write(text_doc.format(title, version, date).encode("utf-8"))
        wf.write(row.decode("utf-8"))
