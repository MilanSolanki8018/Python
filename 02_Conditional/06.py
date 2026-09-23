distance = int(input("Enter the distance in kilometers: "))

if distance < 3:
    print("Go by walking.")
elif distance >= 3 and distance < 15:
    print("Go by bicycle.")
elif distance >= 15:
    print("Go by car.")