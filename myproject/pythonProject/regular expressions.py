import re
password = re.compile(r"[A-Za-z0-9#$%@]{7,}\d")
string = "usay12#0"
check = password.fullmatch(string)
print(check)
