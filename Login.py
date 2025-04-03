import string
import os

# Lucia, 12/11/2024
# To write a simple login program


# Create a simple manu system                                                                  
print("Tasks:")
print("1. Register a new user")
print("2. View accounts - accounts listing")
print("3. Exit the program")
print()
task=input("What would you like to do? 1,2,or 3: ")
print()


if task=="1":
    # Component 1 - Creating a new user account (registration)
    print("Register a new user") 
    newusername=input("Please type in new username: ")
    newpassword=input("Please type in new password: ")
    validpassword=len(newpassword)
    # Check if the new password is more than 10 characters to proceed the registration.
    if validpassword<10:
        print("Password should be more than 10 characters.")
        print("The new user is not registered!")
        print()
    else:
        file=open("accounts.txt","a")
        file.write(newusername + "," + newpassword + "\n")
        file.close()     
        print("New user is registered!")

elif task=="2":
    # Component 3 - View existing accounts(displaying users)

    # Component 2 - Check if this is a valid user to veiw the existing accounts
    print("Please login with your username and password")
    print()
    username=input("Please type in your username: ")
    password=input("Please type in your password: ")
    login=username + "," + password
    file=open("accounts.txt","r")
    user=file.readline()
    user=user.rstrip('\n')
    while user !='':
      result="Login successful!"
      if login==user:
         break
      result="Invalid login!"
      user=file.readline()  
      user=user.rstrip('\n') 
    print(result)
    print()
    file.close()

    # If valid, proceed to print the list.
    if result=="Login successful!":
        file=open("accounts.txt", "r")
        print("List of accounts:"+"\n")      
        user=file.readline()
        a=1      
        while user !='':   
            print(str(a)," ",end="") 
            i=0
            j=user.find(',')                
            while i<j:
                print(user[i], end='')
                i=i+1
            print('\n'.strip())
            a=a+1
            user=file.readline()
        print()
        file.close() 
    
    else:
        print("You can't view existing accounts!")

else:
    # Exit the program
    print("Goodbye!")
    print()

