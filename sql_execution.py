import mysql.connector
import pandas as pd

def execute_mysql_query(sql):
    # MySQL connection parameters
    connection_params = {
        'user': 'sql6690576',
        'password': 'cmiie8J5uu',
        'host': 'sql6.freesqldatabase.com',
        'database': 'sql6690576',
        'port': 3306,
    }

    query = sql

    try:
        # Print the SQL query
        print("Executing SQL query:", query)

        # Establish a connection to MySQL
        conn = mysql.connector.connect(**connection_params)

        # Create a cursor object
        cur = conn.cursor()

        # Execute the query
        try:
            cur.execute(query)
        except mysql.connector.Error as e:
            print("MySQL Error:", e)
            return "MySQL error"

        # Fetch all results
        query_results = cur.fetchall()

        # Get column names from the cursor description
        column_names = [col[0] for col in cur.description]

        # Create a Pandas DataFrame
        data_frame = pd.DataFrame(query_results, columns=column_names)

        # Print the DataFrame
        print(data_frame)
        return data_frame

    except mysql.connector.Error as e:
        print("MySQL Error:", e)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the cursor and connection
        try:
            cur.close()
        except:
            pass

        try:
            conn.close()
        except:
            pass

# Example usage:
df = execute_mysql_query("SELECT * FROM Department_Information")
