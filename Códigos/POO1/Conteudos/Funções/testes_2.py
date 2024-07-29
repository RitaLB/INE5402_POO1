def yesornorec(nota):
    """This function tells you if you'll need to take rec exams or not. 
    If you'll do, tells you what grade you need to achieve to be succeed in the course"""

    def notarec(nota):
        """
        This function tells you the minimum grade 
        you need to achieve to be succeed 
        in the course
        """
        nota = int(nota)
        MinGrade = 12-nota
        
        print("You need to achieve at least {} to be succeeded in your course." .format(MinGrade))



    if int(nota) <= 6:
        return notarec(nota)
    else:
        return "You are safe, go lay on the beach"

mygrade = int(input("Type your grade:"))

print(yesornorec(mygrade))