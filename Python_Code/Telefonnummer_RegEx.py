import re

def validate_phone_number(phone_number):
    # Definiere die Regex für eine deutsche Telefonnummer
    pattern = r'^\+49 \d{3} \d{6,8}$'

    # Überprüfe, ob die Telefonnummer dem Regex-Muster entspricht
    if re.match(pattern, phone_number):
        return True
    else:
        return False

# Beispielaufrufe
number1 = "+49 123 456789"
number2 = "+49 123 4567"
number3 = "invalid_number"
print(f"Ist {number1} eine gültige Telefonnummer? {validate_phone_number(number1)}")
print(f"Ist {number2} eine gültige Telefonnummer? {validate_phone_number(number2)}")
print(f"Ist {number3} eine gültige Telefonnummer? {validate_phone_number(number3)}")