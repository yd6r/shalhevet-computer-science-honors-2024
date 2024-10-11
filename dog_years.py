print('Hello world')
#I can write a comment
user_input_prompt = "Enter your age here:\n "
user_input = input(user_input_prompt)
result = 1 + int(user_input)
print("Next year, your age will be:\n ",result)
user_input_prompt="Do you want to know your age in dog years?\n "
user_input=input(user_input_prompt)
if user_input.lower() in ["yes", "sure"]:
    result_2 = 7 * int(result-1)
    print("Your age in dog years is:\n",result_2)
else: 
    print("Ok")
