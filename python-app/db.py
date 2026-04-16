import pyodbc

SERVER = "(localdb)\\MSSQLLocalDB"
DATABASE = "TestDB"
CONNECTION_STRING = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={SERVER};"
    f"Database={DATABASE};"
    "Trusted_Connection=yes;"
)

TABLES = ["Users", "Products", "Orders", "OrderItems"]


def get_connection():
    return pyodbc.connect(CONNECTION_STRING)


def get_products():
    """Return list of (ProductID, Name, Price) from Products table."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, Name, Price FROM dbo.Products ORDER BY Name")
        return cursor.fetchall()


def get_table_rows(table):
    """Return (columns, rows) for a given table name."""
    if table not in TABLES:
        raise ValueError(f"Unknown table: {table}")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT TOP 50 * FROM dbo.{table}")
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    return columns, rows
