# Regex validate PIN code
# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/python

import re

def validate_pin(pin):
    if pin.isnumeric() == False:
        return False
    elif len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False

# test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
# test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
# test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
print(validate_pin("1234"));