import csv
from app.utils.jobcode import extract_job_code
from app.logging import logger
from dataclasses import dataclass

@dataclass
class InvoiceUpdate:
    job_code: str
    balance: float
    status: str

def parse_qb_csv(path: str) -> list[InvoiceUpdate]:
    updates = []
    try:
        with open(path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                job_code = extract_job_code(row.get("JobCode"))
                if not job_code:
                    continue
                try:
                    balance = float(str(row.get("Balance")).replace("$","").replace(",","").strip())
                except:
                    balance = 0
                status = "PAID" if balance == 0 else "NOT PAID"
                updates.append(InvoiceUpdate(job_code, balance, status))
    except Exception as e:
        logger.exception(f"Error reading CSV {path}: {e}")
    return updates
