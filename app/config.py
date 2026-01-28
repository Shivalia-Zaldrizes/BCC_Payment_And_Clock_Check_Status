import os

# QuickBooks CSV export location
#QB_EXPORT_PATH = os.getenv("QB_EXPORT_PATH", "exports/invoices.csv")

# Microsoft Graph / OneDrive Excel
#GRAPH_CLIENT_ID = os.getenv("GRAPH_CLIENT_ID")
#GRAPH_CLIENT_SECRET = os.getenv("GRAPH_CLIENT_SECRET")
#GRAPH_TENANT_ID = os.getenv("GRAPH_TENANT_ID")

#EXCEL_FILE_ID = os.getenv("EXCEL_FILE_ID")
#EXCEL_TABLE_NAME = os.getenv("EXCEL_TABLE_NAME")

# Excel column names
#JOB_CODE_COLUMN = "Job Code"
#STATUS_COLUMN = "Status"
#BALANCE_COLUMN = "Amount" 



#TESTING LOCAL FILES


# QuickBooks CSV export location
# QuickBooks CSV input
QB_EXPORT_PATH = os.path.join(os.getcwd(), "Import Files", "CSV", "Employee Name,Work Date,Week Ending.csv")

# Local Excel test file
HOURS_EXCEL_PATH = os.path.join(os.getcwd(), "Import Files", "Excel", "Field-Daily-Paychex TEST.xlsx")

# Output Excel file
OUTPUT_EXCEL_PATH = os.path.join(os.getcwd(), "Export Files", "Excel", "processed_output.xlsx")

# Toggle Graph / OneDrive integration
USE_GRAPH = False

# Path to store logs
LOG_DIR = os.path.join(os.getcwd(), "logs")  # creates a 'logs' folder in your project root
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")  # logs/app.log