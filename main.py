import sys
import threading
import tkinter as tk
import time
import datetime
from plyer import notification

title = 'Notification App'
time_mes = {}
bs = []
running = True


# A function to handle notification
def notify_func():
    global running
    if not running:
        running = True
    while running:
        now = datetime.datetime.now()
        current_time = now.strftime('%H:%M:%S')
        now_time = str(current_time)[0:5]
        if now_time in time_mes:
            notification.notify(title=title,
                                message=time_mes[now_time],
                                app_icon=None,
                                timeout=10,
                                toast=False)
            time.sleep(10)


# Set the condition if not true and enter time and notification message to the dictionary
def set_notification():
    global bs
    t1 = user_input.get()
    n1 = user_input2.get()
    time_mes[t1] = n1
    bs = list(time_mes.items())
    add_listbox()


def stop():
    global running
    running = False
    master.quit()


def add_listbox():
    global bs
    global var
    var.set(bs)


def delete():
    global bs
    # index of the selected item in the listbox
    index = lb.curselection()
    # then find the item in the list
    list_item = bs[index[0]]
    # delete in the dictionary
    del time_mes[list_item[0]]
    bs.remove(list_item)
    add_listbox()


master = tk.Tk()
master.title("set notification")
tk.Label(master, text='Notification time').grid(row=0)
tk.Label(master, text='Notification message').grid(row=1)
user_input = tk.Entry(master)
user_input2 = tk.Entry(master)
user_input.grid(row=0, column=1)
user_input2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=stop).grid(row=3,
                                                  column=0,
                                                  sticky=tk.W,
                                                  pady=4)
tk.Button(master, text='Notify', command=lambda: threading.Thread(target=notify_func).start()).grid(row=3,
                                                                                                    column=2,
                                                                                                    sticky=tk.W,
                                                                                                    pady=4)
tk.Button(master, text='Add', command=set_notification).grid(row=2,
                                                             column=1,
                                                             sticky=tk.W,
                                                             pady=4)
tk.Label(master, text='Notifications').grid(row=0,
                                            column=3,
                                            sticky=tk.W,
                                            pady=4)

var = tk.StringVar()

lb = tk.Listbox(master, listvariable=var)
lb.grid(row=1,
        column=3)

tk.Button(master, text="Delete", command=delete).grid(row=3,
                                                      column=4,
                                                      sticky=tk.W,
                                                      pady=4)

master.mainloop()
