from tkinter import *
from tkinter import scrolledtext
 
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
root.geometry('600x400')


def addContact():
      print(nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())
      # resultat.insert(END,nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get()+ "\n")

      resultat.insert(INSERT,nomVar.get() + " " + prenomVar.get()+ " " + telephoneVar.get())

      query="INSERT INTO contacts(nom,prenom,telephone) VALUES(%s,%s,%s)"
      #values=('toto','tata','101010101010')
      values=(nomVar.get(),prenomVar.get(),telephoneVar.get())  # add one line
      cursor.execute(query,values)
      id_contact = cursor.lastrowid
      print(id_contact)
      db.commit() 
 
def showAllContacts():
     query =" SELECT * FROM contacts"
     cursor.execute(query)
     contacts = cursor.fetchall()
  
     #Pour afficher tous les contacts
     for contact in contacts : 
        resultat.insert(INSERT,contact)
        resultat.insert(INSERT,"\n")

def findContact():
      query =" SELECT * FROM contacts WHERE (nom LIKE %s OR prenom LIKE %s OR telephone LIKE %s )"
      # VALUES(%s,%s,%s)
      #cursor.execute(query,values)
      # \' nomVar.get() \' OR prenom LIKE \' prenomVar.get() \' OR telephone LIKE \' telephoneVar.get() \'
      values=(rechercheVar.get(),rechercheVar.get(),rechercheVar.get()) 
      cursor.execute(query,values)
      contacts = cursor.fetchall()
      print(contacts)
      #Pour afficher tous les contacts
      for contact in contacts : 
          resultat.insert(INSERT,contact)
          resultat.insert(INSERT,"\n")



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

# Champ : Recherche
labelRecherche = Label(root, text="Rechercher :")
labelRecherche.grid(row=4, column=1)

rechercheVar = StringVar()
recherche = Entry(root,  textvariable= rechercheVar)
recherche.grid(row=4,column=2)

# Champ : resultat
labelResultat = Label(root ,text="Résultat :")
labelResultat.grid(row=6, column=1)

# resultat = Text(root, height=10, width=40)
# resultat.grid(row=7,column=2)
#resultat = scrolledtext.ScrolledText(root, height=10, width=40)

resultat = Listbox(root, height=10, width=40)
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

