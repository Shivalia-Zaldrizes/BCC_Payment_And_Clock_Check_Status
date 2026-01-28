import pandas as pd

# ---------- helpers ----------

MONETARY_COLUMNS = {
    "gross_wages": ["gross_wages", "gross", "total_gross"],
    "amount_paid": ["amount_paid", "paid"],
    "remaining_balance": ["remaining_balance", "balance", "amount_due"]
}

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def normalize_money_columns(df: pd.DataFrame) -> pd.DataFrame:
    for canonical, options in MONETARY_COLUMNS.items():
        for col in options:
            if col in df.columns:
                df[canonical] = pd.to_numeric(df[col], errors="coerce").fillna(0)
                break
        else:
            df[canonical] = 0
    return df


def normalize_name(name: str) -> str:
    return (
        str(name)
        .lower()
        .replace(",", "")
        .replace(".", "")
        .strip()
    )


def compute_payment_status(row) -> str:
    gross = row["gross_wages"]
    paid = row["amount_paid"]
    remaining = row["remaining_balance"]

    if gross == 0:
        return "No Hours"

    if remaining == 0 and paid > 0:
        return "Paid"

    if paid > 0 and remaining > 0:
        return "Partial"

    if paid == 0 and gross > 0:
        return "Unpaid"

    return "Unknown"


# ---------- main cleaning entry ----------

def clean_qb_payroll(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalize headers
    df = normalize_columns(df)

    # Require employee name
    if "employee_name" not in df.columns:
        raise KeyError("Expected 'Employee Name' column")

    # Clean employee name
    df["employee_name"] = df["employee_name"].str.strip().str.title()

    # Create merge-safe key
    df["merge_name"] = df["employee_name"].apply(normalize_name)

    # Normalize monetary columns
    df = normalize_money_columns(df)

    # Compute payment status
    df["payment_status"] = df.apply(compute_payment_status, axis=1)

    return df
