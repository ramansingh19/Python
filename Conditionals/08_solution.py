password = "raman2321wq"

if len(password) < 6:
  strength = "weak"
if len(password) < 10:
  strength = "Medium"
if len(password) > 10:
  strength = "Strong"

print(strength, "password")
