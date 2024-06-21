# 1
# print("== Registration form ==")
# username = input("Please input username: ")
# password = input("Please input password: ")
# email = input("Please input email: ")
# if username == "abcde" and password == "12345" and email == "abc@gmail.com":
#     print("Successful registration")
# else:
#     print("Failed registration")

# 2
# print("== Registration form ==")
# username = input("Please input username: ")
# while True:
#     password = input("Please input password: ")
#     confirm_password = input("Please re-input password: ")
#     if confirm_password == password:
#         print("Password aligned, please re-enter")
#         pass
#     else:
#         print("Password misalign, you cannot enter")
#     break
# email = input("Please input email: ")
# if username == "abcde" and confirm_password == password and email == "abc@gmail.com":
#     print("Successful registration")
# else:
#     print("Failed registration")

# 3
# import re
# print("== Registration form ==")
# username = input("Please input username: ")
# password = input("Please input password: ")
# while True:
#     if len(password) > 8 and re.search("[a-zA-Z]", password) and re.search("[0-9]", password):
#         print("Valid password")
#         pass
#     else:
#         print("Invalid password")
#     break
# confirm_password = input("Please re-input password:")
# while True:
#     if confirm_password == password:
#         print("Password aligned, please re-enter")
#     else:
#         print("Password misaligned, you cannot enter")
#     break
# email = input("Please input email: ")
# while True:
#     if '@' in email and '.' in email:
#         print("Valid email")
#     else:
#         print("Invalid email")
#     break  