#word =input("enter a word:")
#list=[]
#for i in range(len(word)):
 #   list.append(word[i].lower())
    
#for letter in list:
#    guess =input("ente a single letter:")
 #   if letter==f'{guess}':
  #      print("correct")
   #     break
    #else:
     #   print("try again")
#students ={"harshit","harsh","vishesh"}
#student = input("enter the name of students:")
#if student in students:
 #   print(f"{student} is in the list")
#else:
 #   print(f"{student}is not in the list")
grades ={"harshit":"A",
         "rudra":"B",
         "harsh":"C",
         "vishesh":"D"}
student= input("enter the name of the students:")
if student in grades:
    print(f"{student}' grade is {grades[student]}")
else:
    print(f"{student} was not found")
