import sys
import tkinter as tk
import time
import datetime
from plyer import notification

title = 'Notification App!'
time_mes = {}


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
            time.sleep(25)


master = tk.Tk()
master.title("set notification")
tk.Label(master, text='Time for notification').grid(row=0)
tk.Label(master, text='Notification message').grid(row=1)
user_input = tk.Entry(master)
user_input2 = tk.Entry(master)
user_input.grid(row=0, column=1)
user_input2.grid(row=1, column=1)
ttt = str(user_input.get())


def set_notification():
    t1 = user_input.get()
    n1 = user_input2.get()
    time_mes[t1] = n1


tk.Button(master, text='Quit', command=master.quit and sys.exit).grid(row=3,
                                                                      column=0,
                                                                      sticky=tk.W,
                                                                      pady=4)
tk.Button(master, text='Notify', command=notify_func).grid(row=3,
                                                           column=2,
                                                           sticky=tk.W,
                                                           pady=4)
tk.Button(master, text='Set', command=set_notification).grid(row=2,
                                                             column=1,
                                                             sticky=tk.W,
                                                             pady=4)

master.mainloop()
