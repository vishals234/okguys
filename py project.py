print("wecolme to the library")

def std_data():
    name=input("Enter your name:")
    roll_num=int(input("Enter your roll number:"))
    dept=input("Enter your department:")
# books list
print('"list of books"')
print('Engineering physics all volume:',"Book code: B01")
print('Engineering Mathematics all volume:',"Book code: B02")
print('Engineering Chemistry all volume:',"Book code: B03")
print('fundamental of machine drawing all volume:',"Book code: B03")
print('Universal science books:',"Book code: B04")
print('Python Programming language book:',"Book code: B05")
print('C++ and C programming books:',"Book code: B06")
print('Novels and Story books:',"Book code: B07")
print('General knowledge books:',"Book code: B08")

Book_name=input("Enter book name:")
Book_code=input("Enter book code from the list:")
if (Book_code=='B01'):
    print(Book_name,"Available rack 1 in Row 2")
elif (Book_code=='B02'):
    print(Book_name,"Available rack 2 in Row 1")
elif (Book_code=='B03'):
    print(Book_name,"Available rack 3 in Row 3")
elif (Book_code=='B04'):
    print(Book_name,"Available rack 4 in Row 8")
elif (Book_code=='B05'):
    print(Book_name,"Available rack 5 in Row 9")
elif (Book_code=='B06'):
    print(Book_name,"Available rack 6 in Row 8")
elif (Book_code=='B07'):
    print(Book_name,"Available rack 7 in Row 4")
elif (Book_code=='B08'):
    print(Book_name,"Available rack 8 in Row 10")
else:
    print("Invaild input")
register_book=input('You want to register the book:')
if register_book=='yes':
    print('Fill details')
    std_data()
    print("REGISTRATION DONE SPEND YOUR TIME FOR HAPPY LEARING")
else:
    print("SPEND YOUR TIME FOR HAPPY LEARING")
