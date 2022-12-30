import pyodbc
server = 'HCL-02-29\SQLEXPRESS01'
database = 'newdatabase'
username = 'capstone1'
password = 'capstone@1234'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

#establishing the connection
class table:
    #this class is used to create new table
    def create_table(self):
       # try:except
        q1=cursor.execute('''use newdatabase''')
        q2= cursor.execute('''CREATE TABLE EMPLOYEE( 
        NAME varchar(20),
        EMP_ID int ,
        SALARY int, 
        PROJECT varchar(20) 
        )''')
        print("Table has been created in database")
        #q3=cursor.execute('''select *from create_table''')
        cnxn.commit()
#creating object to access class
obj_table=table()
#accesing the method using object
obj_table.create_table()
