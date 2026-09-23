def sum_all(*args):
    print(args)
    print(type(args))
    print(len(args))
    return sum(args)

print(sum_all(1,4,6,2))