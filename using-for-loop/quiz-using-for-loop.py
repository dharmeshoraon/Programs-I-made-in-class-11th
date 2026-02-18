import random
def gk_quiz():
    questions=[
        ("Who is the father of nation?","Mahatma Gandhi"),
        ("what is the capital of India?","New Delhi"),
        ("Who wrote the national anthem?","Rabindranath Tagore"),
        ("What is the highest honour of India?","Bharat Ratna"),
        ("Why Indian Ocean is called so?","Because it is surrounded by India, It has the largest coastline")
    ]
    random.shuffle(questions)
    score=0
    for q,a in questions:
        ans=input(q+" ")
        if ans.lower()==a.lower():
            print("Correct")
            score+=1
    return score
def remark(score):
    if score==5:
        return "Excellent"
    elif score>=3:
        return "Good"
    else:
        return "Better luck next time"
score=gk_quiz()
remark(score)
print(f"Your score is {score}/5. {remark(score)}")