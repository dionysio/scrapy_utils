import re

import lxml.html
from lxml import etree
import scrapy


def strip_html(html):
    if html and isinstance(html, scrapy.selector.SelectorList):
        html = etree.tostring(html[0].root).decode()

    if html:
        document = lxml.html.document_fromstring(html)
        return document.text_content()
    return ''


def strip_alpha(alphanum):
    if isinstance(alphanum, str):
        return ''.join(c for c in alphanum if c in '0123456789,').replace(',', '.')
    return alphanum


def camel_case_to_snake_case(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
