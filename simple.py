# 1 #################### First basic window & "**kwargs"

import tkinter

window = tkinter.Tk()
window.title("I1 - Cours n°6")
window.geometry('300x200')
window.resizable(False, False)

# Instance of "Label" (associated variable "window")

lbl = tkinter.Label(window, text="Coucou !", fg="white", bg="red")
lbl.pack(side="top",fill="both",expand=True)

# # "**kwargs" : same code but with parameters in dicts
# params_label = {"text":"HELLO...", "fg":"green", "bg":"yellow"}
# params_pack = {"side":"bottom","fill":"none","expand":False}
# #
# lbl = tkinter.Label(window, **params_label)
# lbl.pack(**params_pack)

window.mainloop()