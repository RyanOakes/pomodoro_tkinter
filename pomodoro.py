import tkinter

root = tkinter.Tk()

hi_there = tkinter.Label(
    root,
    text='Hi there!',
    background="red",
    foreground="white",
)
hi_there.pack(fill=tkinter.BOTH, expand=True)

my_name = tkinter.Label(root, text="Oakes")
my_name.pack()

root.mainloop()
