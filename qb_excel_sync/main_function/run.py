import os
import logging
import azure.functions as func
from app.services.qb_csv import parse_qb_csv
from app.services.excel_online import update_excel_status
from app.config import QB_EXPORT_PATH, GRAPH_CLIENT_ID, GRAPH_CLIENT_SECRET, GRAPH_TENANT_ID
from app.logging import logger
import requests

def get_graph_token():
    url = f"https://login.microsoftonline.com/{GRAPH_TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": GRAPH_CLIENT_ID,
        "client_secret": GRAPH_CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }
    resp = requests.post(url, data=data).json()
    return resp.get("access_token")

def main(mytimer: func.TimerRequest) -> None:
    logger.info("Azure Function QB → Excel sync triggered")

    updates = parse_qb_csv(QB_EXPORT_PATH)
    if not updates:
        logger.warning("No updates found")
        return

    token = get_graph_token()
    if not token:
        logger.error("Failed to obtain Graph API token")
        return

    update_excel_status(updates, token)
    logger.info("Azure Function sync completed")
