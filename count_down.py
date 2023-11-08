import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk

def update_label(label, end_time, task):
    now = datetime.now()
    if end_time > now:
        time_left = end_time - now
        time_left_str = f"{task}{str(time_left).split('.')[0]} - ({end_time.strftime('%d.%m.%y')})"
    else:
        time_left_str = f"{task}Time's up! - ({end_time.strftime('%d.%m.%y')})"

    label.config(text=time_left_str)

    if end_time - now < timedelta(days=1):
        label.config(fg="red")
    else:
        label.config(fg="white")

    label.after(1000, update_label, label, end_time, task)

def run_countdown_gui(deadlines):
    root = tk.Tk()
    root.title("Deadline Countdown")
    root.resizable(False, False)
    root.overrideredirect(True)
    root.geometry("600x400")

    # Custom title bar
    title_bar = tk.Frame(root, bg='black', relief='raised', bd=2)
    title_bar.pack(fill=tk.X)

    # Close button on the title bar
    close_button = tk.Button(title_bar, text='X', command=root.destroy, bg='red', fg='white', bd=0)
    close_button.pack(side=tk.RIGHT)

    # Title label on the title bar
    title_label = tk.Label(title_bar, text='Deadline Countdown', bg='black', fg='white')
    title_label.pack(side=tk.LEFT, padx=(10, 0))

    # Bind the title bar motion to the drag_window function
    def drag_window(event):
        root.geometry(f"+{event.x_root - root._offset_x}+{event.y_root - root._offset_y}")

    def click_window(event):
        root._offset_x = event.x
        root._offset_y = event.y

    title_bar.bind('<Button-1>', click_window)
    title_bar.bind('<B1-Motion>', drag_window)

    # Load and resize the image
    image_path = r"DALL·E 2023-11-08 08.36.38 - A daunting image that conveys urgency and the importance of studying for exams. The scene includes a large, looming clock with hands approaching a dea.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((600, 400), Image.LANCZOS)
    image = ImageTk.PhotoImage(resized_image)

    image_label = tk.Label(root, image=image)
    image_label.pack()

    # Create a transparent overlay Frame on the bottom half of the image
    overlay = tk.Frame(root, bg='black')
    overlay.place(relx=0.5, rely=0.75, anchor='center', relwidth=1.0, relheight=0.5)

    label_font = ("Helvetica", 15, "bold")

    # Display all deadlines
    for task, end_time in deadlines.items():
        frame = tk.Frame(overlay, bg='black', pady=5)
        frame.pack(fill='x')

        countdown_label = tk.Label(frame, font=label_font, bg='black', fg='white')
        countdown_label.pack(fill='x')

        update_label(countdown_label, end_time, task)

    root.mainloop()

deadlines = {
    "Webteknologi-prosjekt       |    ": datetime(2023, 11, 16, 23, 59),
    "Exphil flervalg    |    ": datetime(2023, 11, 25, 15, 0),
    "Webteknologi eksamen    |    ": datetime(2023, 11, 29, 9, 0),
    "Matte A eksamen    |    ": datetime(2023, 12, 7, 9, 0),
    "ITGK eksamen    |    ": datetime(2023, 12, 11, 9, 0),
    "Exphil oppgave    |    ": datetime(2023, 12, 18, 15, 0),
}

run_countdown_gui(deadlines)
