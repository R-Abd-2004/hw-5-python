# Question One

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
mydict = {}
for key in keys:
    for value in values:
        mydict[key] = value
        values.remove(value)
        break
print(mydict)


print("="*50)   # Separator

# Question Two

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
for key in keys:
    sample_dict.pop(key)
print(sample_dict)

