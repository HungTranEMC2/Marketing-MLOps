import mysql.connector
import pandas as pd

def load_to_database(df, table_name, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            gender VARCHAR(255),
            age VARCHAR(255),
            occupation VARCHAR(255),
            city_category VARCHAR(255),
            stay_in_current_city_year VARCHAR(255),
            marital_status INT ,
            product_category_1 INT,
            product_category_2 INT,
            product_category_3 INT,
            purchase_amount INT
        )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO {table_name} (gender, age, occupation, city_category, stay_in_current_city_year, marital_status, product_category_1, product_category_2, product_category_3, purchase_amount)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_query, (row['gender'],row['age'],row['occupation'],row['city_category'],row['stay_in_current_city_year'],row['marital_status'],row['product_category_1'],row['product_category_2'],row['product_category_3'],row['purchase_amount']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
if __name__ == '__main__':
    df = pd.read_csv('data/marketing.csv')
    #print(df.columns)
    #Database configuration
    db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password': '12345678',
        'database': 'customer_purchase'
    }
    
    #Load data to MySQL
    load_to_database(df, 'customer_purchase',db_config)
    print('Loading Process is complete')
    