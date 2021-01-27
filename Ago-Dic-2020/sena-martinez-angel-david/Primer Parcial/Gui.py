from tkinter import * 
from tkinter.ttk import *
  
# creando ventana tkinter 
root = Tk() 
  
# Agregando herramientas a la ventana
Label(root, text = 'PuntosExtra', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
  
# Insertando la imagen de login
foto = PhotoImage(file = r"C:\Users\david\OneDrive\Imágenes\login.png") 
  
Button(root, text = 'Click Me !', image = foto).pack(side = TOP) 
  
mainloop() 