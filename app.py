import characterBuilder
import tkinter as tk


character = characterBuilder.Character()

print(character.Stats)

def gui():
    menu = tk.Tk()
    menu.title('Quest')
    # Making a Window
    tk.Label(menu, text='Name: ').grid(row=0)
    tk.Label(menu, text='Army Name: ').grid(row=1)
    tk.Label(menu, text='Body').grid(row=2)

    body_display = tk.Label(menu, text=0)
    body_display.grid(row=3)

    body_and_mind_scale = tk.Scale(menu, from_=6, to=24, orient=tk.HORIZONTAL, showvalue=False)
    body_and_mind_scale.grid(row=2, column=1)

    tk.Label(menu, text='Mind').grid(row=2, column=2)
    mind_display = tk.Label(menu, text=0)
    mind_display.grid(row=3, column=2)

    e1 = tk.Entry(menu)
    e2 = tk.Entry(menu)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    menu.mainloop()


gui()