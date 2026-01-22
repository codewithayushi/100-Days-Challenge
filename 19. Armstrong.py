#  Armstrong 

Number = int(input("Enter a Number: ")) #153
Total = 0

for i in str(Number):             # "1", "5", "3"
    Total=Total+int(i)**3         

if Total == Number:
    print("Armstrong")
else:
    print("Not Armstrong")