quetions =("how many elements are in the periodic table?:",
            "which animal lays the largest eggs?:",
            "what is the most abundant gas in earth's atmosphere?:",
            "how many boens are in the human body?:",
            "which palnet in the solar system is the hottest?:")
options =(("A.116","B.117","C.118","D.119"),
          ("A.whale","B.crocodile","C.elephant","D.ostrich"),
          ("A.nitrogen","B.oxygen","C.carbon-dioxide","D.hydrogen"),
          ("A.mercury","B.venus","C.earth","D.mars"),
          ("A.mercury","B.venus","C.earth","D.mars"))
answers =("A","B","C","D","E")
guesses =[]
score=0
question_num = 0
for question in quetions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess =input("enter the option:").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("correct")
    else:
        print("incorrect")
        print(f"correct answer is{answers[question_num]}")
    question_num+=1
print("------------------")
print("      result      ")
print("------------------")
print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print ("guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
score =score/question_num*100

print(f"your score is:{score}%")