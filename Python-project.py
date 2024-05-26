Question = [
    "1. Who penned the book 'Wings of Fire'?",
    "2. When is International Mother Language Day celebrated?",
    "3. Who was the first Prime Minister of India?",
    "4. Where is Gir National Forest located?",
    "5. Highest dam of India is......."
]

Options = [
    ["A.Gandhi","B.Modi","C.Abdul kalam","D.Rahul"],
    ["A.21 Feb","B,1 May","C.17 Nov","D. 1 jan"],
    ["A.Jawaharlal Nehru","B.Sardar Patel","C.Narendra Modi","D.Rahul Gandhi"],
    ["A.Ludhiyana","B.Gujarat","C.Punjab","D.Ahmedabad"],
    ["A.Sardar Dam","B.Yeldari Dam","C.Ujani Dam","D.Tehri Dam"],
]

Answer = ["C","A","A","B","D"]

w=0
r=0
total=0


for a in range(len(Question)):
    print(Question[a])
    for Option in Options[a]:
          print(Option)
    user=input("Enter your answer : ").upper()
    if user==Answer[a]:
            # print("Correct!! \n")
        w=w+1
        total +=5
    # else:
            # print("Wrong!!! \n")
        # print("incorrect! correct is",Answer[a],"\n")

print("You got", w,"Question correct Out of", len(Question),"\n")
print("Your total score is: ", total)
