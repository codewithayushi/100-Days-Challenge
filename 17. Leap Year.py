# Check if a Year is a Leap Year

Year = int(input("Enter a Year: "))

if (Year%400==0) or (Year%4==0 and Year%100!=0):
    print("Leap Year: ", Year)
else:
    print("Not Leap Year", Year)