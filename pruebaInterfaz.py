import tkinter as tk

root = tk.Tk()
root.title("Interfaz con Tkinter")
root.geometry("400x400")

# Botones principales
button1 = tk.Button(root, text="Botón 1", bg="red", height=5, width=20)
button1.pack(side=tk.LEFT)

button2 = tk.Button(root, text="Botón 2", bg="blue", height=5, width=20)
button2.pack(side=tk.RIGHT)

# Cuadrícula de botones
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM)

button3 = tk.Button(frame, text="Botón 3", bg="yellow", height=5, width=10)
button3.grid(row=0, column=0)

button4 = tk.Button(frame, text="Botón 4", bg="green", height=5, width=10)
button4.grid(row=0, column=1)

button5 = tk.Button(frame, text="Botón 5", bg="orange", height=5, width=10)
button5.grid(row=1, column=0)

button6 = tk.Button(frame, text="Botón 6", bg="purple", height=5, width=10)
button6.grid(row=1, column=1)

root.mainloop()
