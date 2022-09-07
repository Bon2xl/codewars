# Century From Year
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097


def century(year):
  century_count = year / 100
  remaining_months = year % 100

  total = century_count 
  if remaining_months > 0:
    total = int(total) + 1

  return total;

print(century(1705))