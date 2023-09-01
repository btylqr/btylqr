#!/usr/bin/env python3
'''
Convert WEBP image to gif - Works perfectly fine 
source of candy = https://www.sex.com/search/gifs?query=pawg+ass
'''
from PIL import Image
im = Image.open('1.webp')
im.info.pop('background', None)
im.save('that.gif', 'gif', save_all=True)