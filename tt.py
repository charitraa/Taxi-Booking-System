import tkinter as tk

def center_window(window, width, height):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate x and y coordinates for the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's position
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create a top-level window
root = tk.Tk()
root.title("Centered Window")

# Set the size of the window
window_width = 400
window_height = 300
center_window(root, window_width, window_height)

# Add content to the window
label = tk.Label(root, text="Hello, Centered Window!")
label.pack(padx=20, pady=30)

# Run the Tkinter event loop
root.mainloop()
