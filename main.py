import sys
import threading
import tkinter as tk
import time
import datetime
from plyer import notification

title = 'Notification App!'
time_mes = {}
cancel = 0


def notify_func():
    while True:
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
        if cancel == 0:
            continue
        else:
            print("cancelled")
            break


master = tk.Tk()
master.title("set notification")
tk.Label(master, text='Time for notification').grid(row=0)
tk.Label(master, text='Notification message').grid(row=1)
user_input = tk.Entry(master)
user_input2 = tk.Entry(master)
user_input.grid(row=0, column=1)
user_input2.grid(row=1, column=1)


def set_notification():
    global cancel
    cancel = 0
    t1 = user_input.get()
    n1 = user_input2.get()
    time_mes[t1] = n1


def ha():
    global cancel
    cancel = 1


def quit_thread():
    thread = threading.Thread(target=ha)
    thread.start()
    thread.join()


tk.Button(master, text='Quit', command=quit_thread).grid(row=3,
                                                         column=0,
                                                         sticky=tk.W,
                                                         pady=4)
tk.Button(master, text='Notify', command=lambda: threading.Thread(target=notify_func).start()).grid(row=3,
                                                                                                    column=2,
                                                                                                    sticky=tk.W,
                                                                                                    pady=4)
tk.Button(master, text='Set', command=set_notification).grid(row=2,
                                                             column=1,
                                                             sticky=tk.W,
                                                             pady=4)

master.mainloop()
