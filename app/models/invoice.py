from dataclasses import dataclass

@dataclass
class InvoiceStatusUpdate:
    job_code: str
    status: str  # "PAID" or "NOT PAID"
    balance: float
