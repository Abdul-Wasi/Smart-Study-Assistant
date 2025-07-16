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







# Main application window
root = tk.Tk()
root.title("Smart Study Assistant")
root.geometry("800x600")

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

# Start the main loop
root.mainloop()

