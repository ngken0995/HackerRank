from statistics import mean 

class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstname = firstName
    self.lastname = lastName
    self.idNumber = idNumber

  def printPerson(self):
	  print("Name:", self.lastName + ",", self.firstName)
	  print("ID:", self.idNumber)
    
class Student(Person):
  
  def __init__(self,firstName, lastName, idNumber, scores):
    Person.__init__(self, firstName, lastName, idNumber)
    self.scores = scores

  def calculate(self):
    if 90<= mean(scores)<=100:
      return 'O'
    elif 80<= mean(scores) < 90:
      return 'E'
    elif 70 <= mean(scores) < 80:
      return 'A'
    elif 55 <= mean(scores) < 70:
      return 'P'
    elif 40 <= mean(scores) < 55:
      return 'D'
    else:
      return 'T' 

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
