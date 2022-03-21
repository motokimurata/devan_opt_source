import tkinter
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class TestTkcalender(tkinter.Frame):

    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.master.title("tkカレンダーテスト")
        self.master.geometry("800x600")

        # カレンダーのスタイル
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('DateEntry',
                        fieldbackground='white',
                        background='white',
                        foreground='black',
                        arrowcolor='darkblue')

        self.data_start_date = DateEntry(style='DateEntry',showweeknumbers=False)
        self.data_start_date.place(x=200, y=230)
        
        self.data_end_date = DateEntry(style='DateEntry',showweeknumbers=False)
        self.data_end_date.place(x=400, y=230)

        self.print_button = tkinter.Button(master, text="Set date", bg="white", font=(14), command=self.click_print)
        self.print_button.place(x=200, y=150, width=100, height=40)
        
    def click_print(self):
        return self.data_start_date.get_date(), self.data_end_date.get_date()

def main():
    root = tkinter.Tk()
    root = TestTkcalender(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()