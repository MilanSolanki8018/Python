def details(**kwargs):

    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)
        
    return kwargs;

print(details(name="virat", age=30, country="India"))