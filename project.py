a = "welcome to the interactive personal data collector!"
print(a.title() + "\n")
 
name = input("please enter your name :")
age  = int(input("please enter your age :"))
height = float(input("please enter your heights in metres : "))
favouritenumber = int( input( "please enter your favourite number : ") )

print("Thankyou! Here is the information we collected : ")

print ("name :",name ,"(type",type(name),"memory address:",id(name),")")
print ("age :",(age) ,"(type",type(age),"memory address:",id(age),")")
print ("height : ",(height),"(type",type(height),"memory address:",id(height),")")
print ("favourite number : ",(favouritenumber ),"(type",type(favouritenumber),"memory address :",id(favouritenumber),")")

birthyear = (2026 - age) 

print("\nyour birthyear is approximately : ",birthyear,"based on your age of ",age,)
print("thank you for using the personal data collector. goodbye")