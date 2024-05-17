from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "52.2.83.96"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_employees2"  

# Get all employees
@app.get("/employees2")
def get_employees():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employees2")
    result = cursor.fetchall()
    mydb.close()
    return {"employees2": result}

# Get an employee by ID
@app.get("/employees2/{id}")
def get_employee(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM employees2 WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"employee2": result}

# Add a new employee
@app.post("/employees2")
def add_employee(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    name = item.name
    age = item.age
    cursor = mydb.cursor()
    sql = "INSERT INTO employees2 (name, age) VALUES (%s, %s)"
    val = (name, age)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Employee added successfully"}

# Modify an employee
@app.put("/employees2/{id}")
def update_employee(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    name = item.name
    age = item.age
    cursor = mydb.cursor()
    sql = "UPDATE employees2 set name=%s, age=%s where id=%s"
    val = (name, age, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Employee modified successfully"}

# Delete an employee by ID
@app.delete("/employees2/{id}")
def delete_employee(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM employees2 WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Employee deleted successfully"}