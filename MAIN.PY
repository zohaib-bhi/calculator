from tkinter import *
root = Tk()
root.geometry("312x324")

# root.maxsize(312,324)
# root.minsize(312,324)
root.title("zabi")


# this is used to prevent from resizing the window

root.config(bg= "white")

root.resizable(0, 0)
input_text = StringVar()

# bd means border width


def btn_click(item):
    global expression
    expression = expression +(item)
    input_text.set(expression)
    
def btn_clear():
    global expression
    expression="" 
    input_text.set("") 
    
def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)    
expression = ""


f1 = Frame(root, width=312, height=50, bd=0, highlightbackground="black",
           highlightcolor="black", highlightthickness=2)
f1.pack(side=TOP)
input_field = Entry(f1, font=('arial', 18, 'bold'),
                    textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)





f2 = Frame(root, width=312, height=272.5, bg="grey")
f2.pack()


# def btn_click(item):
#     global expression
#     expression = expression + str(item)
#     input_text.set(expression)
    
# def btn_clear():
#     global expression
#     expression="" 
#     input_text.set("") 
    
    
    
# now we are making buttons




clear = Button(f2, text = "c", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear())
                                                                                                                                  
                                                                                                                                    

clear.grid(row = 0,column=0,columnspan=3, padx = 1, pady = 1)


divide = Button(f2, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/"))
                                                                                                                                  
                                                                                                                                    

divide.grid(row = 0, column = 3, padx = 1, pady = 1)




seven = Button(f2, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("7"))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)                                                                                                                        
                                                                                                    

eight = Button(f2, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("8"))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)                                                                                                                        
                                                                                                   

nine= Button(f2, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("9"))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)                                                                                                                        
                                                                                                    

multiply= Button(f2, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)                                                                                                                        
  
four= Button(f2, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("4"))
four.grid(row = 2, column = 0, padx = 1, pady = 1)                                                                                                                        
  
  
five= Button(f2, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("5"))
five.grid(row = 2, column = 1, padx = 1, pady = 1)                                                                                                                        
 
six= Button(f2, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("6"))
six.grid(row = 2, column = 2, padx = 1, pady = 1)                                                                                                                        
 
 
manas= Button(f2, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-"))
manas.grid(row = 2, column = 3, padx = 1, pady = 1)                                                                                                                        
 
 
one= Button(f2, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("1"))
one.grid(row = 3, column = 0, padx = 1, pady = 1)   


two= Button(f2, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("2"))
two.grid(row = 3, column = 1, padx = 1, pady = 1)  


three= Button(f2, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("3"))
three.grid(row = 3, column = 2, padx = 1, pady = 1)                                                                                                                        
                                                       
 
add= Button(f2, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+"))
add.grid(row = 3, column = 3, padx = 1, pady = 1)  


zero= Button(f2, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("0"))
zero.grid(row =4 , column = 0,  columnspan=2 ,padx = 1, pady = 1)       


dot= Button(f2, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("."))
dot.grid(row =4 , column = 2, padx = 1, pady = 1)       
                                                                                                                                          
                                                                                                                                           
                                                                                                                                                                                                                     
equll= Button(f2, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal())
equll.grid(row = 4, column = 3, padx = 1, pady = 1)                                                                                                                        

                                                                                                                                                     
                                                                                                                                                                         

root .mainloop()
