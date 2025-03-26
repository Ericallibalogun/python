amount = int(input("Enter the invested amount : "))
annual_rate = int(input("Enter the annual rate : "))
number_of_years = int(input("Enter the number of years : "))

converted_rate = (round(annual_rate / 100,2))
expected_profit =amount * (1 + converted_rate) ** (number_of_years * 365)

print(f'The expect profit at the end of {number_of_years} years is,{expected_profit:.2f}')



