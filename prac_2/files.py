#Ask user name and write it to name.txt
name = str(input("Enter your name : "))
op_file = open("name.txt","w")
op_file.write(name)
op_file.close()

#Read name from name.txt and print the name
op_file = open("name.txt","r")
new_name = op_file.read()
print("Your name is " + new_name)
op_file.close()

#Read numbers from numbers.txt and sum first two numbers
op_numbers = open("numbers.txt","r")
line1 = op_numbers.readline()
line2 = op_numbers.readline()
sum = int(line1) + int(line2)
print(sum)
op_numbers.close()

#Read numbers from numbers.txt and sum all numbers
op_numbers = open("numbers.txt","r")
lines = op_numbers.readlines()
sum_line = 0
for line in lines :
    sum_line = int(line) + sum_line
print(sum_line)
op_numbers.close()