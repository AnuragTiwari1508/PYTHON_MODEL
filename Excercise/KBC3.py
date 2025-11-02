questions = [
    ["who are you", "anurag", "anshika", "rishabh", "ashish"],
    ["what is your name", "anurag", "anshika", "rishabh", "ashish"],
    ["Tumhara naam kya hai?", "anurag", "anshika", "rishabh", "ashish"],
    ["Apka naame kya he?", "anurag", "anshika", "rishabh", "ashish"],
    ["college name?", "IIT INDORE", "RGPV", "DAVV", "SAGE UNIVERSITY"],
    ["famous university of indore", "IIT INDORE", "RGPV", "DAVV", "SAGE UNIVERSITY"],
]
prizes=[1000,2000,4000,8000,16000]
score=0
for i in range(len(questions)):
    print(questions[i][0])
    print("option a:", questions[i][1])
    print("option b:", questions[i][2])
    print("option c:", questions[i][3])
    print("option d:", questions[i][4])
    ans = int(input("enter your answer 1/2/3/4 :"))
    if ans == 1:
        score += prizes[i]
        print("your answer is correct")
    elif(prizes==2000):
        score =1000
    elif(prizes==8000):
        score =4000
    else:
        print("your answer is incorrect")
        print(f"your total score is : {score}")
        break