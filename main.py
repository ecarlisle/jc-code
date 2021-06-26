correct_answer1 = "5"
answer1 = input("what is 2 + 3? ")
correct_answer2 = "15"
correct_answer3 = "bugs bunny"


if answer1 == correct_answer1:
  print("Correct! Let's try another one!")
  answer2 = input("What is 5 x 3? ")
  if answer2 == correct_answer2:
    print("Correct! Let's do one more question.")
    answer3 = input("Who says 'What's up, doc?' ")
    if answer3.lower() == correct_answer3:
        print("Correct you passed the test!!!")
    else:
      print("Incorrect")
  else:
    print("Incorrect")
else:
  print("Incorrect")
