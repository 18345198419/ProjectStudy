import os

#with open("high_score.txt", "r+") as f:
f=open("high_score.txt", "r+")
score = f.read()
print(str(score))
if not score:
    print("111")
else:
    print("22222")