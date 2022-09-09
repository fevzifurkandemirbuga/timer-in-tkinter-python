import tkinter as tk

timer = None
white = "#ffffff"


def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timerText, text="00:00")
    
    
def start_timer():
    if type(timer) == str:
        reset_timer()
    countdown(int(spinbox.get())*60)
    
    
def countdown(second):
    global timer
    if second >= 0:
        timer_minute = second//60
        timer_second = second % 60
        if timer_second < 10:
            timer_second = f"0{timer_second}"
        canva.itemconfig(timerText, text=f"{timer_minute}:{timer_second}")
        timer = window.after(1000, countdown, second-1,)
        
        
window = tk.Tk()
window.title("timer")
window.config(bg=white)
window.config(padx=100, pady=50)

canva = tk.Canvas(width=250, height=250, bg=white, highlightthickness=0)
clockPhoto = tk.PhotoImage(file="saat.png")
canva.create_image(125, 125, image=clockPhoto)
timerText = canva.create_text(133, 160, font=("ariel", 15, "bold"), text="00:00")
canva.grid(column=1, row=1)

titleLabel = tk.Label(text="TİMER", font=("ariel", 50, "bold"), bg=white)
timeLabel = tk.Label(text="Countdown(minute)", bg=white)
resetButton = tk.Button(text="reset", command=reset_timer)
startButton = tk.Button(text="start", command=start_timer)
spinbox = tk.Spinbox(from_=0, to=60, width=5)

titleLabel.grid(column=1, row=0)
resetButton.grid(column=2, row=2)
timeLabel.grid(column=1, row=2)
startButton.grid(column=0, row=2)
spinbox.grid(column=1, row=3)
window.mainloop()
