import os

# QuickBooks CSV export location
QB_EXPORT_PATH = os.getenv("QB_EXPORT_PATH", "exports/invoices.csv")

# Microsoft Graph / OneDrive Excel
GRAPH_CLIENT_ID = os.getenv("GRAPH_CLIENT_ID")
GRAPH_CLIENT_SECRET = os.getenv("GRAPH_CLIENT_SECRET")
GRAPH_TENANT_ID = os.getenv("GRAPH_TENANT_ID")

EXCEL_FILE_ID = os.getenv("EXCEL_FILE_ID")
EXCEL_TABLE_NAME = os.getenv("EXCEL_TABLE_NAME")

# Excel column names
JOB_CODE_COLUMN = "Job Code"
STATUS_COLUMN = "Status"
BALANCE_COLUMN = "Amount" 