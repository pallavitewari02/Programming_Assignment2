i=int(input("Enter the degree celsius to be converted to Fahrenheit: "))
#(0°C × 9/5) + 32 = 32°F
def convert(i):
    q=(i * 9/5) + 32
    return q

a=convert(i)
print(a)