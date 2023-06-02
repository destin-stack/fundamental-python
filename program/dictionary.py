# Dictionary Declaration
users = {
    "id": 1,
    "name": "Leanna Graham",
    "username": "Bret",
    "email": "sincere@april.biz",
    "address": {
        "street": "West Avenue St",
        "suite": "Apt. 556",
        "city": "Gwen borough",
        "zipcode": "92998-3874"
    }
}

print(users)

# Access data dictionary using key
print("Access specific element : ")
print(f"name : {users['name']}")
print(f"address : {users['address']['street']}")

# Convert dictionary to json and vice versa
import json
result = json.dumps(users)
print(result)
print(type(users))
print(type(result))

# Convert to file
with open('result.json', 'w') as file:
    json.dump(users, file)

