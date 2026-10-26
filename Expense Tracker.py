
expenses =[] # list of all expense in from of dictonory

print("Welcome To Expense Tracker")

while True :
    print("===MENU==")
    print("1. Add Expense ")
    print("2. View All Expense")
    print("3. View Total Kharcha ")
    print("4. Exit")

    choice=int(input("Enter Your choice :  "))


# ADD Expense

    if(choice==1):
        date= input("Kiss date par kharcha kiya thaa? ")
        category= input("Enter The Category (food,travel): ")
        description= input("Enter the details about Kharcha: ")
        amount= input("Enter The Amount You Want To Spent it: ")

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }


        expenses.append(expense)
        print("Done Bro Expense added Succesfully")

#2
    elif(choice==2):
        if (len(expenses)==0):
            print("No Expenses Added yet plz add")

        else:
            print("This is your All Expenses")

            count=1
            for eachkharcha in expenses:
                print(f"kharcha number{count} --> {eachkharcha["date"]},{eachkharcha["category"]},{eachkharcha["description"]},{eachkharcha["amount"]}")    
                count= count+1


#3
    elif(choice==3):
        total =0
        for eachkharcha in expenses:
            total = total + int(eachkharcha["amount"])

        print("\n This is Your Total Kharcha",total)


    elif(choice==4):
        print("Thank you For Visting ")
        break

    else:
        print("Invalid Choice Plz Try Again ")
      
        



