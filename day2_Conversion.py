def celcius_to_fahrenheit(cel):
    return ((9/5)*cel)+32

def metre_to_kilometre(m):
    return m/1000

def usd_to_inr(usd):
    return usd*83.57

celcius=int(input("Enter celcius: "))
print(f"{celcius} celcius = {celcius_to_fahrenheit(celcius)} fahrenheit")

metre=int(input("Enter metre : "))
print(f"{metre} metre = {metre_to_kilometre(metre)} Kilometre")

usd=int(input("Enter usd : "))
print(f"{usd} usd = {usd_to_inr(usd)} inr")