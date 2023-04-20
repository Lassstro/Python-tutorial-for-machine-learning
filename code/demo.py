# import random

# money = 100 # Khởi tạo số tiền của người chơi

# while True:
#     print("Số tiền của bạn là:", money)
#     choice = input("Bạn chọn Tài hay Xỉu? ").lower()
#     if choice not in ["tài", "xỉu"]:
#         print("Vui lòng chọn Tài hoặc Xỉu.")
#         continue
#     bet = int(input("Nhập số tiền cược của bạn: "))
#     if bet > money:
#         print("Số tiền cược của bạn không đủ.")
#         continue
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     dice3 = random.randint(1, 6)
#     total = dice1 + dice2 + dice3
#     print("Kết quả xúc xắc:", dice1, dice2, dice3)
#     if total > 10:
#         result = "tài"
#     else:
#         result = "xỉu"
#     if choice == result:
#         money += bet
#         print("Chúc mừng, bạn đã thắng", bet, "đồng.")
#     else:
#         money -= bet
#         print("Rất tiếc, bạn đã thua", bet, "đồng.")
#     play_again = input("Bạn muốn tiếp tục chơi (tiếp) hay dừng (dừng)? ").lower()
#     if play_again == "dừng":
#         print("Cảm ơn bạn đã chơi!")
#         break

while True:
    user_name = input("Nhập tên đăng nhập: ")
    pass_word = input("Nhập mật khẩu: ")
    # loại bỏ khoảng trắng 2 đầu
    user_name = user_name.strip()
    pass_word = pass_word.strip()
    # Kiểm tra tên đăng nhập
    if len(user_name) < 8 or len(user_name) > 12:
        print("Tên đăng nhập không hợp lệ. Tên đăng nhập cần có 8-12 kí tự, Hãy kiểm tra lại")
        continue
    if not user_name.isalnum():
        print("Tên đăng nhập không hợp lệ. Tên đăng nhập chỉ chứa kí tự chữ và số. Hãy kiểm tra lại")
        continue
    print("Tên đăng nhập hợp lệ")
    # Kiểm tra mật khẩu
    if len(pass_word) < 8 or len(pass_word)> 12:
        print("Mật khẩu không hợp lệ. Mật khẩu cần có 8-12 kí tự")
        continue
    check_upper = False
    check_lower = False
    check_number = False
    check_special_character = False
    for character in pass_word:
        if character.isupper():
            check_upper = True
            continue
        if character.islower():
            check_lower = True
            continue
        if character.isnumeric():
            check_number = True
            continue
        if not character.isalnum():
            check_special_character = True
            continue
    if check_upper and check_lower and check_number and check_special_character:
        print('Hợp lệ')
        break
    else:
        print("Mật khẩu không hợp lệ. Mật khẩu bắt buộc có chữ cái viết hoa, chữ cái thường, số và kí tự đặc biệt. Hãy kiểm tra lại")