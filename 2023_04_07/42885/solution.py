people = [70, 50, 80, 50]
limit = 100

arr = sorted(people, reverse=True)

i = 0
while i < len(arr):
    if (arr[i] + arr[-1]) <= limit:
        arr.pop()
    i += 1
        
print(i)