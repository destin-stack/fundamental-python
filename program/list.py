# list declaration
bookList = ['Seven Habits', 'How to Influence People', 'First Thing First']
print(bookList)
print("=============================================")

# For loop for list
for book in bookList:
    print(book)
print("=============================================")

# Access data list using index
print("Display book for specific index")
print(bookList[0])
print("=============================================")

for i in range(0, len(bookList)):
    print(bookList[i])
print("=============================================")

# Add data to list using append()
bookList.append('Norwegian Wood')
print(bookList)
print("=============================================")

# Delete all list data using clear()
# bookList.clear()
# print(bookList)

# Update list data
bookList[0] = 'New Book Title'
print(bookList)
print("=============================================")

# Remove list data using pop and remove
# bookList.pop(0)
# bookList.remove(bookList[1])
# print(bookList)
# print("=============================================")

# List Comprehension - Remove list data using del
# Syntax : del listName[index(start):number of data to be deleted(end):step]
print(f"Before deletion : {bookList}")
del bookList[0:1]
print(f"After deletion : {bookList}")

