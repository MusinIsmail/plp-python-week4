# list_warmup.py

# 1. Create a list called fruits containing four fruits of your choice
fruits = ["apple", "banana", "orange", "mango"]

# 2. Print the first and the last item using indexes
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 3. Append a fifth fruit, then print the whole list
fruits.append("pineapple")
print("After append:", fruits)

# 4. Remove one fruit, then print the list again
fruits.remove("banana")
print("After remove:", fruits)

# 5. Print how many fruits remain using len()
print(f"Number of fruits remaining: {len(fruits)}")