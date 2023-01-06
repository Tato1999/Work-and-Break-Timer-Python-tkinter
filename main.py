import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
counter = 0
start_on = False
mark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global mark, counter, timer
    mark = ""
    counter = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg="RED")
    canvas.itemconfig(timer_text, text=f"00:00")
    check_label.config(text=mark)       
    
    
        
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global counter, mark
    counter += 1
    if counter == 0:
        canvas.itemconfig(timer_text, text=f"00:00")            
    elif counter == 8:
        title_label.config(text="Break", fg="RED")
        start_count_down(LONG_BREAK_MIN,0)
        mark = ""
    elif counter % 2 != 0:
        title_label.config(text="Work", fg="GREEN")
        start_count_down(WORK_MIN,0)
        mark = "✔"
        check_label.grid(column=1,row=3) 
    elif counter % 2 == 0:
        title_label.config(text="Break", fg="PINK")
        mark = ""
        start_count_down(SHORT_BREAK_MIN,0)

    check_label.config(text=mark)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_count_down(min,sec):
    global timer
    add_zero = ''
    add_zero_min = ""
    if sec < 10:
        add_zero = '0'
    else:
        add_zero = ''

    if min < 10:
        add_zero_min = "0"
    else:
        add_zero_min = ""
    canvas.itemconfig(timer_text, text=f"{add_zero_min}{min}:{add_zero}{sec}")
    if min >= 0:
        if sec <= 0:
            min -= 1
            sec = 5
            timer = window.after(1000, start_count_down, min, sec - 1) 
        else:
            timer = window.after(1000, start_count_down, min, sec - 1) 
        # if min < 0:
        #     canvas.itemconfig(timer_text, text=f"00:00")
    elif min < 0:
        canvas.itemconfig(timer_text, text=f"00:00")            
            
# # comented method are used in course
# count_min = math.floor(count/60) #to see how many minute is in our value

# count_sec = count % 60
# canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
# if count > 0:
#     window.after(1000, start_count_down count - 1)
## count value is maybe 188/ 188/60 = 3 min and 8 sec

        
    

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()

window.title("Timer")
window.config(padx=50,pady=50,bg=YELLOW)


title_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME,30))
title_label.grid(column=1,row=0)
check_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW)


start_button = tkinter.Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0,row=2)
reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0, bg=YELLOW)
reset_button.grid(column=2,row=2)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)

image_src = tkinter.PhotoImage(file='/Users/programing/Desktop/programing/Work_Timer/tomato.png')

canvas.create_image(100,112, image=image_src)

timer_text = canvas.create_text(103,130, text='00:00', fill='white', font=(FONT_NAME,35, "bold"))

canvas.grid(column=1,row=1)





window.mainloop()
