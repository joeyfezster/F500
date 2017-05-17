import re


def contains_alphanumerics(text):
    if re.search('[a-zA-Z0-9]', text): return True
    return False


def detect_is_date(title):
    return str(title).lower() in ["date"]
