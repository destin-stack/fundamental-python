# Try Python
print('Hello World')
print("Destin here, let's start our journey in learning Python")

# Conditional/Branching
milk_bottle_count = 100
egg_count = 7
budi_money = 20000
milk_price = 20000
egg_price = 2000

print(f"Budi have {budi_money} money, he want to buy milk and eggs")
if milk_bottle_count > 0:
    if budi_money >= milk_price:
        budi_money = budi_money - milk_price
        print(f"Buy 1 milk -> current money = {budi_money}")
    else:
        print("Budi did not have enough money")
else:
    print("Milk stock is empty")

if budi_money > 0:
    if egg_count >= 6:
        if budi_money >= egg_price * 6:
            budi_money = budi_money - egg_price*6
            print(f"Buy 6 eggs -> current money = {budi_money}")
        else:
            print("Not enough money")
    else:
        print("Not enough egg stock")
else:
    print("There's no enough money")


# Looping
# For looping

print("=====================================================")
print("                  READING BOOK PROGRAM              ")
books = 10
read_book = 0

print("Let's read books and get bunch of knowledge!!!")
for i in range(0, books):
    print(f"Book {i+1} has been read")
    read_book += 1

print("Finish reading all books")
print("=====================================================")