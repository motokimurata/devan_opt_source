import numpy as np
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from datetime import time
import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
import tkinter.ttk as ttk
from pulp import*
from ortoolpy import addvars, addbinvars
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from opt_gui import show_table
from opt_gui import choice_file
import csv_view
import calender_view

target_date = calender_view.TestTkcalender()
target_date.start()
date_filter_start = target_date.s_date
date_filter_end = target_date.e_date
dt_native = pd.to_datetime(date_filter_start)

print(date_filter_start)
print(date_filter_end)
print(type(date_filter_start))
print(type(date_filter_end))

print(type(dt(2022,1,27)))
print(dt_native)
print(type(dt_native))