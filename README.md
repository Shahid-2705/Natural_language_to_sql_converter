# AI Natural Language to SQL Assistant

This project is a web-based AI assistant that converts natural language queries into SQL using the Hugging Face `flan-t5-small` model and executes them on a local MySQL database.

## Prerequisites

1.  **Python 3.8+**
2.  **XAMPP** (or any MySQL server)
3.  **Basic understanding of SQL**

## Installation

1.  **Clone/Download** the project.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This will install PyTorch and Transformers, which might take some time.*

## Database Setup

1.  Start **Apache** and **MySQL** in XAMPP control panel.
2.  Open **phpMyAdmin** (usually `http://localhost/phpmyadmin`).
3.  Import `database.sql` or copy-paste its content into the SQL execution tab.
    -   Creates `company_db` database.
    -   Creates `employees` table.
    -   Inserts sample data.

## Configuration

If your MySQL settings differ from the defaults (User: `root`, Password: ``), update `db_handler.py`:

```python
self.host = "localhost"
self.user = "root"
self.password = ""
self.database = "company_db"
```

## Running the Application

1.  Run the Flask app:
    ```bash
    python app.py
    ```
2.  Wait for the model to load (first time will download ~300MB).
3.  Open your browser and search: `http://127.0.0.1:5000`

## Usage Examples

Type queries like:
- "Show all employees"
- "Show employees from New York"
- "Who works in Engineering?"
- "Show employees with salary greater than 70000"

## Security

-   The application strictly allows **SELECT** queries only.
-   Attempts to DELETE, DROP, or INSERT will be blocked.

## Architecture

-   **Frontend**: HTML/CSS/JS (Fetch API)
-   **Backend**: Flask
-   **AI Model**: Google FLAN-T5 Small (via Hugging Face Transformers)
-   **Database**: MySQL
