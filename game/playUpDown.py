import random

def check_number():
    while True:
        number = input("1부터 50까지 숫자중 하나를 선택하세요:")
        try:
            number = int(number)
        except ValueError:
            print("숫자만 입력 가능합니다.")
            continue

        if 0 < number < 51:
            return number
        else:
            print("숫자 1부터 50까지만 선택 가능합니다.")
            continue


def playUpDown():
    print("==================== UP DOWN GAME ====================")
    while True:
        answer = random.randint(1, 50)

        hand = check_number()

        count = 0
        while True:
            count += 1
            if hand < answer:
                print("UP")
                hand = check_number()
            elif hand > answer:
                print("DOWN")
                hand = check_number()
            else:
                print(f"Number: {answer}")
                print("Correct!!")
                break
        print(f"축하합니다! {count}번 만에 맞히셨어요!")
        replay = input("Press ENTER to replay (N 입력시 종료)").upper()
        if replay == "N":
            break