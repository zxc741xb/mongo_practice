import tkinter as tk
from lib.DBMgr import DBMgr
import webbrowser


def callback(url):
    webbrowser.open_new_tab(url)


class DetailPage:
    def __init__(self, frame):
        self.frame = frame
        self.build_frame()
        self.dbmgr = DBMgr()

    def callback(url):
        webbrowser.open_new_tab(url)

    def build_frame(self):
        link1 = tk.Label(self.frame, text="1. 疾管署疫苗簡介", bg='white', fg="blue", font=('微軟正黑體', 14), cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://www.cdc.gov.tw/Category/MPage/epjWGimoqASwhAN8X-5Nlw"))

        link2 = tk.Label(self.frame, text="2. WHO Coronavirus disease (COVID-19): Vaccines", bg='white', fg="blue", font=('微軟正黑體', 14), cursor="hand2")
        link2.pack()
        link2.bind("<Button-1>", lambda e: callback("https://www.who.int/news-room/q-a-detail/coronavirus-disease-(covid-19)-vaccines?topicsurvey=v8kj13)&gclid=Cj0KCQjw8IaGBhCHARIsAGIRRYqQYz27a03tLm4-cmaaLOFw3gIgiYtm7-u_nbGJiluGhIsKOMoy_KMaAqQAEALw_wcB"))
