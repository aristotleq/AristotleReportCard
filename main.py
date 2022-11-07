################ Functions ################

# Function shows the user a menu of options they have
def displayMenu():

  print("1. Add a Student")
  print("2. Remove a Student")
  print("3. Add Quiz Grade for Student")
  print("4. List a Student's Quiz Grades")
  print("5. Get Student's Letter Grade")
  print("6. Quit")


# Function prompts user to enter a new student
def addingAStudent():
  
  studentName = input("Enter a student name: ")
  studentName = studentName.capitalize()
  # statement below creates appendable list within dictionary
  studentDict[studentName] = []
  print(f"{studentName} added!")
  

# Function involves you removing a pair from a dictionary  
def removeAStudent():

  studentName = input("Enter a student name: ")
  studentName = studentName.capitalize()
  if studentName not in studentDict:
    print(f"{studentName} not in dictionary!")
  else:
    studentDict.pop(studentName)
    print(f"{studentName} removed!")
    

# Function grabs a student from dictionary and adds a quiz grade to list
def addQuizGradeForStudent():
  
  studentName = input("Enter a student name: ")
  studentName = studentName.capitalize()
  if studentName not in studentDict:
    print(f"{studentName} not in dictionary!")
  else:
    studentGrade = getNumberGradeFromUser()    
    # studentDict[studentName] = studentGrade <- creates value, doesn't append
    studentDict[studentName].append(studentGrade)
    print(f"Added {studentGrade} to {studentName}'s quizzes")
    

# Function lists all of the grades for a student
def listStudentQuizGrades():
  
  studentName = input("Enter a student name: ") 
  studentName = studentName.capitalize()
  if studentName not in studentDict:
    print()
    print(f"{studentName} not in dictionary!")
  else:
    print()
    print(f"{studentName}'s Quizzes: ")
    for x in studentDict[studentName]:  
      # x = studentDict[studentName] <- reminder how to access value
      print(x)     
       

# Function prompts the user to enter a numeric grade
# Function verifies the user entered a valid float for the grade
def getNumberGradeFromUser():
  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val
  

# Function takes listed grades, calculates average, matches, and displays corresponding letter grade
def displayLetterGradeFromUser():
  
  sum = 0
  studentGrade2 = 0
  studentName = input("Enter a student name: ") 
  studentName = studentName.capitalize()
  if studentName not in studentDict:
    print(f"{studentName} not in dictionary!")
  else:
    for y in studentDict[studentName]:
      sum += y 
      z = len(studentDict[studentName])
      studentGrade2 = sum / z
      
  studentGrade2 = float(studentGrade2)
    
  if studentGrade2 >= 90:
    print(f"{studentName}'s current grade is an A")
  if studentGrade2 >= 80 and studentGrade2 < 90:
    print(f"{studentName}'s current grade is a B")
  if studentGrade2 >= 70 and studentGrade2 < 80:
    print(f"{studentName}'s current grade is a C")
  if studentGrade2 >= 60 and studentGrade2 < 70:
    print(f"{studentName}'s current grade is a D")
  if studentGrade2 >= 50 and studentGrade2 < 60:
    print(f"{studentName}'s current grade is an E")
  if studentGrade2 < 50:
    print(f"{studentName}'s current grade is a F")


################ Main Program ################

menuOption =  ""
studentName = ""
studentDict = {}
studentGrade = 0
val = 0
  
# Menu options loop
while(menuOption != "Quit"):

  print()
  displayMenu()  
  print()
  # Prompt the user to select an option
  menuOption = input("Select an option: ")
  if menuOption == "1":
    addingAStudent()
  if menuOption == "2":
    removeAStudent()
  if menuOption == "3":
    addQuizGradeForStudent()
  if menuOption == "4":
    listStudentQuizGrades()
  if menuOption == "5":
    displayLetterGradeFromUser()
  if menuOption == "6":
    print("Exiting..")
    menuOption = "Quit"  
  