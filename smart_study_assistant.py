import tkinter as tk

# ----------Global Variables----------
#Timer Variables
work_time = 25 * 60
short_break_time = 5 * 60
long_break_time = 15 * 60
current_time = work_time
is_running = False
timer_id = None
pomodoro_count = 0

# ----------Helper Functions----------
def start_timer():
    """Starts or resumes the timer."""
    global is_running
    is_running = True
    update_timer()
    start_button.config(state=tk.DISABLED)
    pause_button.config(state=tk.NORMAL)

def pause_timer():
    """Pauses the timer."""
    global is_running, timer_id
    is_running = False
    root.after_cancel(timer_id)
    start_button.config(state=tk.NORMAL)
    pause_button.config(state=tk.DISABLED)

def reset_timer():
    """Resets the timer to work time"""
    global current_time, is_running, timer_id
    is_running = False
    if timer_id:
        root.after_cancel(timer_id)
    current_time = work_time
    minutes = current_time / 60
    seconds = current_time % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    timer_label.config(fg= "white")
    start_button.config(state=tk.NORMAL)
    pause_button.config(state=tk.DISABLED)
    status_label.config(text="Status: Ready")

def update_timer():
    """Updates the timer label every second."""
    global current_time, timer_id, pomodoro_count

    if is_running and current_time >= 0:
        minutes = current_time / 60
        seconds = current_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        #Change color for breaks
        if status_label.cget("text") == "Status: break Time!":
            timer_label.config(fg="green")
        else:
            timer_label.config(fg="white")

        current_time -= 1

    elif current_time < 0:
        # Time is up
        root.bell() # Play a sound
        pomodoro_count += 1

        #Logic for switching between work and break sessions
        if pomodoro_count % 4 == 0:
            status_label.config(text="Status: Long Break!")
            current_time = long_break_time
        else:
            status_label.config(text="Status: Break Time!")
            current_time = short_break_time

        # Log the completion
        log_study_session()

        #Update the timer label aand restart
        minutes = current_time / 60
        seconds = current_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        start_timer() # Automatically restart for the next session







# Main application window
root = tk.Tk()
root.title("Smart Study Assistant")
root.geometry("800x600")
root.configure(bg="#2c3e50")

# ----------Frames----------
# Create frames for Layout
timer_frame = tk.Frame(root, padx=20, pady=20)
timer_frame.pack(side='left', fill='both', expand=True)

right_side_frame = tk.Frame(root, padx=20, pady=20)
right_side_frame.pack(side='right', fill='both', expand=True)

# To-Do List Frame inside the right_side_frame
todo_frame = tk.Frame(right_side_frame, padx=10, pady=10)
todo_frame.pack(side='top', fill='both', expand=True)

# Daily Study Log Frame inside the right_side_frame
log_frame = tk.Frame(right_side_frame, padx=10, pady=10)
log_frame.pack(side='bottom', fill='both', expand=True)

# ----------Timer Widgets----------
timer_title_label = tk.Label(timer_frame, text="Pomodoro Timer", font=("helvetica", 24, "bold"), fg="#ecf0f1", bg="#34495e")
timer_title_label.pack(pady=10)

status_label = tk.Label(timer_frame, text="Status: Ready", font=("Helvetica", 16), fg="#bdc3c7", bg="#34495e")
status_label.pack(pady=5)

timer_label = tk.Label(timer_frame, text="25:00", font=("Helvetica", 72, "bold"), fg="#ecf0f1", bg="#34495e")
timer_label.pack(pady=20)

button_frame = tk.Frame(timer_frame, bg="#34495e")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_timer, font=("Helvetica", 12), bg="#27ae60", fg="white", activebackground="#2ecc71")
start_button.pack(side='left', padx=5)

pause_button = tk.Button(button_frame, text="Pause", command=pause_timer, font=("Helvetica", 12), bg="#f39c12", fg="white", activebackground="#f1c40f", state=tk.DISABLED)
pause_button.pack(side='left', padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_timer, font=("Helvetica", 12), bg="#e74c3c", fg="white", activebackground="#c0392b")
reset_button.pack(side='left', padx=5)

# Start the main loop
root.mainloop()

