#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Yan Wang on 16-6-15


from Tkinter import *           # 导入 Tkinter 库
import tkMessageBox

import os
import commands
import subprocess

import Config_data


#self.text_usr.get('0.0',END)  提取Text部件中的文本（所有）



#vpn quick 主类
class VPN_main:
    def __init__(self):

        #储存 用户名，密码，ip，以及对应的地址列表等信息的全局变量

        self.config_data = Config_data.Config_data()

        self.config_data.read_form_file()



        self.main_Windows = Tk()    #Tkinter 主循环

        self.main_Windows.wm_minsize(300,300)

        label_top_str = StringVar()  #顶部文字 内容
        label_top = Label(self.main_Windows,textvariable = label_top_str,relief = RAISED)
        label_top_str.set("DeVPN 辅助程序")
        label_top.pack()

        label_usr_str = StringVar()     #用户名
        label_usr = Label(self.main_Windows,textvariable = label_usr_str,relief=RAISED)
        label_usr_str.set("User Name:")
        label_usr.pack()


        self.text_usr = Text(self.main_Windows,heigh=1) #用户名 文本框
        self.text_usr.insert(INSERT,self.config_data.usr)
        self.text_usr.pack()

        label_pwd_str = StringVar()     #密码
        label_pwd = Label(self.main_Windows,textvariable = label_pwd_str,relief = RAISED)
        label_pwd_str.set("Password:")
        label_pwd.pack()

        self.text_pwd = Text(self.main_Windows,heigh=1) #密码框
        self.text_pwd.insert(INSERT,self.config_data.pwd)
        self.text_pwd.pack()

        self.button_connect  = Button(self.main_Windows,text="CONNECT",command=self.connect)    #连接vpn按钮
        self.button_connect.pack()

        self.button_refresh = Button(self.main_Windows,text="REFRESH",command=self.refresh)    #刷新地址列表
        self.button_refresh.pack()

        self.button_save=Button(self.main_Windows,text="Save",command=self.save)
        self.button_save.pack()

        self.text_add = Text(self.main_Windows,heigh=1) #地址文本框
        self.text_add.insert(INSERT,self.config_data.add)
        self.text_add.pack()

        self.information_var=StringVar()    #最低部用来显示当前操作状态的变量
        label_info = Label(self.main_Windows,textvariable = self.information_var,relief = RAISED)
        self.information_var.set("By Yan Wang")
        label_info.pack()



    def save(self):
        '''
        保存用户名，地址，和服务器IP到config.cache(json)文件。
        :return:
        '''
        usr = self.text_usr.get('0.0', END)
        pwd = self.text_pwd.get('0.0', END)
        add = self.text_add.get('0.0', END)

        # print usr,len(usr[0:len(usr)-1])

        self.config_data.usr = usr[0:(len(usr) - 1)]
        self.config_data.pwd = pwd[0:(len(pwd) - 1)]
        self.config_data.add = add[0:(len(add) - 1)]

        self.config_data.save_to_file()


    def connect(self):
        self.information_var.set("saving usr,pwd,")
        self.save()
        self.information_var.set("connecting.  ..")
        #tkMessageBox.showinfo("connect button",self.text_usr.get('0.0',END))

        usr= self.text_usr.get('0.0',END)
        pwd=self.text_pwd.get('0.0',END)
        add=self.text_add.get('0.0',END)

        #print usr,len(usr[0:len(usr)-1])

        usr = usr[0:(len(usr)-1)]
        pwd = pwd[0:(len(pwd)-1)]
        add = add[0:(len(add)-1)]

        cmd = 'echo '+ pwd +' | sudo openconnect -u ' + usr + '  ' + add +' --no-cert-check'

        #print cmd
        subprocess.Popen(cmd,shell=True)




        self.information_var.set("connected")

    def refresh(self):
        tkMessageBox.showinfo("refresh button","refresh button")



    def run(self):

        self.main_Windows.mainloop()






if __name__ == '__main__':
    VPN_main_process = VPN_main()

    VPN_main_process.run()
