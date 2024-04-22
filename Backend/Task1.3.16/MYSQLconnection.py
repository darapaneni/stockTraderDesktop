import mysql.connector

class DBConnect:
    def __init__(self):
        self.connection = None

        
    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(user='root', password='MyNewPass',
                                                      host='127.0.0.1', database='productorder')
        except mysql.connector.Error as err:
            print(err)
        else:
            if self.connection.is_connected():
                print("Connected to database")

                
    def connect_to_db_with_dict(self):
        db_config = {
            'user': 'root',
            'password': 'MyNewPass',
            'host': '127.0.0.1',
            'database': 'productorder'}
        
        self.connection = mysql.connector.connect(**db_config)
        if self.connection.is_connected():
            print("Connected to database")            
         
 
    def connect_to_db_with_config_file(self):
        try:
            self.connection = mysql.connector.connect(option_files='my_conf.txt', option_groups=['connection_details'])
        except mysql.connector.Error as err:
            print(err)
        else:
            if self.connection.is_connected():
                print("Connected to database")

                
    def close_db_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("DB connection closed")
            
# Driver code            
if __name__ == "__main__":
    connector = DBConnect()
    connector.connect_to_db()
    connector.close_db_connection()

    connector.connect_to_db_with_dict()
    connector.close_db_connection()

    connector.connect_to_db_with_config_file()
    connector.close_db_connection()