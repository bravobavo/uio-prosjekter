"""This is a calculator"""
import time

# Functions
def plus(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Loop
while True:
    # Variables
    index = 0
    tall1 = ""
    tall2 = ""
    metode = ""
    forrige = 0
    inputShit = raw_input("Gi oss et regnestykke paa formen x[*,/,+,-]y\n")
    for value in inputShit:
        try:
            # Er det et tall?
            int(value)
        except ValueError:
            # Det er ikke et tall, da sjekker vi om det er en operator
            if value == "+" or value == "-" or value == "*" or value == "/":
                metode = value
                tall1 = int(inputShit[0:index])
                forrige = index
            else:
                # SHIT det er ikke en operator, vi maa avslutte
                error = "Sorry {} er ikke et stottet tegn".format(value)
                raise ValueError(error)
        index = index + 1

    tall2 = int(inputShit[forrige+1:])
    print "%s %s %s ER..." % (tall1, metode, tall2)
    time.sleep(2)

    if metode == "+":
        print plus(tall1, tall2)
    elif metode == "-":
        print subtract(tall1, tall2)
    elif metode == "*":
        print multiply(tall1, tall2)
    elif metode == "/":
        print divide(tall1, tall2)
