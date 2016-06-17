#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Yan Wang on 16-6-17

import json


class Config_data:
    def __init__(self):
        self.usr=''
        self.pwd=''
        self.add=''


    def save_to_file(self):
        config_file=open('config.cache','w')
        data_str=json.dumps(self.convert_to_dict())
        config_file.write(data_str)
        config_file.close()

    def read_form_file(self):
        config_file=open('config.cache','r')
        data_str=config_file.read()

        print 'data str (function read from file:)',data_str

        the_dic = json.loads(data_str)
        print 'type of dict:' ,type(the_dic)
        print the_dic

        self.usr=the_dic['usr']
        self.pwd=the_dic['pwd']
        self.add=the_dic['add']

        config_file.close()


    def convert_to_dict(self):
        #print 'default(', repr(self), ')'
        # 把MyObj对象转换成dict类型的对象
        d = {'usr': self.usr,
             'pwd': self.pwd,
             'add':self.add
             }
        #d.update(self.__dict__)
        return d




