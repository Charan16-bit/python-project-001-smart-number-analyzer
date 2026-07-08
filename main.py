print("======================")
print("SMART NUMBER ANALYZER")
print("======================")

entered_number = 947531

original = entered_number


sum = 0 
product = 1
largest = 0 
smallest = 9

reverse = 0
palidrome = 0
armstrong = 0 
prime = 0
perfect = 0

while (entered_number>0):
    digit = entered_number % 10
    sum+=digit
    product = product * digit
    reverse = reverse * 10 + digit
    armstrong += digit ** 3
    if (digit > largest):
        largest = digit 
    if (digit < smallest):
        smallest = digit
    entered_number //= 10
print("Digit Analysis")
print("---------------")
print("Sum            :",sum)
print("Product        :",product)
print("Largest Digit  :",largest) 
print("Smallest Digit :",smallest) 
print("\nNumber Analysis")
print("-------------------------")
### prime number 
i = 1
prime = 0
while (i <= original):
    if(original % i ==0 ):
        prime += 1
    i += 1

if(prime == 2):
    print("Prime        :",prime)
else:
    print("Not prime:     :",prime)


#perfect number
i = 1
perfect = 0
while (i < original):
    if(original % i ==0 ):
        perfect+= i
    i += 1
if(perfect == original):
    print("Perfect       :",perfect)
else:
    print("Not perfect    :",perfect)

if reverse == original:
    palindrome = "Yes"
else:
    palindrome = "No"

####ARMSTORNG
if armstrong == original:
    print("Armstrong : yes")
else:
    print("Armstrong : No")

print("Reverse         :",reverse)

