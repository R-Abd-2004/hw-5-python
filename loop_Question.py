# Question One

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers :
    if num > 500 :
        break
    elif num > 150 :
        continue
    elif num % 5 == 0 :
        print(num)

print("="*50)   # Separator

# Question Two

for i in range(5):
    print(i)
else:
    print("Done!")

print("="*50)   # Separator

# Question Three

num = 76542
reverse_num = 0
while num != 0:
    rsult = num % 10
    reverse_num = reverse_num * 10 + rsult
    num //= 10
print(reverse_num)

# Test
