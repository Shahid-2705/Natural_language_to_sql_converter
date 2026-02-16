from transformers import pipeline
import torch

class NLToSQL:
    def __init__(self):
        print("Loading Model... Please wait.")

        # Automatically use GPU if available
        device = 0 if torch.cuda.is_available() else -1

        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            device=device
        )

        if device == 0:
            print("Model Loaded Successfully on GPU.")
        else:
            print("Model Loaded Successfully on CPU.")

    def generate_sql(self, nl_query):
        """
        Converts a natural language query into an SQL query.
        """

        # Structured instruction prompt (important)
        prompt = f"""
You are an expert SQL assistant.
Task: Convert English questions into MySQL SELECT queries for the table 'employees'.

Table Schema:
employees(id, name, department, salary, city)

Rules:
1. ALWAYS use the table name 'employees'.
2. 'IT', 'Engineering', 'Sales', 'HR', 'Marketing' are values in the 'department' column.
3. Do NOT join with other tables.
4. Do NOT make up table names.

Examples:
Input: Show all employees
Output: SELECT * FROM employees;

Input: Show employees in Sales
Output: SELECT * FROM employees WHERE department = 'Sales';

Input: Show employees in IT with salary > 50000
Output: SELECT * FROM employees WHERE department = 'Engineering' AND salary > 50000;

Input: {nl_query}
Output:
"""

        output = self.generator(
            prompt,
            max_length=128,
            do_sample=False,     # makes output stable
            temperature=0.0
        )

        sql_query = output[0]['generated_text']

        # Cleanup
        sql_query = sql_query.replace("SQL:", "").strip()

        return sql_query

    def explain_sql(self, sql_query):
        """
        Explains the SQL query in natural language.
        """
        prompt = f"""
You are an AI that explains SQL queries.

Query: {sql_query}

Explanation:
"""
        output = self.generator(
            prompt,
            max_length=128,
            do_sample=False,
            temperature=0.0
        )
        
        explanation = output[0]['generated_text']
        return explanation
