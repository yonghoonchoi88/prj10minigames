import random

def playUpDown():
    print("==================== UP DOWN GAME ====================")
    while True:
        answer = random.randint(1, 50)

        hand = int(input("1부터 50까지 숫자중 하나를 선택하세요:"))
        if hand > 50 or hand < 1:
            print("숫자 1부터 50까지만 선택 가능합니다.")
            continue

        else:
            count = 0
            while True:
                count += 1
                if hand < answer:
                    print("UP")
                    hand = int(input("숫자:"))
                elif hand > answer:
                    print("DOWN")
                    hand = int(input("숫자:"))
                else:
                    print(f"Number: {answer}")
                    print("Correct!!")
                    break
        print(f"축하합니다! {count}번 만에 맞히셨어요!")
        replay = input("Press any key to replay (N 입력시 종료)").upper()
        if replay == "N":
            break