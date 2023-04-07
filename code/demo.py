import random

money = 100 # Khởi tạo số tiền của người chơi

while True:
    print("Số tiền của bạn là:", money)
    choice = input("Bạn chọn Tài hay Xỉu? ").lower()
    if choice not in ["tài", "xỉu"]:
        print("Vui lòng chọn Tài hoặc Xỉu.")
        continue
    bet = int(input("Nhập số tiền cược của bạn: "))
    if bet > money:
        print("Số tiền cược của bạn không đủ.")
        continue
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    total = dice1 + dice2 + dice3
    print("Kết quả xúc xắc:", dice1, dice2, dice3)
    if total > 10:
        result = "tài"
    else:
        result = "xỉu"
    if choice == result:
        money += bet
        print("Chúc mừng, bạn đã thắng", bet, "đồng.")
    else:
        money -= bet
        print("Rất tiếc, bạn đã thua", bet, "đồng.")
    play_again = input("Bạn muốn tiếp tục chơi (tiếp) hay dừng (dừng)? ").lower()
    if play_again == "dừng":
        print("Cảm ơn bạn đã chơi!")
        break
