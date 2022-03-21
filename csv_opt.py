import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog, tkinter.messagebox

class CsvViewer2:
    
    def __init__(self):
        
        self.root = None
        self.data = None
        self.tree = None
        self.path = None
    
    def choice_file(self):
        # ファイル選択ダイアログの表示
        self.root = tk.Tk()
        self.root.withdraw()
        # ここの1行を変更　fTyp = [("","*")] →　fTyp = [("","*.csv")]
        fTitle = "最適化処理を行うCSVファイルを選択してください"
        fTyp = [("","*.csv")]
        curdir = os.getcwd()
        iDir = curdir
        file = tkinter.filedialog.askopenfilename(title = fTitle, filetypes = fTyp ,initialdir = iDir)
        return file



    def quit_me(self): # tkinterセッション終了
            self.root.quit()
            self.root.destroy()
            
    def start(self):

        self.call_root_window()
        self.call_csv_reader_widget()
        self.call_treeview_widget()
        self.root.mainloop()    
        
    def show_table(self): # 最適化処理結果をテーブルで表示
            
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", lambda :self.quit_me(root))
        self.root.title("Optimization Result")
        self.root.geometry("620x400")
        self.tree = ttk.Treeview(self.root,show='headings')
        
        # 列を３列作る
        self.tree["column"] = (1, 2, 3)

        # ヘッダーテキスト
        self.tree.heading(1, text="コンテナNo.")
        self.tree.heading(2, text="希望納品日")
        self.tree.heading(3, text="最適納品日")
        
        # 列の幅
        self.tree.column(1, width=200)
        self.tree.column(2, width=200)
        self.tree.column(3, width=200)

        # データ挿入
        for i in range(len(col0)):
            self.tree.insert("", "end", values=(col0[i], col1[i], col2[i]))
        
        # 設置数
        #button = tk.Button(root, text='Download_CSV', command= lambda :show_graph(before_l,after_l,intx,strday))
        #button.pack(side=tk.BOTTOM)
        button2 = ttk.Button(self.root, text='Show_Graph', command= lambda :self.show_graph())
        button2.pack(side=tk.BOTTOM)
        self.tree.pack(side=tk.LEFT,fill=tk.BOTH)

        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command = self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.root.mainloop()

    def show_graph(self): # 最適化前（Before）と最適化後（After）の棒グラフを表示
        
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", lambda :self.quit_me())
        self.root.title("Optimization Result Graph")
        self.root.geometry("1000x600")   
        
        fig = plt.figure(figsize=[12,12])
        ax1 = fig.add_subplot(221)
        ax1.bar(intx_c,before)
        ax1.set_title('Before')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Amounts of Equipment')
        ax1.yaxis.set_major_locator(MultipleLocator(1))
        plt.xticks(intx_c, strdate_c,rotation=90)
        plt.ylim(0, 20)
        plt.tight_layout()

        ax2 = fig.add_subplot(222)
        ax2.bar(intx_c,after)
        ax2.set_title('After')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Amounts of Equipment')
        ax2.yaxis.set_major_locator(MultipleLocator(1))
        plt.xticks(intx_c, strdate_c,rotation=90)
        plt.ylim(0, 20)
        plt.tight_layout()
        

        # Canvas
        canvas = FigureCanvasTkAgg(fig, master=root)  # Generate canvas instance, Embedding fig in root
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
        canvas._tkcanvas.pack() 

        # root
        self.root.update()
        self.root.deiconify()
        self.root.mainloop()
    