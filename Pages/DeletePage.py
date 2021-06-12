import tkinter as tk
from tkinter import messagebox
from lib.DBMgr import DBMgr


class DeletePage:
    def __init__(self, frame):
        self.frame = frame
        self.key = tk.StringVar()
        self.value = tk.StringVar()
        self.build_frame()
        self.dbmgr = DBMgr()

    def delete(self):
        myQuery = {self.key.get(): self.value.get()}
        result = self.dbmgr.delete(myQuery)
        messagebox.showinfo('delete_info', '已刪除'+self.key.get()+':'+self.value.get()+'之資料')

    def build_frame(self):
        label1 = tk.Label(self.frame, text='刪除資料', bg='#FFF8D7', fg='black', font=('微軟正黑體', 14))
        label1.pack()

        key = tk.Label(self.frame, text='key', bg='white', fg='black', font=('微軟正黑體', 14))
        key.pack()
        key_entry = tk.Entry(self.frame, textvariable=self.key, width=80)
        key_entry.pack()

        value = tk.Label(self.frame, text='value', bg='white', fg='black', font=('微軟正黑體', 14))
        value.pack()
        value_entry = tk.Entry(self.frame, textvariable=self.value, width=80)
        value_entry.pack()

        button = tk.Button(self.frame, text='確認', bg='white', fg='black', font=('微軟正黑體', 14), command=self.delete)
        button.pack(pady=100)
