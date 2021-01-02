def my(start: int, end: int):
    while start < end:
        yield start
        start +=1

for i in my(1,10):
    print(i)