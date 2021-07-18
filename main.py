import datetime #for reading present date
import time
from plyer import notification #for getting notification on PC

title = 'Notification App!'
message= ''
time_mes = {}

count = 0

def pop_not():
    notification.notify(title= title,
                    message=message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
    time.sleep(25)


while count<2:
    x = str(input("Enter time in the format HHTT"))
    y = input("Enter message to be displayed")
    time_mes[x] = y
    count += 1

while True:
    now = datetime.datetime.now()
    current_time = now.strftime('%H:%M:%S')
    now_time = str(current_time)[0:5]
    if now_time in time_mes:
        message = time_mes[now_time]
        pop_not()
