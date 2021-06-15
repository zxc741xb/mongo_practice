import tkinter as tk
from tkinter import messagebox
from lib.DBMgr import DBMgr


class InsertPage:
    def __init__(self, frame):
        self.frame = frame
        self.key = tk.StringVar()
        self.value = tk.StringVar()
        self.key2 = tk.StringVar()
        self.value2 = tk.StringVar()
        self.key3 = tk.StringVar()
        self.value3 = tk.StringVar()
        self.build_frame()
        self.dbmgr = DBMgr()

    def insert(self):
        item = {'name': self.value.get(), 'country': self.value2.get(), self.key3.get(): self.value3.get()}
        self.dbmgr.insert(item)
        messagebox.showinfo('insert_info', '新增完成')

    def build_frame(self):
        label1 = tk.Label(self.frame, text='插入資料', bg='#FFF8D7', fg='black', font=('微軟正黑體', 12))
        label1.pack()

        key_label = tk.Label(self.frame, text='name', bg='white', fg='black', font=('微軟正黑體', 12))
        key_label.pack()

        value_entry = tk.Entry(self.frame, textvariable=self.value, width=40)
        value_entry.pack()

        key2_label = tk.Label(self.frame, text='country', bg='white', fg='black', font=('微軟正黑體', 12))
        key2_label.pack()

        value2_entry = tk.Entry(self.frame, textvariable=self.value2, width=40)
        value2_entry.pack()

        dash_label = tk.Label(self.frame, text='-----------------------------------------------------', bg='white', fg='black',
                              font=('微軟正黑體', 12))
        dash_label.pack(pady=10)

        key2_label = tk.Label(self.frame, text='其他資訊(eg. 併發症,適用對象)：自行輸入', bg='white', fg='black', font=('微軟正黑體', 12))
        key2_label.pack()
        key2_entry = tk.Entry(self.frame, textvariable=self.key3, width=40)
        key2_entry.pack()

        value3_label = tk.Label(self.frame, text='其他資訊內容', bg='white', fg='black', font=('微軟正黑體', 12))
        value3_label.pack()
        value3_entry = tk.Entry(self.frame, textvariable=self.value3, width=40)
        value3_entry.pack()

        button = tk.Button(self.frame, text="確認", bg='white', fg='black', font=('微軟正黑體', 12), command=self.insert)
        button.pack(pady=40)
