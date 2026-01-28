import re

JOB_CODE_REGEX = re.compile(r"JB\d{10}")

def extract_job_code(text: str) -> str | None:
    """Extract a valid JobCode from a string, or return None"""
    if not text:
        return None
    match = JOB_CODE_REGEX.search(str(text))
    return match.group(0) if match else None
