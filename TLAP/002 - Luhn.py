def lun_val():
    user_value_digits = []
    user_value = input("Insert number to validate ")
    if user_value.isdigit():
        
        for index, digit in enumerate(user_value):
            digit = int(digit)
            if index % 2 == 1:
                digit *= 2
                if digit > 9:
                    big_d=decomp_number(digit)
                    user_value_digits.append(big_d)

            user_value_digits.append(digit)
        print(user_value_digits)

def mul_number(digit):



def decomp_number(digit):
   big_number = [int(d) for d in str(digit)]
   summ = sum(big_number)
   return summ

def validate_sum(digit_sum):
    if digit_sum % 10 == 0:
        return print("The validation is successful")
    else:
        return print("The validation not successful")


lun_val()

