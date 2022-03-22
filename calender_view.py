import os
from re import S
import tkinter as tk
from tkinter import ANCHOR, ttk
from attr import s
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime as dt
from csv_view import CsvViewer

class TestTkcalender:

    def __init__(self):
        self.root = None  # ルートウィンドウ
        self.data_start_date = None
        self.data_end_date = None
        self.print_button = None
        self.s_date = None
        self.e_date = None
        self.booking_path = None
        self.warehouse_path = None
        self.test = CsvViewer()
        
    def start(self):
        self.call_root_window()
        self.call_csv_widget()
        self.call_csv_reader_widget()
        #self.call_csv_reader_widget()
        self.root.mainloop()
    
    def call_root_window(self):
        """
        ルートウィンドウを呼び出す
        """
        self.root = tk.Tk()
        self.root.geometry('600x500')
        self.root.title('SelectCsv')    
         
        
    def call_csv_widget(self):
        # カレンダーのスタイル
        frame = tk.Frame(self.root, relief="ridge", bd=1)
        frame.pack(fill=tk.BOTH, expand=True,padx=5, pady=60)
        #frame.columnconfigure(0, weight=1)
        #frame.rowconfigure(0, weight=1)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('DateEntry',
                        fieldbackground='white',
                        background='white',
                        foreground='black',
                        arrowcolor='darkblue')
        
        #button01 = ttk.Button(frame, text="Set date", width=8, padding=[1,2,1],command=self.click_print)
        lbl01 = ttk.Label(frame, text="開始日", width=13, justify='right')
        lbl02 = ttk.Label(frame, text="終了日", width=13, justify='right')
    
        self.data_start_date = DateEntry(style='DateEntry',showweeknumbers=False, width=13)
        
        self.data_end_date = DateEntry(style='DateEntry',showweeknumbers=False, width=13)
        
        lbl01.place(x=20,y=15)
        self.data_start_date.place(x=80, y=74)
        lbl02.place(x=260,y=15)
        self.data_end_date.place(x=320, y=74)
        #button01.place(x=480, y=36) 
        
    def call_csv_reader_widget(self):
        """
        csvファイルを読み込むためのウィジェットを呼び出す関数
        """
        # widget配置のフレームを作成
        frame = tk.Frame(self.root, relief="ridge", bd=1)
        frame.pack(fill=tk.BOTH, padx=5, pady=30)

        # ラベルを作成
        tk.Label(frame, text='Warehouse Plan file >>').pack(side=tk.LEFT)

        # CSVファイルのファイルパスを指定する入力フィールドを作成
        self.entry_field = tk.Entry(frame)
        self.entry_field.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # ファイルダイアログを呼び出すボタンを作成
        tk.Button(frame, text='Set CSV', command=lambda: self.extract_csv_path(self.entry_field)).pack(side=tk.LEFT)
        
        # widget配置のフレームを作成
        frame = tk.Frame(self.root, relief="ridge", bd=1)
        frame.pack(fill=tk.BOTH, padx=5, pady=30)

        # ラベルを作成
        tk.Label(frame, text='Devan Booking file >>').pack(side=tk.LEFT)

        # CSVファイルのファイルパスを指定する入力フィールドを作成
        self.entry_field2 = tk.Entry(frame)
        self.entry_field2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # ファイルダイアログを呼び出すボタンを作成
        tk.Button(frame, text='Set CSV', command=lambda: self.extract_csv_path(self.entry_field2)).pack(side=tk.LEFT)

        
        frame = tk.Frame(self.root, relief="ridge", bd=1)
        frame.pack(fill=tk.BOTH, padx=5, pady=50)

        # ラベルを作成
        tk.Label(frame, text='Optimization >>').pack(side=tk.LEFT)

        # CSVファイルのパスを戻り値として返し最適化処理を行うボタン
        tk.Button(frame, text='Go To',
                  #command=lambda: self.send_csv(entry_field.get(), 
                  command=lambda: self.send_path(  # entry_fieldに入力されているファイルパス
                                                )).pack(side=tk.LEFT)
        
    def extract_csv_path(self,entry_field):
        self.test.start()
        self.set_path(entry_field)
    
    def set_path(self,entry_field):
        """
        tk.Entryの内容をクリアした後にファイルダイアログを呼び出し
        選択したファイルパスを，tk.Entryに記入する関数。
        :param entry_field: tk.Entry
        """
        # tk.Entryに記入されている内容をクリアする
        entry_field.delete(0, tk.END)
        
        # ファイルダイアログの選択結果をtk.Entryの内容に挿入する
        #entry_field.insert(tk.END, str(file_path))
        entry_field.insert(tk.END, str(self.test.path))   

        
    def send_path(self):
        self.out_path()
        self.quit_me()
    
    def quit_me(self): # tkinterセッション終了
        self.root.quit()
        self.root.destroy()
        
    def out_path(self):
        self.s_date = self.data_start_date.get_date()
        self.e_date = self.data_end_date.get_date()
        self.booking_path = self.entry_field2.get()
        self.warehouse_path = self.entry_field.get()
        return self.s_date, self.e_date, self.booking_path,self.warehouse_path
        
if __name__ == "__main__":
    viewer = TestTkcalender()
    viewer.start()
    print(viewer.s_date)
    print(viewer.booking_path)