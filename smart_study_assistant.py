import tkinter as tk
from datetime import datetime

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

# ----------Pomodoro Functions----------
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
    if timer_id: # Ensure timer_id exists before cancelling
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
    minutes = current_time // 60
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
        minutes = current_time // 60
        seconds = current_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        #Change color for breaks
        if status_label.cget("text") == "Status: Break Time!":
            timer_label.config(fg="green")
        else:
            timer_label.config(fg="white")

        current_time -= 1
        timer_id = root.after(1000, update_timer)

    elif current_time < 0:
        # Time is up
        root.bell() # Play a sound
        pomodoro_count += 1
        status_label.config(text=f"Status: Pomodoro {pomodoro_count} completed!")

        #Logic for switching between work and break sessions
        if pomodoro_count % 4 == 0:
            status_label.config(text="Status: Long Break!")
            current_time = long_break_time
        else:
            status_label.config(text="Status: Break Time!")
            current_time = short_break_time

        # Log the completion
        log_study_session()

        #Update the timer label and restart
        minutes = current_time // 60
        seconds = current_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        start_timer() # Automatically restart for the next session


# ----------To-Do List Functions----------
def add_task():
    """Adds a new task to the listbox."""
    task = task_entry.get().strip()
    if task:
        todo_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    """Removes the selected task from the listbox and logs it as completed."""
    try:
        selected_index = todo_listbox.curselection()[0]
        completed_task = todo_listbox.get(selected_index) # Get the task text before deleting
        todo_listbox.delete(selected_index)

        # Log the completed task
        current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{current_time_str}] Completed task: '{completed_task}'.\n"
        log_text.insert(tk.END, log_entry)
        log_text.see(tk.END) # Scroll to the bottom

    except IndexError:
        pass # No item selected


# ----------Daily Study Log Functions----------
def log_study_session():
    """Logs the completed Pomodoro session."""
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time_str}] Completed a {work_time/60}-minute Pomodoro session.\n"
    log_text.insert(tk.END, log_entry)
    log_text.see(tk.END)    # Scroll to the bottom

def save_log():
    """Saves the log to a text file."""
    with open("study_log.txt", "w") as file:
        log_content = log_text.get("1.0", tk.END)
        file.write(log_content)
    # Optional: provide user feedback
    status_label.config(text="Status: Log Saved!")
    root.after(2000, lambda: status_label.config(text="Status: Ready"))

def load_log():
    """Loads the log from a text file on startup."""
    try:
        with open("study_log.txt", "r") as file:
            log_content = file.read()
            log_text.delete("1.0", tk.END)
            log_text.insert(tk.END, log_content)
    except FileNotFoundError:
        pass # File doesn't exist, do nothing


# Main application window
root = tk.Tk()
root.title("Smart Study Assistant")
root.geometry("800x600")
root.configure(bg="#2c3e50")

# ----------Frames----------
# Create frames for Layout
timer_frame = tk.Frame(root, padx=20, pady=20, bg="#34495e")
timer_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

right_side_frame = tk.Frame(root, padx=20, pady=20, bg="#34495e")
right_side_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

# To-Do List Frame inside the right_side_frame
todo_frame = tk.Frame(right_side_frame, padx=10, pady=10, bg="#2c3e50")
todo_frame.pack(side='top', fill='both', expand=True, pady=(0, 10))

# Daily Study Log Frame inside the right_side_frame
log_frame = tk.Frame(right_side_frame, padx=10, pady=10, bg="#2c3e50")
log_frame.pack(side='bottom', fill='both', expand=True, pady=(10, 0))

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


# ----------TO-DO LIST WIDGETS----------
todo_title_label = tk.Label(todo_frame, text="To-Do List", font=("Helvetica", 16, "bold"), fg="#ecf0f1", bg="#2c3e50")
todo_title_label.pack(pady=(0, 10))

task_entry = tk.Entry(todo_frame, width=50, font=("Helvetica", 12))
task_entry.pack(pady=5)

button_frame_todo = tk.Frame(todo_frame, bg="#2c3e50")
button_frame_todo.pack(pady=5)

add_button = tk.Button(button_frame_todo, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#3498db", fg="white", activebackground="#2980b9")
add_button.pack(side='left', padx=5)

remove_button = tk.Button(button_frame_todo, text="Remove Task", font=("Helvetica", 12), bg="#e74c3c", fg="white", activebackground="#c0392b", command=remove_task)
remove_button.pack(side='left', padx=5)

todo_listbox = tk.Listbox(todo_frame, height=10, width=50, font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1", selectbackground="#1abc9c", bd=0)
todo_listbox.pack(pady=10, fill='both', expand=True)


# ----------DAILY STUDY LOG WIDGETS----------
log_title_label = tk.Label(log_frame, text="Daily Study Log", font=("Helvetica", 16, "bold"), fg="#ecf0f1", bg="#2c3e50")
log_title_label.pack(pady=(0, 10))

log_text = tk.Text(log_frame, height=10, width=50, font=("Helvetica", 10), bg="#34495e", fg="#ecf0f1", bd=0)
log_text.pack(fill='both', expand=True)

log_button_frame = tk.Frame(log_frame, bg="#2c3e50")
log_button_frame.pack(pady=5)

save_button = tk.Button(log_button_frame, text="Save Log", command=save_log, font=("Helvetica", 12), bg="#16a085", fg="white", activebackground="#1abc9c")
save_button.pack(pady=5) # Adjusted packing for single button

# Load the log file on startup
load_log()

# Start the main loop
root.mainloop()