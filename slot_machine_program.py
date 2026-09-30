import random

balance = 100

# All slot machine symbols
symbols = [
    # Numbers
    "0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣",
    "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣",

    # Fruits
    "🍒", "🍋", "🍊", "🍉",
    "🍇", "🍎", "🍓", "🍌",

    # Classic symbols
    "⭐", "🔔", "💎", "💰",
    "👑", "🎯", "🍀"
]


# Starting balance
balance = 100


# Spin the slot machine
def spin():
    result = [
        random.choice(symbols),
        random.choice(symbols),
        random.choice(symbols)
    ]

    return result


# Calculate winnings
def calculate_winnings(result, bet):

    # Three matching symbols
    if result[0] == result[1] == result[2]:
        # 7️⃣ is the biggest jackpot
        if result[0] == "7️⃣":
            return bet * 20

        # 💎 is a very valuable symbol
        elif result[0] == "💎":
            return bet * 15

        # 👑 is also a valuable symbol
        elif result[0] == "👑":
            return bet * 10

        # ⭐️ and 💰 give a good payout
        elif result[0] in ["⭐️", "💰"]:
            return bet * 5

    # Two matching symbols
    elif (
        result[0] == result[1]
        or result[1] == result[2]
        or result[0] == result[2]
    ):
        return bet * 2

    # No matching symbols
    else:
        return 0

# Main game loop
while balance > 0:

    print("\n🎰 SLOT MACHINE 🎰")
    print("=" * 40)
    print(f"💰 Balance: ${balance}")
    print("=" * 40)

    # Ask the player for a bet 
    try:
        bet = int(input("🎟️ Enter your bet: $"))

        # Check if the bet is valid 
        if bet <= 0:
            print("❌ Bet must be greater than $0!")
            continue

        if bet > balance:
            print("❌ You don't have enough money!")
            continue

    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    # Take the bet from the balance
    balance -= bet

    print("\n🎰 Spinning...")

    # Spin the machine 
    result = spin()

    # Display the result
    print("\n" + " | ".join(result))

    # Calculate winnings
    winnings = calculate_winnings(result, bet)

    # Check the result
    if winnings > 0:
        balance += winnings

        # Three matching symbols
        if result[0] == result[1] == result[2]:
            if result[0] == "7️⃣":
                print("\n💥💥💥 JACKPOT!!! 💥💥💥")
                print("7️⃣ | 7️⃣ | 7️⃣")

            else: 
                print("\n🎉 THREE MATCHING SYMBOLS!")

            print(f"💰 You won ${winnings}!")

        # No matching symbols
    else:
        print("\n😢 No match!")
        print(f"💸 You lost ${bet}!")

    # Show current balance
    print(f"💰 Current balance: ${balance}")

    # Check if the player has money left
    if balance <= 0:
        print("\n💸 You ran out of money!")
        break

    # Ask the player if they want to continue
    play_again = input("\n🔄 Play again? (y/n): ").lower()

    if play_again not in {"yes", "y"}: 
        break

# Game over
print("\n🎰 GAME OVER 🎰")
print("=" * 40)
print(f"💰 Final balance: ${balance}")
print("👋🏻 Thanks for playing!")