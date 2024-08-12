# Functions with *args

def sum_all(*args):
    # print(*args)
    # for i in args:
    #     print(i*3)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,10))