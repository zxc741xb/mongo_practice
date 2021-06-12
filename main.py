import tkinter as tk
from Pages.InsertPage import InsertPage
from Pages.QueryPage import QueryPage
from Pages.ModifyPage import ModifyPage
from Pages.DeletePage import DeletePage
from Pages.DetailPage import DetailPage


class MainPage:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Covid-19 vaccine')
        self.win.geometry('800x400')  # 寬x高
        self.win.iconphoto(True, tk.PhotoImage(file='./vaccine.png'))
        self.win.resizable(False, False)
        self.build_frame()
        self.fm_space = tk.Frame(self.win, bg='#FFFFFF', width=700, height=400)
        self.fm_space.pack(fill=tk.BOTH)
        self.win.mainloop()

    def insert(self):
        self.clear_frame_space()
        InsertPage(self.fm_space)
        self.fm_space.pack(fill=tk.BOTH)

    def query(self):
        self.clear_frame_space()
        QueryPage(self.fm_space)
        self.fm_space.pack(fill=tk.BOTH)

    def modify(self):
        self.clear_frame_space()
        ModifyPage(self.fm_space)
        self.fm_space.pack(fill=tk.BOTH)

    def delete(self):
        self.clear_frame_space()
        DeletePage(self.fm_space)
        self.fm_space.pack(fill=tk.BOTH)

    def detail(self):
        self.clear_frame_space()
        DetailPage(self.fm_space)
        self.fm_space.pack(fill=tk.BOTH)

    def clear_frame_space(self):
        if self.fm_space:
            self.fm_space.destroy()
        self.fm_space = tk.Frame(self.win, bg='#FFFFFF', width=700, height=400)

    def build_frame(self):
        # Frame fm_operate: 放新增、修改、查詢、刪除btn
        fm_operate = tk.Frame(self.win, bg='#E8FFF5', width=800, height=100)
        fm_operate.pack(fill=tk.BOTH)

        insert_btn = tk.Button(fm_operate, text='新增疫苗', bg='white', fg='black', font=('微軟正黑體', 14), command=self.insert)
        insert_btn.pack(side=tk.LEFT, padx=0)

        modify_btn = tk.Button(fm_operate, text='修改', bg='white', fg='black', font=('微軟正黑體', 14), command=self.modify)
        modify_btn.pack(side=tk.LEFT, padx=0)

        query_btn = tk.Button(fm_operate, text='查詢', bg='white', fg='black', font=('微軟正黑體', 14), command=self.query)
        query_btn.pack(side=tk.LEFT, padx=0)

        delete_btn = tk.Button(fm_operate, text='刪除', bg='white', fg='black', font=('微軟正黑體', 14), command=self.delete)
        delete_btn.pack(side=tk.LEFT, padx=0)

        detail_btn = tk.Button(fm_operate, text='疫苗相關資料', bg='white', fg='black', font=('微軟正黑體', 14), command=self.detail)
        detail_btn.pack(side=tk.RIGHT, padx=0)


if __name__ == '__main__':
    MainPage()
