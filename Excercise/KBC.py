q1="who is prime minister of india"
q2="famous university of indore"
q3="Most famous person IET DAVV"
q4="Most expensive city of india"
q5="capital of india"
ques=[q1,q2,q3,q4,q5]
sum =0
for i in range(len(ques)):  #len(ques) cannot give directly because format is like for i in range(int) in case of directly writing for i in ques it will take each element of string whether is str or int for anyother data type
    print(ques[i])
    match i:
        case 0:
            print("option a: jawahar lal nehru")
            print("option b: narendra modi")
            print("option c: amit shah")
            print("option d: manmohan singh")
            ans=int(input("enter your answer 1/2/3/4 :"))
            if ans==2:
                sum +=1000
                print("your answer is correct")
            else:
                print("your answer is incorrect")
        case 1:
            print("option a: IIT INDORE")
            print("option b: RGPV")
            print("option c: DAVV")
            print("option d: SAGE UNIVERSITY")
            ans=input("enter your answer 1/2/3/4 :")
            if ans=="3":
                sum +=2000
                print("your answer is correct")
            else:
                print("your answer is incorrect")
        case 2:
            print("option a: Anurag Tiwari")
            print("option b: Ashish Balodia")
            print("option c: Anshika Agrawal")
            print("option d: Pari Meena")
            ans=input("enter your answer 1/2/3/4 :")
            if ans=="1":
                sum +=4000
                print("your answer is correct")
            else:
                print("your answer is incorrect")
        case 3:
            print("option a: indore")
            print("option b: delhi")
            print("option c: banglore")
            print("option d: mumbai")
            ans=input("enter your answer 1/2/3/4 :")
            if ans=="4":
                sum +=8000
                print("your answer is correct")
            else:
                print("your answer is incorrect")
        case 4:
            print("option a: Indore")
            print("option b: Bhopal")
            print("option c: Kolkatta")
            print("option d: Delhi")
            ans=input("enter your answer 1/2/3/4 :")
            if ans=="4":
                sum +=16000
                print("your answer is correct")
            else:
                print("your answer is incorrect")
print("your total score is :",sum)
print("Samay samapti ki ghoshna")