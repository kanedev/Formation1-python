from tkinter import *
 
import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pythonprojetcontacts"
)
print(db)

cursor= db.cursor()

# create blank root
root = Tk()
root.title("my Contacts App")
root.geometry('500x500')

def say_hello():
    print('hello tkinter')
  #  buffer = field.get()
  #  lbl2.config(text=buffer)
    print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())
    resutat.insert(END,nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())



def addContact():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())
      resultat.insert(END,nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())
 
def showAllContacts():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())

def findContact():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())

def updateContact():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())      

def deleteContact():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())

def quitApp():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())

# Champ : Nom
labelNom = Label(root, text="Nom :")
labelNom.grid(row=1, column=1)

nomVar = StringVar()
nom = Entry(root, textvariable= nomVar)
nom.grid(row=1,column=2)

# Champ : Prénom
labelPrenom = Label(root, text="Prénom :")
labelPrenom.grid(row=2, column=1)

prenomVar = StringVar()
prenom = Entry(root,  textvariable= prenomVar)
prenom.grid(row=2,column=2)

# Champ : Téléphone
labelTelephone = Label(root, text="Téléphone :")
labelTelephone.grid(row=3, column=1)

telephoneVar = StringVar()
telephone = Entry(root,  textvariable= telephoneVar)
telephone.grid(row=3,column=2)


# Champ : resultat
labelResultat = Label(root ,text="Résultat :")
labelResultat.grid(row=6, column=1)

resultat = Text(root, height=10, width=40)
resultat.grid(row=7,column=2)

buttonaddContact = Button(root,text='Ajouter', command=addContact)
buttonaddContact.grid(row=2,column=3)

buttonshowAllContacts = Button(root,text='Tous les contacts', command=showAllContacts)
buttonshowAllContacts.grid(row=3,column=3)

buttonfindContact = Button(root,text='Rechercher',bg="black", command=findContact)
buttonfindContact.grid(row=4,column=3)

buttonupdateContact = Button(root,text='Modifier', command=updateContact)
buttonupdateContact.grid(row=5,column=3)

buttondeleteContact = Button(root,text='Supprimer', command=deleteContact)
buttondeleteContact.grid(row=6,column=3)

buttonquitApp = Button(root,text='Quitter', command=quitApp)
buttonquitApp.grid(row=7,column=3)


# if you forget to call the mainloop function, nothing will appear to the user
root.mainloop()

