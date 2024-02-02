from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

cart = []
#ARRAY FRUITS
fruits = ["Banana    $1.97", "Mango    $2.10", "Orange    $2.25", "Strawberry    $1.45", "Avocado    $2.23"]

#FUNCTION PICK FRUITS
def set_fruit():
    any_fruit = choose_fruits.get()
    dolar="$"
    label_total_bill["text"] = dolar, sum(cart)
    
#Banana   
    if any_fruit == "Banana    $1.97":
        amount = 1.97
        name ="Banana" 
        dolar="$"
        quant = int(type_quantity.get())
        
        if not quant == 0:
            total = quant * amount
            
            choose_fruits.delete(0,END)
            type_quantity.delete(0,END)
            lines = [total]
            for line in lines:
                cart.append(line)
                label_board["text"] = name, quant, "amounts:", dolar,cart
        else:
            messagebox.showwarning("", "type quantity!!")
            
#Mango         
    elif any_fruit == "Mango    $2.10":
        amount = 2.10
        name ="Mango"
        dolar="$"
        quant = int(type_quantity.get())
        
        if not quant == 0:
            total = quant * amount
            
            choose_fruits.delete(0,END)
            type_quantity.delete(0,END)
            
            lines = [total]
            for line in lines:
                cart.append(line)
                label_board["text"] = name, quant, "amounts:", dolar,cart
            
        else:
            messagebox.showwarning("", "type quantity!!")
            
#Avocado
    elif any_fruit == "Avocado    $2.23":
        amount = 2.23
        name = "Avocado"
        dolar="$"
        quant = int(type_quantity.get())
        
        if not quant == 0:
            total = quant * amount
            
            choose_fruits.delete(0,END)
            type_quantity.delete(0,END)
            lines = [total]
            for line in lines:
                cart.append(line)
                label_board["text"] = name, quant, "amounts"	
                
