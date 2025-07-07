
# Database connection configuration

import sqlite3

def get_source_db_connection(db_path='source_data.db'):
    """
    Returns a connection to the source SQLite database.
    Change db_path to your actual database file if needed.
    """
    conn = sqlite3.connect(db_path)
    return conn

# Example usage (remove or comment out in production):
# conn = get_source_db_connection()
# cursor = conn.cursor()
# cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
# print(cursor.fetchall())
# conn.close()


#Load raw data from a SQLite database
def load_raw_data_from_db(conn, table_name):
    """
    Load raw data from a specified table in the SQLite database.
    
    Parameters:
    conn (sqlite3.Connection): Connection to the SQLite database.
    table_name (str): Name of the table to load data from.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    print(f"Loaded {len(df)} rows from table '{table_name}'")
    return df   

#Loa data from Google cloud storage using pandas
def load_data_from_gcs(bucket_name, file_name):     
    
#Loa data from Google cloud storage using kafka connectors
    """
    Load data from Google Cloud Storage using pandas.       