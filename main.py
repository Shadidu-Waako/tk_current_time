import tkinter as tk
import time as tm


my_window = tk.Tk()
# my_window.title('Current time')
# # current_time = tm.strftime('%I:%M:%S:%p')
# current_time = tm.strftime('%H:%M:%S:%p')
# clock_label = tk.Label(my_window, font='algerian 80', bg='yellow', fg='black', text=current_time)
# clock_label.grid(row=0, column=0)


def display_time():
    current_time = tm.strftime('%H:%M:%S')
    clock_label['text'] = current_time
    my_window.after(1000, display_time)


my_window.title('Digital Clock')
clock_label = tk.Label(my_window, font='algerian 80', bg='black', fg='white')
clock_label.grid(row=0, column=0)
display_time()
my_window.mainloop()
