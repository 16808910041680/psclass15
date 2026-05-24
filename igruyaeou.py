import numpy as np
import random
import time
import sys
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
key_shuffle = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince']

pause_time = 3
float (pause_time)
print ("Welcome to the Key Shuffle Game! Choose your difficulty.")
difficulty = input ("Type 'easy' for 5 items, 'medium' for 10 items, 'hard' for all 15 items, or custom to choose your own number of items (1-15) and the time it pauses (1-5 seconds): ")
if difficulty == 'easy':
    key_shuffle = key_shuffle[:5]
elif difficulty == 'medium':
    key_shuffle = key_shuffle[:10]
elif difficulty == 'hard':
    key_shuffle = key_shuffle[:15]
elif difficulty == 'custom':
    num_items = int(input("Enter the number of items (1-15): "))
    pause_time = float(input("Enter the pause time (1-5 seconds): "))
    key_shuffle = key_shuffle[:num_items]


print("Original list:")
print(key_shuffle)
print ("Correct Key:")
key = random.choice(key_shuffle)
print (key)
time.sleep (3)
print ("Shuffling!")
def delete_last_line():
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    sys.stdout.flush()

for i in range (50):
    random.shuffle(key_shuffle)
    print (key_shuffle) 
    time.sleep(0.2)
    delete_last_line()
    if len (key_shuffle) > 13:
        delete_last_line()
    


print ("Final shuffled list! Find the key!")
print (key_shuffle)
time.sleep (pause_time)
delete_last_line()
delete_last_line()

keyguess = input ("Tell me where is the key in the string? Number from 1 to 15:")
print("You selected:", keyguess)
keyindex = key_shuffle.index(key)
keyguess = int(keyguess)
keyindex = keyindex + 1
keyindex = int(keyindex)


if keyguess - keyindex == 0:
    print("You guessed", keyguess, "and the key is at position", keyindex, ". You win!")
elif keyguess - keyindex == 1 or keyguess - keyindex == -1:
    print("You guessed", keyguess, "and the key is at position", keyindex, ". So close!")
else:
    print("You guessed", keyguess, "and the key is at position", keyindex, ".Better luck next time!")