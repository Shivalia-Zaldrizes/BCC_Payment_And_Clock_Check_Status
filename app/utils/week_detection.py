from datetime import datetime
from typing import List, Tuple
from openpyxl.worksheet.worksheet import Worksheet


def is_week_ending_cell(value) -> bool:
    if not value:
        return False
    return "Week Ending" in str(value)


def extract_week_date(value) -> str | None:
    """
    Converts 'Week Ending 1/21/2026' → '2026-01-21'
    """
    try:
        parts = str(value).split("Week Ending")[-1].strip()
        dt = datetime.strptime(parts, "%m/%d/%Y")
        return dt.date().isoformat()
    except Exception:
        return None


def find_week_blocks(ws: Worksheet) -> List[Tuple[int, int, str]]:
    """
    Returns:
    [
      (start_row, end_row, week_ending_iso),
      ...
    ]
    """
    blocks = []
    rows = list(ws.iter_rows(values_only=True))

    i = 0
    while i < len(rows):
        if is_week_ending_cell(rows[i][0]):
            week_date = extract_week_date(rows[i][0])
            start = i + 1

            j = start
            while j < len(rows) and not is_week_ending_cell(rows[j][0]):
                j += 1

            end = j
            if week_date:
                blocks.append((start + 1, end, week_date))
            i = j
        else:
            i += 1

    return blocks
