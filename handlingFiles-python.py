file = open("text.txt", "w")
cont = 1
while cont <= 5:
    print(f"Person {cont}: ")
    name = input("Enter the name: ")
    height = int(input("Enter the height in centimeters: "))
    while height < 150 or height > 250 or height < 0:
        print("Invalid height, try again")
        height = int(input("Enter the height in centimeters: "))
    file.write(name + "," + str(height) +"\n")
    cont += 1

file.close() 

file = open("text.txt", "r")

list = []
heightSum = 0
tallerPerson = ""
tallestHeight = 0

for line in file:
    output = line.split(",")
    name = output[0]
    altura = int(output[1])
    data = (name,altura)
    list.append(data)

file.close()

for data in list:
    heightSum += data[1]
    if data[1] > tallestHeight :
        tallestHeight = data[1]
        tallerPerson = data[0]

heightAvg = heightSum / len(list)


print(f"Height average: {heightAvg:5.0f}")
print(f"Tallest person: {tallerPerson} ({tallestHeight})")

    




