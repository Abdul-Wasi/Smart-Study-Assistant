import tkinter as tk

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

