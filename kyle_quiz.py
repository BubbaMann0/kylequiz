print ("Kyle Quiz!!!")
print ("")
input ("Press Enter to Begin")

total = 0
print ("///////////////////////")
print ("(Question 1)")
print ("what is Kyles favorite food")
print ("(A) Mac'n Cheese")
print ("(B) Souls")
print ("(C) Clam Chowder")
print ("(D) Ants")

ANS1 = input("")
if ANS1 == str("D"):
    total += int(1)
    print ("Correct!!!")
else: print ("incorrect")

print (total)

print ("///////////////////////")
print ("(Question 2)")
print ("What is Kyles Favorite Activty")
print ("(A) Screaming")
print ("(B) Feeling Authoritys")
print ("(C) Chasing the Innocent")
print ("(D) #$%&#$&#")

ANS2 = input("")
if ANS2 == str("C"):
    total += int(1)
    print ("Correct!!!")
else: print ("Incorrect")

print ("///////////////////////")
print ("(Question 3)")
print ("What is Kyles Favorite Thing to do in Chesterton")
print ("(A) Nothing (There is nothing to do in Chesterton)")
print ("(B) going to Caitlyn's house")
print ("(C) Crime")
print ("(D) looking for ants")

ANS3 = input("")
if ANS3 == str("C"):
    total += int(1)
    print ("Correct!!!")
else: print ("incorrect")

print ("///////////////////////")
print ("(Question 4)")
print ("What is Kyle Attracted to")
print ("(A) Men")
print ("(B) Other genders")

ANS4 = input("")
if ANS4 == str("A"):
    total += int(1)
    print ("Correct!!!")
else: print ("Incorrect")

print ("///////////////////////")
print ("(Question 5)")
print ("Who is Kyles Favorite Person")
print ("(A) Caitlyn")
print ("(B) Javiar")
print ("(C) Bob Even")
print ("(D) Aaron")

ANS5 = input("")
if ANS5 == str("C"):
    total += int(1)
    print ("Correct!!!")
else: print ("Incorrect")

print ("///////////////////////")
print ("(Question 6)")
print ("What was Kyles Original Name")
print ("(A) Milk Boy")
print ("(B) Big Bubba")
print ("(C) Uncle Cletus")
print ("(D) Cousin Skeeter")

ANS6 = input("")
if ANS6 == str("B"):
    total += int(1)
    print ("Correct!!!")
else: print ("Incorrect")

print ("///////////////////////")
print ("(Question 7)")
print ("How do I Stop the Screaming")
print ("(A) Feed on the Innocent")
print ("(B) Seek Proffesional Help")
print ("(C) Do Mental Health Excersizes")
print ("(D) Start Going to Therapy")

ANS7 = input("")
if ANS7 == str("A"):
    total += int(1)
    print ("Correct!!!")
else: print ("Incorrect")

print ("///////////////////////")
print("Your Score is", total,"/7")
print("")

if total == int(1) or int(0):
    print ("You are a Disappointment")
elif total == int(2) or int(3):
    print ("Clearly we are not really Friends")
elif total == int(4) or int(5):
    print ("Good Job!")
elif total == int(6):
    print ("Very Good!")
else: print ("Perfect Score!")

input ("Press Enter to Close")



