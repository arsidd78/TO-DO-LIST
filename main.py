from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time
import logging

# Creating our Window:
root = Tk()
root.iconbitmap(r'C:\Users\7seas\Downloads\list_80426.ico')
root.title('To-DO LIST')
root.geometry('700x600')

#                 Creating a background for our Application:

# Creating a Background Picture:
bg=ImageTk.PhotoImage(Image.open(r'C:\Users\7seas\Downloads\ToDoBG.jpeg'))
background=Label(root,image=bg)
background.place(x=0,y=0,relwidth=1,relheight=1)


# Connecting to our List Data base:

db=r'E:\PYTHON\PROJECTS\TO-DO_LIST\Tasks_List.db' # Path to List Db
connect=sqlite3.connect(db)
c=connect.cursor()


#Creating Functionality of buttons:


def ADD():
    
    connect=sqlite3.connect(db)
    c=connect.cursor()
    c.execute('INSERT INTO Task_List VALUES(:Task,:Date_added,:completed_Tasks)',
              {
                  'Task':add.get(),
                  'Date_added':time.asctime(),
                  'completed_Tasks':'Not Completed'

              })
    connect.commit()
    connect.close()
    # Creating logs:
    logging.basicConfig(filename=r'E:\PYTHON\PROJECTS\TO-DO_LIST\To-do-list_logs.log',filemode='a',format='%(asctime)s %(message)s')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info('The user has added a task')

    add.delete(0,END) # As soon as add button is clicked the text written in the box will be deleted.




# Functionality of Remove button:
def REMOVE(oid):
    
    
    connect=sqlite3.connect(db)
    
    c=connect.cursor()
    c.execute('DELETE FROM Task_List WHERE oid='+str(oid))

    logging.basicConfig(filename=r'E:\PYTHON\PROJECTS\TO-DO_LIST\To-do-list_logs.log',filemode='a',format='%(asctime)s %(message)s')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info(f'Task:{record[0]} was removed')

    connect.commit()
    connect.close()
    
    
    
   

    
    TASKS()

    

    
# Functionality of Show all button:
def SHOW():
    
    global show_window
    global recorde
    connect=sqlite3.connect(db)
    c=connect.cursor()
    c.execute('SELECT *,OID FROM Task_List')
    records=c.fetchall()
    data=''
    show_window=Tk()
    for recorde in records:
        data+= str(record[0])+' \n '+f'Time Added:{record[1]}'+' \n '+f'Status: {record[2]}'   +'\n'+'\n'
        
        
        
    
    show_window.title('All Tasks')
    show_window.iconbitmap(r'C:\Users\7seas\Downloads\list_80426.ico')
    show_window.geometry('600x600')
    Label(show_window,text=data,fg='black',bg='lightblue').grid(row=0,column=0,columnspan=3,sticky='W')
    
        
    connect.commit()
    connect.close()

# Creating functionality of edit button:    
def UPDATE(oid):
    global edit_entry
    Label(root,text='Edit your Task:',bg='lightblue', fg='black',padx=20,width=10).grid(row=2,column=0)
    edit_entry=Entry(root,width=50,bg='white',fg='black',border=5)
    edit_entry.grid(row=2,column=1)
    save_button=Button(root,text='Save',bg='darkblue',fg='white',command=lambda oid=oid: EDIT(oid),width=7)
    save_button.grid(row=2,column=2,padx=15)
    connect=sqlite3.connect(db)
    c=connect.cursor()
    c.execute('SELECT Task FROM Task_List WHERE OID='+str(oid))
    task=c.fetchmany()

    edit_entry.insert(0,task)
  


    connect.commit()
    connect.close()
    edit_entry.delete(0,END)

def EDIT(oid):
    
    connect=sqlite3.connect(db)
    c=connect.cursor()
    c.execute('''UPDATE Task_List SET
              Task=:task,
              Date_added=:time,
              CompletedTask=:completed
              
              WHERE oid=:OID''',
            {'task':edit_entry.get(),
             'time':time.asctime(),
             'completed':record[2],
             'OID':oid



            })
    
    connect.commit()
    connect.close()
    edit_entry.delete(0,END)
    TASKS()    



def TASKS():
    
        
        global r    
        global record
        global task_label
        global remove_button
        global edit_entry
       
        global add
        global add_button
        
        # Clearing previous task labels and buttons
        for widget in root.winfo_children():
            if isinstance(widget, (Label, Button)):
                widget.destroy()
      
        background = Label(root, image=bg)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        connect = sqlite3.connect(db)
        c = connect.cursor()
        c.execute('SELECT *,OID FROM Task_List')
        records = c.fetchall()  # This is the list containing all the task their date and status.
        r = 5

        
        Label(root, text='TASK :', bg='lightblue', fg='black',padx=20,width=10).grid(row=0, column=0,sticky='W')

        

        
        add=Entry(root,width=50,bg='white',fg='black',border=5)
        add.insert(0,'Type your task here ')
        add.grid(row=0,column=1,padx=10)
        add_button=Button(root,text='Add',bg='darkblue',fg='white',command=ADD,width=7)
        add_button.grid(row=0,column=2,padx=15)

        
        
        show_all_task=Button(root,text='Show All Task',bg='darkblue',fg='white',command=TASKS,width=25)
        show_all_task.grid(row=4,column=1)

        for record in records:
            task_label = Label(root, text=record[0], fg='black',bg='lightblue')
            task_label.grid(row=r, column=0, sticky='W')

            

            remove_button = Button(root, text='Remove', fg='white', bg='darkblue', width=7, command=lambda oid=record[3]: REMOVE(oid))
            remove_button.grid(row=r, column=2, padx=18)

            edit_button=Button(root,text='Edit',bg='darkblue',fg='white',command=lambda oid=record[3]:UPDATE(oid))
            edit_button.grid(row=r,column=3,padx=18)

            r += 1

        connect.commit()
        connect.close()

         
# Creating Label:
Label(root, text='TASK :', bg='lightblue', fg='black',padx=20,width=10).grid(row=0, column=0,sticky='W')



# Creating Entries:
add=Entry(root,width=50,bg='white',fg='black',border=5)
add.insert(0,'Type your task here ')
add.grid(row=0,column=1,padx=10)




# Creating Buttons:
add_button=Button(root,text='Add',bg='darkblue',fg='white',command=ADD,width=7)
add_button.grid(row=0,column=2,padx=15)


show_all_task=Button(root,text='Show Tasks',bg='darkblue',fg='white',command=TASKS,width=25)
show_all_task.grid(row=4,column=1)


# Closing and commiting into our Task list Db:

connect.commit()
connect.close()

root.mainloop()
