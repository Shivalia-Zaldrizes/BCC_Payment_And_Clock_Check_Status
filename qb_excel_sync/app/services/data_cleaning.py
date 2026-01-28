import pandas as pd

NO_WORK_VALUES = {"NO PUNCH", "CALL OUT", "", None}

def clean_qb_payroll(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Clean and split names
    df["name"] = df["name"].str.strip().str.title()

    # Split "Last, First", handle missing comma
    def split_name(full_name):
        if pd.isna(full_name) or full_name.strip() == "":
            return pd.Series(["Unknown", "Unknown"])
        parts = [p.strip() for p in full_name.split(",", 1)]
        if len(parts) == 2:
            return pd.Series([parts[0], parts[1]])  # last_name, first_name
        else:
            return pd.Series([parts[0], "Unknown"])  # assume all goes to last_name

    df[["last_name", "first_name"]] = df["name"].apply(split_name)

    # Numeric columns: ensure proper type
    numeric_cols = ["reg", "ot", "non-wkd", "total_paid_hrs", "unpaid"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Optional: normalize Work Start/End and Lunch times
    time_cols = ["work_start", "work_end", "lunch_in", "lunch_out", "scheduled_start", "scheduled_end"]
    for col in time_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format="%I:%M %p", errors="coerce").dt.time

    # Create pay_status based on Unpaid column
    df["pay_status"] = df["unpaid"].apply(lambda x: "Paid" if x == 0 else "Not Paid")

    return df
