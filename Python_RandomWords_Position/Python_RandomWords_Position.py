
import random

words_list = ["cat", "apple", "mangobar"]
rnd_words = random.choice(words_list)
words_count = len(rnd_words)
lives = 6
end_of_game = False

print(f"Random word is:", rnd_words )

display = []
for _ in range(words_count):
    display += "_"


while not end_of_game:
    guess = input("Enter a letter. \n").lower()


       
# for letter in rnd_words:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")

    for position in range(words_count):
        letter =  rnd_words[position]
        if letter == guess:
            display[position] = letter
    

    if guess not in rnd_words:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Your lose")
        
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    
    
   
    





