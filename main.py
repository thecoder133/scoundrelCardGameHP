def save_high_score(score):
    """Save the high score to a file"""
    with open('scoundrel_high.txt', 'w') as f:
        f.write(str(score))

def load_high_score():
    """Load the high score from file"""
    try:
        with open('scoundrel_high.txt', 'r') as f:
            return int(f.read())
    except:
        return 0

def check_high_score(score):
    """Check if this is a new high score"""
    current_high = load_high_score()
    
    print(f"\n{'='*30}")
    if score > current_high:
        save_high_score(score)
        print(f"🏆 NEW HIGH SCORE: {score} HP!")
        print(f"Previous best: {current_high} HP")
    else:
        print(f"Final Score: {score} HP")
        print(f"High Score: {current_high} HP")
    print(f"{'='*30}\n")

def scoundrel_game():
    """Track HP for Scoundrel card game"""
    hp = 20
    print("\n=== SCOUNDREL DUNGEON ===")
    print("Starting HP: 20\n")
    
    while True:
        print(f"Current HP: {hp}")
        
        try:
            change = int(input("HP change (+/-): "))
        except ValueError:
            print("Please enter a number!")
            continue
        
        hp += change
        
        # Death condition
        if hp <= 0:
            print("\n💀 YOU DIED!")
            
            # Calculate remaining cards as penalty
            remaining = input("Remaining card values (space-separated): ").strip()
            if remaining:
                try:
                    cards = [int(x) for x in remaining.split()]
                    penalty = sum(cards)
                    final_score = hp - penalty
                    print(f"\nRemaining cards penalty: -{penalty}")
                    print(f"Your score: {final_score}")
                except ValueError:
                    final_score = hp
            else:
                final_score = hp
            
            check_high_score(final_score)
            break
        
        # Victory condition - survived the whole deck
        check_victory = input("Deck empty? (y/n): ").lower().strip()
        if check_victory == 'y':
            print("\n🎉 YOU ESCAPED THE DUNGEON!")
            check_high_score(hp)
            break

# Start game
scoundrel_game()
