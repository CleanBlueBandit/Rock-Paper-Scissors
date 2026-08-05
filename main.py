import random
import os
import time


name = input("Welcome to Rock paper scissors!\nYour name: ")
while True:
    x = int(input("Enter your hand sign\n1 - Rock\n2 - Paper\n3 - scissors\nYour choice: "))
    os.system("cls")
    print("[Referee]: 3...")
    time.sleep(1)
    os.system("cls")
    print("[Referee]: 2...")
    time.sleep(1)
    os.system("cls")
    print("[Referee]: 1...")
    time.sleep(1)
    os.system("cls")
    print("[Referee]: GO!")
    time.sleep(0.2)
    match x:
        case 1:
            print(f"[{name}]: I choose Rock!")
            y = random.randint(0, 2)
            match y:
                case 0:
                    # play Rock
                    print("[Bot]: I choose Rock!")
                    time.sleep(2)
                    print("The verdict is... ", end='')
                    time.sleep(1)
                    print("Draw!")
                    break
                case 1:
                    # play Paper
                    print("[Bot]: I choose Paper!")
                    time.sleep(2)
                    print("The verdict is... ", end='')
                    time.sleep(1)
                    print("Bot wins!")
                    break
                case 2:
                    # play scissors
                    print("[Bot]: I choose scissors!")
                    print(f"[Referee]: The verdict is... ")
                    time.sleep(0.7)
                    print(f"{name} wins!")
                    break
            break
        case 2:
            print(f"[{name}]: I choose Paper!")
            y = random.randint(0, 2)
            match y:
                case 0:
                    # play Rock
                    print("[Bot]: I choose Rock!")
                    time.sleep(2)
                    print("The verdict is... ", end='')
                    time.sleep(1)
                    print(f"{name} wins!")
                    break
                case 1:
                    # play Paper
                    print("[Bot]: I choose Paper!")
                    time.sleep(2)
                    print("The verdict is... ", end='')
                    time.sleep(1)
                    print("Draw!")
                    break
                case 2:
                    # play scissors
                    print("[Bot]: I choose scissors!")
                    print("[Referee]: The verdict is... ")
                    time.sleep(0.7)
                    print("Bot wins!")
                    break
            break
        case 3:
            print(f"[{name}]: I choose Scissors!")
            y = random.randint(0, 2)
            match y:
                case 0:
                    # play Rock
                    print("[Bot]: I choose Rock!")
                    time.sleep(2)
                    print("The verdict is... ", end='')
                    time.sleep(1)
                    print("Draw!")
                    break
                case 1:
                    # play Paper
                    print("[Bot]: I choose Paper!")
                    time.sleep(2)
                    print("The verdict is... ", end='')
                    time.sleep(1)
                    print("Bot wins!")
                    break
                case 2:
                    # play scissors
                    print("[Bot]: I choose scissors!")
                    print(f"[Referee]: The verdict is... ")
                    time.sleep(0.7)
                    print(f"{name} wins!")
                    break
        case _:
            print("[Referee]: Wrong. Next time, enter the number 1, 2 or 3")
os.system("pause")
