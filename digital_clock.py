import tkinter as tk
import tkinter.ttk as ttk
from time import strftime

class DigitalClockApp():
	def __init__(self, root):
		self.root = root
		self.root.title('Digital Clock')
		self.clock_label = ttk.Label(self.root, font=("ds-digital", 80),
										background="black", foreground="red", width=10, anchor="center")
		self.clock_label.pack(anchor="center")

	def timer(self):
		self.str_time = strftime("%I:%M:%S %p")
		self.clock_label.config(text=self.str_time)
		self.clock_label.after(1000, self.timer)


if __name__ == '__main__':
	window = tk.Tk()
	clock = DigitalClockApp(window)
	clock.timer()
	window.mainloop()

