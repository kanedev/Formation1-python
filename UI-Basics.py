from tkinter import *

# create blank root
root = Tk()
root.title("my first app in python")
root.geometry('400x400')

def say_hello():
    print('hello tkinter')
  #  buffer = field.get()
  #  lbl2.config(text=buffer)
    print(nomVar.get() + " " + prenomVar.get())
    resutat.insert(END,nomVar.get() + " " + prenomVar.get())






# Champ : Nom
labelNom = Label(root, text="Votre nom :")
labelNom.grid(row=1, column=1)

nomVar = StringVar()
nom = Entry(root, textvariable= nomVar)
nom.grid(row=1,column=2)

# Champ : Prénom
labelPrenom = Label(root, text="Votre prénom :")
labelPrenom.grid(row=2, column=1)

prenomVar = StringVar()
prenom = Entry(root,  textvariable= prenomVar)
prenom.grid(row=2,column=2)

# Champ : resultat
resutat = Text(root, height=1, width=10)
resutat.grid(row=3,column=2)




button = Button(root,text='Envoyer', command=say_hello)
button.grid(row=4,column=2)


# if you forget to call the mainloop function, nothing will appear to the user
root.mainloop()

