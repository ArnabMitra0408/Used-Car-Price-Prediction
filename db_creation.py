import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="root"
)
mycursor = mydb.cursor()

# Check if the Car_Price database exists; create if it doesn't
mycursor.execute("SHOW DATABASES LIKE 'Car_Price'")
database_exists = mycursor.fetchone()

if not database_exists:
    mycursor.execute("CREATE DATABASE Car_Price")
    print("Database 'Car_Price' created.")
else:
    print("Database 'Car_Price' already exists.")

# Switch to the Car_Price database
mydb.database = "Car_Price"

# Check if Pipeline_LOGS table exists; create if it doesn't
mycursor.execute("SHOW TABLES LIKE 'Pipeline_LOGS'")
table_exists = mycursor.fetchone()

if not table_exists:
    mycursor.execute("""CREATE TABLE Pipeline_LOGS (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        LevelName VARCHAR(50),
        Message VARCHAR(1000),
        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    print("Table 'Pipeline_LOGS' created.")
else:
    print("Table 'Pipeline_LOGS' already exists.")

# Check if Application_LOGS table exists; create if it doesn't
mycursor.execute("SHOW TABLES LIKE 'Application_LOGS'")
table_exists = mycursor.fetchone()

if not table_exists:
    mycursor.execute("""CREATE TABLE Application_LOGS (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        LevelName VARCHAR(50),
        Message VARCHAR(1000),
        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    print("Table 'Application_LOGS' created.")
else:
    print("Table 'Application_LOGS' already exists.")

print("Database setup complete.")

# Close the cursor and connection
mycursor.close()
mydb.close()
