import mysql.connector
from mysql.connector import Error

class DBHandler:
    def __init__(self):
        # Configuration for XAMPP MySQL (default user: root, no password)
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "company_db"

    def connect(self):
        """Establishes a connection to the database."""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def validate_sql(self, sql_query):
        """
        Validates the SQL query to ensure safety.
        Only SELECT statements are allowed.
        """
        if not sql_query:
            return False, "Empty query."
        
        # Simple validation: Check if it starts with SELECT
        normalized_query = sql_query.strip().upper()
        if not normalized_query.startswith("SELECT"):
            return False, "Security Alert: Only SELECT queries are executed."
        
        forbidden_keywords = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE"]
        for keyword in forbidden_keywords:
            if keyword in normalized_query:
                return False, f"Security Alert: '{keyword}' statements are not allowed."

        return True, "Valid SQL."

    def execute_query(self, sql_query):
        """
        Executes a safe SQL query and returns the results.
        """
        is_valid, message = self.validate_sql(sql_query)
        if not is_valid:
            return None, message

        connection = self.connect()
        if not connection:
            return None, "Database connection failed."

        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            
            # Fetch all results
            result = cursor.fetchall()
            
            # Get column names
            column_names = [i[0] for i in cursor.description] if cursor.description else []
            
            cursor.close()
            connection.close()
            
            return {"columns": column_names, "data": result}, None

        except Error as e:
            if connection.is_connected():
                connection.close()
            return None, f"SQL Execution Error: {e}"
