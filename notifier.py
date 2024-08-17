
from plyer import notification
from tkinter import *
from tkinter import messagebox
import time

windows = Tk()
windows.title("Notification App")
windows.geometry("500x500")
windows.config(bg="light green")




#details:
def get_details():
    get_title = title.get()
    get_title1 = title1.get()
    duration = title2.get() #duration
    
    if get_title == "" or get_title1 == "" or duration == "":
        messagebox.showerror("Alert","Empty!!! Your TextField is empty")
        
    else:
        int_time = int(duration)
        conversion = int_time * 60
        messagebox.showinfo("Info","Are You Sure?")
        
        time.sleep (conversion) # Application paused until conversion
        
        notification.notify(
    title = get_title,
    message = get_title1,
    app_name = "Notifier",
    timeout = 10             
    )
        
        

#Placeholder one for heading(Notification App)
heading_label = Label(windows, text = "Notification App", font=("Times New Roman", 20, "bold"), fg="blue")
heading_label.place(x = 130, y = 40)

#title to notify, placeholder
title_label = Label(windows, text="Notification Title", font=("Times New Roman", 13, "italic","bold"),bg="light blue",fg="black")
title_label.place(x = 25, y = 120 )

title = Entry(windows, width=30, font=("Times New Roman", 12))
title.place(x = 180, y = 120)

#Display Message, placeholder
disp_label = Label(windows, text="Display Message", font=("Times New Roman", 13, "italic", "bold"), bg="light blue",fg="black")
disp_label.place(x = 25, y = 190 )

title1 = Entry(windows, width=30, font=("Times New Roman", 12))
title1.place(x = 180, y = 190)

#Set Time, placeholder
time_label = Label(windows, text="Set Duration", font=("Times New Roman", 13, "italic", "bold"),bg="light blue",fg="black")
time_label.place(x = 25, y = 250 )

title2 = Entry(windows, width=5, font=("Times New Roman", 12))
title2.place(x = 180, y = 250)

#Min, Placeholder
min_label = Label(windows, text="mins", font=("Times New Roman", 10,"bold"))
min_label.place(x = 235, y = 250 )

#Button
button = Button(windows, text="Set", font=("Times New Roman", 13, "bold"), fg="#ffffff", bg="red", width=10, command=get_details)
button.place(x=140, y=300)

       
windows.resizable(0,0)
windows.mainloop()


