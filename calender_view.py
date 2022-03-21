import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime as dt

class TestTkcalender:

    def __init__(self):
        self.root = None  # ルートウィンドウ
        self.data_start_date = None
        self.data_end_date = None
        self.print_button = None
        self.s_date = None
        self.e_date = None
        #self.frame = self.Frame(self.master, relief="ridge", bd=1)
    
    def start(self):
        self.call_root_window()
        self.call_csv_reader_widget()
        self.root.mainloop()
    
    def call_root_window(self):
        """
        ルートウィンドウを呼び出す
        """
        self.root = tk.Tk()
        self.root.geometry('600x500')
        self.root.title('SelectCsv')    
         
        
    def call_csv_reader_widget(self):
        # カレンダーのスタイル
        frame = tk.Frame(self.root, relief="ridge", bd=1)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('DateEntry',
                        fieldbackground='white',
                        background='white',
                        foreground='black',
                        arrowcolor='darkblue')

        tk.Button(frame, text="Set date", command=self.click_print).pack(side=tk.LEFT)
        
        self.data_start_date = DateEntry(style='DateEntry',showweeknumbers=False)
        self.data_start_date.place(x=200, y=230)
        
        self.data_end_date = DateEntry(style='DateEntry',showweeknumbers=False)
        self.data_end_date.place(x=400, y=230)

        #self.print_button = tk.Button(frame, text="Set date", bg="white", font=(14), command=lambda:self.click_print())
        #tk.Button(frame, text="Set date", bg="white", font=(14), command=lambda:self.click_print())
        #self.print_button.place(x=100, y=100, width=100, height=40)
    
    def click_print(self):
        self.out_path()
        self.quit_me()
    
    
    def quit_me(self): # tkinterセッション終了
        self.root.quit()
        self.root.destroy()
        
    def out_path(self):
        self.s_date = self.data_start_date.get_date()
        self.e_date = self.data_end_date.get_date()
        return self.s_date, self.e_date
        #print(tdatetime)
        #print(self.data_start_date.get_date())
        #return self.data_start_date.get_date(), self.data_end_date.get_date()
        
if __name__ == "__main__":
    viewer = TestTkcalender()
    viewer.start()
    print(viewer.s_date)