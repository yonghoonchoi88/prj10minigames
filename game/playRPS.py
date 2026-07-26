def playRPS():
    print("==================== ROCK PAPER SCISSORS GAME ====================")

    import random

    answer = random.randint(1, 3)

    if answer == 1:
        answer = "가위"
    if answer == 2:
        answer = "바위"
    if answer == 3:
        answer = "보"

    result = " "

    while True:
        hand = input("가위 바위 보:")
        if hand != "가위" and hand != "바위" and hand != "보":
            print("가위, 바위, 보 중에 다시 선택하세요")
        elif hand == answer:
            print(f"컴퓨터: {answer} 유저: {hand}")
            print("다시 선택하세요")
        elif answer != hand:
            print(f"컴퓨터: {answer} 유저: {hand}")
            if hand == "가위":
                result = "컴퓨터승" if answer == "바위" else "유저승"
            elif hand == "바위":
                result = "컴퓨터승" if answer == "보" else "유저승"
            elif hand == "보":
                result = "컴퓨터승" if answer == "가위" else "유저승"
            print(result)
            break