#print welcome message for quiz
print("welcome to my quiz!")
# create var playing to take input asking user to play
play = input("would you like to take my quiz? ")

# if var  is not equal yes then quit
if play.lower() != 'yes':
    quit()

#print okay lets play
print("lets begin the quiz")
# score = 0
score = 0



answer = input("what does cpu mean: ")

if answer.lower() == 'central processing unit':
    print("correct")
    score += 1
else:
    print("incorrect")


#else then print incorrect decrement score by  - 1
# answer what does gpu stand for?
# if answer equals graphics processing unit then print correct increment score by 1
# else then print incorrect decrement score by  - 1
answer = input("what does gpu mean: ")

if answer.lower() == 'graphic processing unit':
    print("correct")
    score += 1
else:
    print("incorrect")


# answer what does ram stand for?
# if answer equals random access memory then print correct increment score by 1
# else then print incorrect decrement score by  - 1

answer = input("what does ram mean: ")

if answer.lower() == 'random access memory':
    print("correct")
    score += 1
else:
    print("incorrect")


print("you finished the quiz your score is: ", score)
print ("your score as percent: ", (score /3)* 100,"%")
# print score make sure to convert to string
# print percent score//3  100


