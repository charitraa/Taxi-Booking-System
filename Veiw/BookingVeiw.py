import tkinter as tk
from tkinter import messagebox


class Booking(tk.Tk):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.title("Booking Page")

        # Label and Entry for Pickup Location
        self.pickup_label = tk.Label(master, text="Pickup Location:")
        self.pickup_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.pickup_entry = tk.Entry(master)
        self.pickup_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label and Entry for Drop-off Location
        self.dropoff_label = tk.Label(master, text="Drop-off Location:")
        self.dropoff_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.dropoff_entry = tk.Entry(master)
        self.dropoff_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Label and Entry for Date
        self.date_label = tk.Label(master, text="Date:")
        self.date_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Label and Entry for Time
        self.time_label = tk.Label(master, text="Time:")
        self.time_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.time_entry = tk.Entry(master)
        self.time_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Submit Button
        self.submit_button = tk.Button(master, text="Book Ride", command=self.book_ride)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def book_ride(self):
        pickup_location = self.pickup_entry.get()
        dropoff_location = self.dropoff_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        # Here, you can implement the logic to book the ride based on the entered information.
        # For simplicity, let's just display the information for now.
        ride_info = f"Pickup: {pickup_location}\nDrop-off: {dropoff_location}\nDate: {date}\nTime: {time}"

        messagebox.showinfo("Ride Booked", ride_info)

if __name__ == "__main__":
    app = Booking()
    app.mainloop()
