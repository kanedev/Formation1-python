import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pythondb"
)
print(db)

cursor= db.cursor()

#cursor.execute('CREATE DATABASE pythondb')
#cursor.execute('CREATE TABLE contacts( id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),tel VARCHAR(25))')

query="INSERT INTO contacts(name,tel) VALUES(%s,%s)"
#values=('toto','101010101010')  # add one line
#cursor.execute(query,values)

"""
#  add many values
values =[
    ('toto1','101010101011'),
    ('toto2','101010101012'),
    ('toto3','101010101013'),
    ('toto4','101010101014')
]

cursor.executemany(query,values)

"""
#db.commit() 

#on récupère de la base de données les contacts 
query =" SELECT * FROM contacts"
cursor.execute(query)
contacts = cursor.fetchall()

"""
#Pour afficher tous les contacts
for contact in contacts : 
    print(contact)
"""


#Pour afficher juste les noms des contacts
for contact in contacts : 
    print(contact[1])

#on récupère de la base de données les contacts 
query2 =" SELECT * FROM contacts WHERE id = %s"
id=(4,)

cursor.execute(query2,id)
contact = cursor.fetchone() # On récupère juste un seule
print (contact)














print('Done')







