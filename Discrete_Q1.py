def numbers():
   digits = []
   for x in range(5):
       user_input = input("Enter any numbers you want. You are allowed to repeat any digits: ")
       digits.append(user_input)
   print(digits)

   figures = set(digits)

   if len(digits) == len(figures):
       print("True")

   else:
       print(f"False. The set should be {figures}")


numbers()

