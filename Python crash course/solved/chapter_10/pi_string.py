filename = 'pi_million_digits.txt'

with open('C:\\Users\\etiri\\Documents\\Python\\Python crash course\\en_python.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))
