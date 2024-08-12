# Generator function with yield

def even_generator(limit):
    for i in range(2,limit+1,2):
        # return i # result error as "NoneType is not iterable"
        yield i # This will return nums one by one 
    
for num in even_generator(10):
    print(num)