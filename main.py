#! /usr/bin/env python3
# -*- coding: utf-8 -*-
""" main """
import sys
import asyncio
import yaml
import os

import url_request
from utils import set_background

IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'img')
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'image_struct.yaml')

class image_downloader(object):
    """ download image
    """    
    def __init__(self, root_url):
        self.loop = asyncio.get_event_loop()
        self.web = url_request.get(root_url)
        
    # def url_generator(self, selection, interval):
        """ 
        TODO(AdjWang):
            1. An image url is like a folder path: 
                1) get -> root path url
                2) [several xpath] maybe used to generate [several path url for next level]
                3) get -> [several path url for next level] then goto 2) until get the [image url]
                4) get -> image url
                yield per image url to get.
            2. The image_structs should be simplified as follow:
                1) website1
                    1) root path
                    2) (image path)
                        1) xpath1
                        2) element1
                        3) xpath2
                        4) element2
                        ...
                2) websete2
                ...
        """
        # image_urls = self.web.html.xpath(selection['xpath']).attrs[selection['element']]
        # for image_url in image_urls:
        #     yield image_url

        # while True:
        #     async def _image_next_get(page):
        #         await page.press.keyboard('ArrowDown')
        #         await asyncio.sleep(interval)   # Wait for the real image loaded
        #     self.loop.run_until_complete(_image_next_get(self.web.html.page))
        #     image_urls = self.web.html.xpath(selection['xpath']).attrs[selection['element']]
        #     for image_url in image_urls:
        #         yield image_url
        
    def url_generator(self, selection, interval):
        async def _image_next_get(page):
            await page.keyboard.press('ArrowDown')
            await asyncio.sleep(interval)   # Wait for the real image loaded
        
        image_url = self.web.html.xpath(selection['xpath'], first=True).attrs[selection['element']]
        self.loop.run_until_complete(_image_next_get(self.web.html.page))
        selection['url'] = self.web.html.page.url
        return image_url, selection
                   
            
def load_config(config_file):
    with open(config_file, 'r') as f:
        image_struct = yaml.load(f.read(), Loader=yaml.FullLoader)
    return image_struct
    
def save_config(config_file, config_data):
    with open(config_file, 'w') as f:
        yaml.dump(config_data, f)

if __name__ == "__main__":
    image_struct = {
        'element': 'src',
        'url': r'http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E5%A3%81%E7%BA%B8&step_word=&hs=0&pn=0&spn=0&di=168330&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=&lm=-1&st=undefined&cs=3062374190%2C3164523231&os=609645438%2C61978557&simid=4067838971%2C577556431&adpicid=0&lpn=0&ln=3538&fr=&fmq=1589782577879_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=1920&height=1080&face=undefined&ist=&jit=&cg=wallpaper&bdtype=11&oriquery=%E5%A3%81%E7%BA%B8&objurl=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fd22bbcc815668a3244e4237c1731b98d8ee370a3.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bktstktst_z%26e3Bv54AzdH3F6jw1AzdH3Fveccca8bc&gsm=1&rpstart=0&rpnum=0&islist=&querylist=&force=undefined',
        'xpath': r'.//img[@id="currentImg"]',
    }
    if os.path.exists(CONFIG_PATH):
        image_struct = load_config(CONFIG_PATH)
    
    downloader = image_downloader(image_struct['url'])
    image_url, image_struct = downloader.url_generator(image_struct, interval=1)
    save_config(CONFIG_PATH, image_struct)
    
    if not image_url:
        raise Exception('image did not loaded!')
    url_request.get_save(image_url, IMAGE_PATH)
    set_background(IMAGE_PATH)        
    
