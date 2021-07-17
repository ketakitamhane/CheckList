from tkinter import *
from tkinter import messagebox
root=Tk()
#root properties
root.title("My Checklist App")#root title
root.geometry("325x325")#window size
root.resizable(0,0)#resizing
root.iconbitmap("logo.ico")#logo

#setting up general fonts and colors
myfont = ("Times New Roman",10)
rootColor = "#3b5998"
buttonColor =  "#f7f7f7"
root.config(bg= rootColor)

#functiondefinition
#fn to add text in listbox when Add Item is clicked
def addItem():
    if listEntry.get() == "":
        #message popup
        messagebox.showinfo("Illegal Entry in list","cannot enter blank item in list box")
    else:
        listBox.insert(END,listEntry.get())
        listEntry.delete(0,END)
        
#fn to remove an item        
def removeItem():
    listBox.delete(ANCHOR)
    
#fn to clear entire list    
def clear():
    listBox.delete(0,END)
   
#fn to save entire list into external txt file  
def save():
    #we will open a file (in write mode), and write the required contents into it.
    #with checklist.txt opened in write mode named as f for your future reference
    with open("checklist.txt","w") as f:
        listTuple = listBox.get(0,END)
        for items in listTuple:
            f.write(items+"\n")
            
#function to recall stored elements in txt file
def openList():
    try:
        with open("checklist.txt","r") as f:
            for line in f:
                listBox.insert(END,line)
    except:
        pass
    
        
   

    

        
    
        

#create layout
#Create Frames
inputFrame = Frame(root, bg=rootColor)
outputFrame = Frame(root, bg=rootColor)
buttonsFrame = Frame(root, bg=rootColor)
inputFrame.pack()
outputFrame.pack()
buttonsFrame.pack()
#Create layout of element in input frame - entrywidget, add button
listEntry = Entry(inputFrame,width = 23,borderwidth=3,font=myfont)
listAddButton = Button(inputFrame,text="Add Item",borderwidth=3,font=myfont,bg=buttonColor,command=addItem)

listEntry.grid(row=0,column=0,padx=5,pady=5)
listAddButton.grid(row=0,column=1,padx=5,pady=5,)

#create layout of elements in output frame
scrollbar = Scrollbar(outputFrame)
listBox = Listbox(outputFrame,height=13,width=37,borderwidth=3,font=myfont,yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)
listBox.grid(row=0,column=0)
scrollbar.grid(row=0,column=1,sticky="NS")
#create layout of element in buttons frame
listRemoveButton = Button(buttonsFrame,text="Remove Item",borderwidth=2,font=myfont,bg=buttonColor,command=removeItem)
listClearButton = Button(buttonsFrame,text="Clear List",borderwidth=2,font=myfont,bg=buttonColor,command=clear)
SaveButton = Button(buttonsFrame,text="Save",borderwidth=2,font=myfont,bg=buttonColor,command=save)
QuitButton = Button(buttonsFrame,text="Exit",borderwidth=2,font=myfont,bg=buttonColor,command=root.destroy)

listRemoveButton.grid(row=0,column=0,padx=2,pady=10)
listClearButton.grid(row=0,column=1,padx=2,pady=10,ipadx=5)
SaveButton.grid(row=0,column=2,padx=2,pady=10,ipadx=15)
QuitButton.grid(row=0,column=3,padx=2,pady=10,ipadx=15)








#mainloop
openList()
root.mainloop()
