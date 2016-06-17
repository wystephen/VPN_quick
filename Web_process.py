#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Yan Wang on 16-6-16

import sys
import urllib2
import urllib



class devpn_web:
    def __init__(self,web_add="devpn.info"):
        self.web_add = web_add


    def login(self):
        login_html=urllib2.urlopen('http://devpn.info/login/')
        print login_html.read()





if __name__ == '__main__':
    dw=devpn_web()
    dw.login()
