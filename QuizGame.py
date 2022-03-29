# QUIZ GAME #

# User Input #
user_name = input("Enter you name: ").upper()

# Greetings and instructions #
print(f""""WELCOME TO THE QUIZ GAME, {user_name}!"\n
Instructions:
* Enter the correct answer from the options e.g: A, B, C, D
* Answers can be case-insensitive.\n""")

# Confirmation #
confirmation = input("Do you wish to continue? (yes/no): ").upper()
if confirmation == 'NO':
    print("Good Bye!")
    quit()

# Variables Declaration #
score = 0
options = ["A", "B", "C", "D"]
error = "Invalid option selected. Please select the options from the available options only. Try again."

# Question 1 #
print("\n\n1. Who invented the Light Bulb?\n"
      "A. Thomas Edison         B. Albert Einstein\n"
      "C. Isaac Newton          D. Alexander Graham Bell")
while True:
    answer = input("Your answer: ").upper()
    if answer in options:
        if answer == 'A':
            score += 1
            print("Correct answer!\n\n")
            break
        else:
            print("Wrong answer\n\n")
            break
    else:
        print(error)
        continue

# Question 2 #
print("2. What is the name of the biggest planet in our solar system?\n"
      "A. Earth             B. Mars\n"
      "C. Jupiter           D. Pluto")
while True:
    answer = input("Your answer: ").upper()
    if answer in options:
        if answer == 'C':
            score += 1
            print("Correct answer!\n\n")
            break
        else:
            print("Wrong answer\n\n")
            break
    else:
        print(error)
        continue

# Question 3 #
print("3. Who is the founder of Facebook?\n"
      "A. Jeff Bezos            B. Mark Zuckerberg\n"
      "C. Jack Ma               D. Steve Jobs")
while True:
    answer = input("Your answer: ").upper()
    if answer in options:
        if answer == 'B':
            score += 1
            print("Correct answer!\n\n")
            break
        else:
            print("Wrong answer\n\n")
            break
    else:
        print(error)
        continue

# Question 4 #
print("4. Who is known as the Father of the Indian Constitution?\n"
      "A. M. K. Gandhi               B. Subhash Chandra Bose\n"
      "C. Dr B. R. Ambedkar          D. Jawaharlal Nehru")
while True:
    answer = input("Your answer: ").upper()
    if answer in options:
        if answer == 'C':
            score += 1
            print("Correct answer!\n\n")
            break
        else:
            print("Wrong answer\n\n")
            break
    else:
        print(error)
        continue

# Result #
print(f"You gave {score} right answer(s).")
print("You scored", str((score / 4) * 100) + "%")

# Conclusion #
if score <= 1:
    print("Your G.K needs a lot of improvement!")
elif score == 4:
    print("Excellent work!")
else:
    print("Good! But still needs improvement.")
