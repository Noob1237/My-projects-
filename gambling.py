import random

balance = 1000

while balance > 0:
    print(f"\nBalance: ${balance}")
    
    try:
        bet = int(input("Bet amount (0 to quit): $"))
        if bet == 0:
            break
        if bet <= 0 or bet > balance:
            print("Invalid bet!")
            continue
        
        choice = input("RED or BLACK: ").lower()
        if choice not in ["red", "black"]:
            print("Invalid choice!")
            continue
        
        result = random.choice(["red", "black"])
        if result == choice:
            balance += bet
            print(f"WIN! +${bet}")
        else:
            balance -= bet
            print(f"LOSE! -${bet}")
    
    except ValueError:
        print("Enter a number!")

print(f"\nFinal: ${balance}")


