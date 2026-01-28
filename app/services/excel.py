import requests
from app.config import EXCEL_FILE_ID, EXCEL_TABLE_NAME
from app.logging import logger

def update_excel_status(updates: list, graph_token: str):
    """Update Status column in Excel based on JobCode"""
    if not updates:
        logger.info("No updates to apply")
        return

    base_url = f"https://graph.microsoft.com/v1.0/me/drive/items/{EXCEL_FILE_ID}/workbook/tables/{EXCEL_TABLE_NAME}/rows"
    headers = {"Authorization": f"Bearer {graph_token}", "Content-Type": "application/json"}

    try:
        rows = requests.get(base_url, headers=headers).json()["value"]
    except Exception as e:
        logger.exception(f"Failed to fetch Excel rows: {e}")
        return

    # Default: assume JobCode column = 0, Status column = 1
    job_col_idx = 0
    status_col_idx = 1

    updates_applied = 0
    for row in rows:
        row_values = row["values"][0]
        for update in updates:
            if row_values[job_col_idx] == update.job_code:
                row_values[status_col_idx] = update.status
                try:
                    update_url = f"{base_url}/{row['id']}"
                    requests.patch(update_url, json={"values": [row_values]}, headers=headers)
                    updates_applied += 1
                except Exception as e:
                    logger.exception(f"Failed to update row for JobCode {update.job_code}: {e}")

    logger.info(f"Applied {updates_applied}/{len(updates)} updates to Excel")
