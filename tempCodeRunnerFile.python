print("welcome to the pattern generator and Number Analyzer!\n")

print("select an option:")

while True:
    print("\n\n1. Generate a pattern")
    print("2. Analyze a  range of number")
    print("3. Exit")

    choice = int(input("\nEnter your choice : "))

    match(choice):

        case 1 :
            rows = int(input("Enter the number of rows for the pattern:"))
    
            for i in range(1,rows+1):
                for j in range(1,i+1):
                    print("*",end=" ")
                print() 
    
        case 2 :
            start = int(input("Enter the start of the range:"))
            end = int(input("Enter the end of the range:"))
            total = 0
            for num in range(start,end+1):
               if(num%2==0):
                   print(f"Number {num} is Even")
               else:
                   print(f"Number {num} is Odd")
               total+=num
            print(f"Sum of all numbers from {start} to {end} is: {total}")

        case 3 :
             print("Exiting the program. Goodbye!")
             break
           
        case _ :
            print("Please enter valid choice")