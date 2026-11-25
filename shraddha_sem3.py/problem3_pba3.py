import re

text="""Pune:411001
Mumbai: 400001
Delhi:110001
Inva;id PIN: 012345
Invalid PIN: 41100"""

pattern= r"\b[1-9][0-9]{5}\b"

result = re.findall(pattern,text)

print("Valid Indian PIN codes:")

for pin in result:
  print(pin)
