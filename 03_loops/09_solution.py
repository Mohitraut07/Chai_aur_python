# List Uniqueness checker

items = ["apple","banana","mango","jackfruit","jackfruit"]
unique_items = set()

for item in items:
    if item in unique_items:
        print("Repeated item is:",item)
        break
    unique_items.add(item)