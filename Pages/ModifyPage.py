import tkinter as tk
from tkinter import messagebox
from lib.DBMgr import DBMgr


class ModifyPage:
    def __init__(self, frame):
        self.frame = frame
        self.key = tk.StringVar()
        self.value = tk.StringVar()
        self.key2 = tk.StringVar()
        self.value2 = tk.StringVar()
        self.build_frame()
        self.dbmgr = DBMgr()

    def modify(self):
        myQuery = {self.key.get(): self.value.get()}
        newValue = {'$set': {self.key.get(): self.value2.get()}}
        self.dbmgr.modify(myQuery, newValue)
        messagebox.showinfo('modify_info', '已修改完成')

    def build_frame(self):
        label1 = tk.Label(self.frame, text='欲修改的值', bg='#FFF8D7', fg='black', font=('微軟正黑體', 12))
        label1.pack()

        key = tk.Label(self.frame, text='key', bg='white', fg='black', font=('微軟正黑體', 12))
        key.pack()
        key_entry = tk.Entry(self.frame, textvariable=self.key, width=40)
        key_entry.pack()

        value = tk.Label(self.frame, text='value', bg='white', fg='black', font=('微軟正黑體', 12))
        value.pack()
        value_entry = tk.Entry(self.frame, textvariable=self.value, width=40)
        value_entry.pack()

        label2 = tk.Label(self.frame, text='更新值', bg='#FFF8D7', fg='black', font=('微軟正黑體', 12))
        label2.pack()

        key2 = tk.Label(self.frame, text='key', bg='white', fg='black', font=('微軟正黑體', 12))
        key2.pack()
        key2_entry = tk.Entry(self.frame, textvariable=self.key2, width=40)
        key2_entry.pack()

        value2 = tk.Label(self.frame, text='value', bg='white', fg='black', font=('微軟正黑體', 12))
        value2.pack()
        value2_entry = tk.Entry(self.frame, textvariable=self.value2, width=40)
        value2_entry.pack()

        button = tk.Button(self.frame, text="確認", bg='white', fg='black', font=('微軟正黑體', 12), command=self.modify)
        button.pack(pady=50)
