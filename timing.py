import time
from tkinter import Tk, Label, Button, Frame, Entry, messagebox


class SimpleTimingBoard:
    start_time = 0
elapsed_time = 0
running = False
paused = False
performance_data = []
current_data_index = 0
dark_mode = False

def update_timer(root, time_label, data_label):
    global start_time, elapsed_time, running, current_data_index
    if running:
        elapsed_time = time.time() - start_time
        display_time(time_label)
        display_data(data_label)
        root.after(100, update_timer, root, time_label, data_label)

def display_time(time_label):
    global elapsed_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    hours, minutes = divmod(minutes, 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
    time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")

def display_data(data_label):
    global performance_data, current_data_index
    if current_data_index < len(performance_data):
        name, performance = performance_data[current_data_index]
        data_label.config(text=f"{name} - {performance:.3f}")
        current_data_index += 1
    else:
        data_label.config(text="")

def start_timer(root, time_label, data_label):
    global running, paused, start_time, elapsed_time
    if not running and not paused:
        start_time = time.time() - elapsed_time
        running = True
        update_timer(root, time_label, data_label)
    elif paused:
        running = True
        paused = False
        start_time = time.time() - elapsed_time
        update_timer(root, time_label, data_label)

def pause_timer():
    global running, paused
    if running:
        running = False
        paused = True

def stop_timer():
    global running, paused
    running = False
    paused = False

def reset_timer(time_label, data_label):
    global running, paused, start_time, elapsed_time, current_data_index
    running = False
    paused = False
    start_time = 0
    elapsed_time = 0
    current_data_index = 0
    time_label.config(text="00:00:00.000")
    data_label.config(text="")

def add_custom_data(entry, data_label):
    global performance_data
    custom_input = entry.get()
    if custom_input:
        try:
            name, performance = custom_input.split(":")
            performance_data.append((name.strip(), float(performance.strip())))
            entry.delete(0, "end")
        except ValueError:
            messagebox.showerror("Error", "Invalid format. Use 'Name: Performance'.")
    else:
        messagebox.showwarning("Warning", "No data entered.")

def save_data():
    global performance_data
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for name, performance in performance_data:
                file.write(f"{name}: {performance:.3f}\n")
        messagebox.showinfo("Save", f"Data saved to {file_path}")

def load_data():
    global performance_data
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            performance_data = []
            for line in file:
                try:
                    name, performance = line.strip().split(":")
                    performance_data.append((name.strip(), float(performance.strip())))
                except ValueError:
                    continue
        messagebox.showinfo("Load", f"Data loaded from {file_path}")

def sort_by_name():
    global performance_data
    performance_data.sort(key=lambda x: x[0])
    messagebox.showinfo("Sort", "Data sorted by name.")

def sort_by_performance():
    global performance_data
    performance_data.sort(key=lambda x: x[1])
    messagebox.showinfo("Sort", "Data sorted by performance.")

def toggle_dark_mode(root, time_label, data_label):
    global dark_mode
    dark_mode = not dark_mode
    bg_color = "black" if dark_mode else "white"
    fg_color = "white" if dark_mode else "black"
    root.config(bg=bg_color)
    time_label.config(bg=bg_color, fg=fg_color)
    data_label.config(bg=bg_color, fg=fg_color)

def update_title(root):
    current_time = time.strftime("%H:%M:%S")
    root.title(f"Timing Board - {current_time}")
    root.after(1000, update_title, root)

# Main Program
if __name__ == "__main__":
    root = Tk()
    root.title("Timing Board")

    time_label = Label(root, text="00:00:00.000", font=("Helvetica", 48), bg="black", fg="white")
    time_label.pack(pady=20)

    data_label = Label(root, text="", font=("Helvetica", 14))
    data_label.pack(pady=20)

    button_frame = Frame(root)
    button_frame.pack(pady=10)

    Button(button_frame, text="Start", font=("Helvetica", 14), command=lambda: start_timer(root, time_label, data_label)).pack(side="left", padx=10)
    Button(button_frame, text="Pause", font=("Helvetica", 14), command=pause_timer).pack(side="left", padx=10)
    Button(button_frame, text="Stop", font=("Helvetica", 14), command=stop_timer).pack(side="left", padx=10)
    Button(button_frame, text="Reset", font=("Helvetica", 14), command=lambda: reset_timer(time_label, data_label)).pack(side="left", padx=10)

    custom_data_entry = Entry(root, font=("Helvetica", 14))
    custom_data_entry.pack(pady=10)
    Button(root, text="Add Custom Data", font=("Helvetica", 14), command=lambda: add_custom_data(custom_data_entry, data_label)).pack(pady=5)

    Button(root, text="Sort by Name", font=("Helvetica", 14), command=sort_by_name).pack(pady=5)
    Button(root, text="Sort by Performance", font=("Helvetica", 14), command=sort_by_performance).pack(pady=5)

    Button(root, text="Save Data", font=("Helvetica", 14), command=save_data).pack(pady=5)
    Button(root, text="Load Data", font=("Helvetica", 14), command=load_data).pack(pady=5)

    Button(root, text="Toggle Dark Mode", font=("Helvetica", 14), command=lambda: toggle_dark_mode(root, time_label, data_label)).pack(pady=5)

    update_title(root)
    root.mainloop()

