def plus_three(number):
    def add_three(number):  # Clearer name
        return number + 3
    number = add_three(number)
    return number
print(plus_three(10))
  
