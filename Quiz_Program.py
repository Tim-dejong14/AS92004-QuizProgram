total_score = 0
valid_answers = ["a", "b", "c", "d"]

print("Hello, welcome to the quiz!")
print("Todays quiz is on general knowledge, there will be 5 MULTI choice questions to answer!\n")
print("Enter only the letter of the answer you want to choose!") # quiz info

questions = [["What is the capital of France?", "A: Berlin", "B: Madrid", "C: Rome", "D: Paris"], 
             ["Which planet is known as the: Red Planet?", "A: Mars", "B: Venus", "C: Jupiter", "D: Saturn"],
             ["Who wrote the Harry Potter book series?", "A: J.R.R. Tolkien", "B: J.K. Rowling", "C: Suzanne Collins", "D: Rick Riordan" ],
             ["What is the freezing point of water in degrees Celsius?", "A: 32°C", "B: 10°C", "C: 0°C", "D: -10°C"],
             ["Which animal is known as the largest mammal on earth?", "A: Blue Whale", "B: Giraffe", "C: Elephant", "D: Hippopotamus"]
             ]
answers = ["d", "a", "b", "c", "a"]

for i, question in enumerate(questions): # creates a index for which number the question is on as the i variable and puts the question as the questions details
    for line in question:
        print(line)
    while True:
        answer = input("Enter your answer: ").lower()
        if answer in valid_answers:
            print("question answered\n")
            if answer == answers[i]:
                total_score += 1
            break
        else:
            print("Enter a valid answer")

print("Quiz over")

if total_score == 0:
    print(f"You failed the quiz and got {total_score}/{len(questions)} correct...")#feedback if you fail the quiz 
elif total_score == len(questions):
    print (f"You got {len(questions)}/{len(questions)} questions correct and have won the quiz! congrats~!") #len questions is to say that we have the max number of something so using it here is saying we have 5/5 questions answered.
else:
    print(f"Your score is {total_score}/{len(questions)}")#feedback if you get a question that is not 100% or 0% correct
