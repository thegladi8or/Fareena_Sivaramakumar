import mysql.connector
from model import  Pupper
from model import Breed

connectionToDB = mysql.connector.connect(user='root', password='rootroot',
                              host='localhost',
                              database='pupper')

mycursor = connectionToDB.cursor()

pupperOne = Pupper("Socks", 'F', 45.0, 25.0, "Grey and WHite", "20180908", 3)
breedOne = Breed ("Joker", "Alert","Shiny")


#writing to table breed
sqlInsert = "INSERT INTO breed (name,temperament,coat) VALUES (%s, %s, %s)"
valInsert = (breedOne.name,breedOne.temperament,breedOne.coat)
mycursor.execute(sqlInsert, valInsert)

#writing to table pupper
sqlInsert = """INSERT INTO pupper (name,sex,weight,height,color,date_of_birth,breed_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
valInsert = (pupperOne.name,pupperOne.sex,pupperOne.weight,pupperOne.height ,pupperOne.color,pupperOne.date_of_birth,pupperOne.breed_id)
mycursor.execute(sqlInsert,valInsert) 

#reading all rows from table pupper
mycursor.execute("Select * from pupper")
result = mycursor.fetchall()
for items in result:
    print(items)
    
#reading all rows from table breed
mycursor.execute("Select * from breed")
result = mycursor.fetchall()
for items in result:
    print(items)
    
#Search by breedID    
txt = input("Enter the breed ID: ")   
mycursor.execute("Select * from breed where ID=" + txt)
print(mycursor.fetchone())

#Search by pupperID    
txt = input("Enter the Pupper ID: ")   
mycursor.execute("Select * from pupper where ID=" + txt)
print(mycursor.fetchone())
