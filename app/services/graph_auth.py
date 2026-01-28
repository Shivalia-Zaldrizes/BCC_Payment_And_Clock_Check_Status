import requests
from app.config import GRAPH_TENANT_ID, GRAPH_CLIENT_ID, GRAPH_CLIENT_SECRET
from app.logging import logger

def get_graph_token() -> str | None:
    """
    Get OAuth2 token for Microsoft Graph (client credentials flow)
    """
    token_url = f"https://login.microsoftonline.com/{GRAPH_TENANT_ID}/oauth2/v2.0/token"
    payload = {
        "client_id": GRAPH_CLIENT_ID,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": GRAPH_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    try:
        r = requests.post(token_url, data=payload)
        r.raise_for_status()
        access_token = r.json().get("access_token")
        if not access_token:
            logger.error("Failed to get access_token from Graph response")
            return None
        return access_token
    except Exception as e:
        logger.exception(f"Error fetching Graph token: {e}")
        return None
