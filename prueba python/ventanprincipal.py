import sys
import tkinter as tk

root = tk.Tk()

menu_principal = tk.Menu()

menu_buscar_cancion = tk.Menu(menu_principal, tearoff=0)
menu_buscar_video_en_youtube = tk.Menu(menu_principal, tearoff=0)

menu_principal.add_cascade(label="Cancion",menu=menu_buscar_cancion)
menu_principal.add_cascade(label="Video",menu=menu_buscar_video_en_youtube)

menu_buscar_cancion.add_command(label="Buscar")
menu_buscar_cancion.add_separator()
menu_buscar_cancion.add_command(label="Salir",command=root.quit)

root.config(menu=menu_principal)

root.mainloop()