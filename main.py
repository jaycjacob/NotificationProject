import datetime #for reading present date
import time
from plyer import notification #for getting notification on PC

title = 'Notification App!'
message= ''
time_mes = {}
now = datetime.datetime.now()
#current_time = now.strftime('%H:%M:%S')
hy = 18


def pop_not():
    notification.notify(title= title,
                    message=message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)



x = input("Enter time in the format hour, minutes, seconds")
y = input("Enter message to be displayed")
time_mes[x] = y
#    b = input("Enter y to continue or N to exit")
if str(hy) in time_mes:
    message = "happy"
#    message = time_mes[current_time]
    pop_not()
else:
    print("none")
