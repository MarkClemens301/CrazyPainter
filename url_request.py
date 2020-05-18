# -*- coding: utf-8 -*-
""" Just like a browser """
from requests_html import HTMLSession
import pyppeteer
import asyncio

    
class HTMLSessionFixed(HTMLSession):
    """ Add optional argument: headless """
    def __init__(self, headless=True):
        super().__init__()
        self.headless = headless
        
    @property
    def browser(self):
        if not hasattr(self, "_browser"):
            self.loop = asyncio.get_event_loop()
            # headless change to False
            self._browser = self.loop.run_until_complete(pyppeteer.launch(headless=self.headless, args=['--no-sandbox']))
        return self._browser


def get(url, render=True):
    session = HTMLSessionFixed(headless=True)
    r = session.get(url)
    if render:
        r.html.render(keep_page=True, sleep=1, timeout=10)
    return r

def get_save(image_url, file_path):
    image = get(image_url, render=False)
    with open(file_path, 'wb') as f:
        f.write(image.html.raw_html)
            
if __name__ == "__main__":
    r = get('http://httpbin.org/headers')
    print(r.html.raw_html)
    # print(user_agent())

