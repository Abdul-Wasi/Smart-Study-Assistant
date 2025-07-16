# Smart Study Assistant

**A productivity-focused desktop application built with Python and Tkinter to help students manage their study time and tasks effectively.**

---

## 🚀 Project Overview

The **Smart Study Assistant** is a unified desktop tool designed to enhance student productivity and concentration. It integrates three essential features: a **Pomodoro Timer**, a **To-Do List Manager**, and a **Daily Study Log**. Developed entirely in Python using the built-in `tkinter` library, this application provides an interactive and intuitive graphical user interface (GUI).

This project was a valuable exercise in practical GUI development, reinforcing fundamental Python concepts such as loops, file handling, time management, and real-world application logic. It emphasizes combining robust functionality with user-friendly design.

---

## ✨ Features

* **🍅 Pomodoro Timer:**
    * Helps users follow the widely-adopted 25-minute focused study sessions followed by short breaks (5 minutes) and longer breaks (15 minutes after every 4 sessions).
    * Improves concentration and reduces burnout by structuring study periods.
    * Visual countdown display with real-time updates.
    * "Start," "Pause," and "Reset" controls for flexible use.
    * Audible bell notification when a session ends.
* **✅ To-Do List Manager:**
    * Allows users to easily add, view, and remove tasks.
    * Integrates with the Daily Study Log: **completed tasks are automatically logged**.
* **📜 Daily Study Log:**
    * Keeps a chronological record of all completed Pomodoro sessions.
    * Automatically logs tasks marked as completed from the To-Do List.
    * Allows users to **save the log to a text file** for review or personal tracking.
    * Loads previous logs upon application startup, ensuring data persistence.

---

## 💻 How to Run

### Prerequisites

* Python 3.x installed on your system.
    * No external libraries are required as `tkinter` is part of Python's standard library.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone (Your Repository URL)
    cd smart-study-assistant
    ```
2.  **Run the application:**
    ```bash
    python smart_study_assistant.py
    ```

The application window should appear.

---

## 🧠 What I Learned

Developing the Smart Study Assistant was an invaluable learning experience. Key takeaways include:

* **GUI Development with Tkinter:** Gained practical skills in designing and implementing interactive user interfaces using `tkinter` widgets (Labels, Buttons, Entry fields, Listboxes, Text areas) and layout managers (`pack`).
* **Event-Driven Programming:** Deepened understanding of how GUIs respond to user input and time-based events, particularly through the use of `root.after()` for non-blocking timer updates, which is crucial for maintaining application responsiveness.
* **Application State Management:** Learned to manage the application's various states (e.g., timer running/paused, current session type) using global variables and conditional logic.
* **File Handling:** Implemented robust file I/O operations for saving and loading the daily study log, ensuring data persistence across sessions.
* **Modular Code Design:** Practiced organizing code into logical functions (e.g., `start_timer`, `add_task`, `save_log`) for better readability, maintainability, and reusability.
* **Real-World Application Logic:** Applied theoretical programming concepts to solve practical problems in time management and task organization, leading to a functional and useful tool.

---

## 🤝 Contributing

This project was developed for a course, but feel free to explore and suggest improvements!

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

---

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📧 Contact

Abdul Wasi - bhatabdul75@gmail.com
