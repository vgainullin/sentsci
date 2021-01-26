import re

prefixes = "(Fig|Dr|Mr|Mrs)"
floating = "[.]([0-9])"
websites = "[.](com|net|org|io|gov)"


def split(text):
    text = re.sub(prefixes, r"\\1<prd>", text)
    text = re.sub(websites, r"\\1", text)
    text = re.sub("<prd>", ".", text)

    text = re.sub(r"\.\s", r".<splitter>", text)
    text = re.sub(r"\?\s", r"?<splitter>", text)
    text = re.sub(r"\!\s", r"!<splitter>", text)

    return text.split("<splitter>")