#  Lists of Admins
Admins = ["Ahmed", "stevin", "Sara", "Omar", "Hima"]

# Login
Name_input = input("Enter Your Name: ").strip().capitalize()
if Name_input in Admins:
    print(f"Welcome {Name_input} , Great to See you. ")

    option = input("Delete or Update ur Name? ").strip().capitalize()

    if option == "Update":
        Your_new_Name = input("Enter ur New Valid Name: ")
        Admins[Admins.index(Name_input)] = Your_new_Name
        print("Name Is Updated Successfully")

        print(Admins)

    elif option == "Delete":
        Admins.remove(Name_input)
        print(Admins)


else:
    print("You Are not Admin , Go out.")
