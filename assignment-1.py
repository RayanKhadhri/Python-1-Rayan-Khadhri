grade = 0
# This section is for calculating the grade for labs
labs = int(input("Enter the number of labs completed: "))
if labs > 6:
    labs = 6
if labs < 0:
     labs = 0
def labgrade(labs:int) -> float :
     return ((labs / 6) * 100) * 0.2
grade += labgrade(labs)

# This section is for calculating the grade for quizzes
quizzes = int(input("Enter the number of quizzes completed: "))
if quizzes > 6:
     quizzes = 6
if quizzes < 0:
     quizzes = 0
def quizzgrade(quizzes:int) -> float:
     return ((quizzes / 6) * 100) * 0.15
grade += quizzgrade(quizzes)

# This section is for calculating the grade for the assignments
ass1 = float(input("Enter grade for Assignment 1: "))
ass2 = float(input("Enter grade for Assignment 2: "))
ass3 = float(input("Enter grade for Assignment 3: "))
ass4 = float(input("Enter grade for Assignment 4: "))
def assgrade(ass1:float, ass2:float, ass3:float, ass4:float) -> float:
     return ((ass1 + ass2 + ass3 + ass4) / 4) * 0.16
grade += assgrade(ass1, ass2, ass3, ass4)

# This section is for calculating the grade for midterms
mid1 = float(input("Enter grade for Midterm 1: "))
mid2 = float(input("Enter grade for Midterm 2: "))
def midgrade(mid1:float, mid2:float) -> float:
     return ((mid1 + mid2) / 2 ) * 0.25
grade += midgrade(mid1, mid2)

# This section is for calculating the grade for the Final
final = float(input("Enter grade for Final Exam: "))
def finalgrade(final:float) -> float:
     return (final * 0.18)
grade += finalgrade(final)

# This section is for calculating the grae for the final and midterm prep
prep = float(input("Enter grade for Midterms and Final Preperation: "))
def prepgrade(prep:float) -> float:
     return (prep * 0.06)
grade += prepgrade(prep)
round(grade)

print("Your grade is: " + str(grade))
