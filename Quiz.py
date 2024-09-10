print("Welcome to Claire's excellent quiz! You will be presented with 4 questions. Good luck!")
x = ["b", "b", "a", "y"]
points = 0
def question(b, a):
    q = input(b)
    if q == x[a]:
        print("correct!")
        return 1
    else:
        print("incorrect!")
        return 0

q1 = question("Who teaches AP physics?\na) Mr. Hodgson\nb) Mr. Tang\nc) Mr. Low\nd) Mr. Slapsys\nYour answer: ", 0)
q2 = question("Who teaches Computer Studies 10?\na) Ms. Sodhi\nb) Mr.Zaremba\nc) Ms.Reed\nd) Mr.Tang\nYour answer: ", 1)
q3 = question("Who teaches math?\na)Mr. Kwong\nb)Mr. Chu\nc) Ms. McCartin\nd) Mr. Matthews\nYour answer: ", 2)
q4 = question("Does pineapple belong on pizza (y/n)\nYour Answer: ", 3)
points = q1 + q2 + q3 + q4
print("You got", points, "points!")