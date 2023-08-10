import time

def multiply_turing(n,m):
    TAB = "\t"

    tape = ""
    pointer = 1
    counter = 1
    
    
    currentState = 0
    states = {
        0: {"1": "X,R,1", "*": "*,L,6"},
        1: {"1": "1,R,0", "*": "*,R,1"},
        2: {"1": "⊥,R,1", "=": "=,L,3"},
        3: {"1": "1,R,0", "=": "=,R,0", "^": "1,0,1"},
        4: {"1": "1,L,0", "=": "=,L,0", "⊥": "⊥,R,-2"},
        5: {"1": "1,L,0", "*": "*,L,0", "⊥": "1,L,0", "X": "X,R,-5"},
        6: {"X": "1,L,0", "^": "^,R,1"}
    }

    # Setup tape
    # Initial ^ character
    tape += "^"
    for x in range(n):
        tape += "1"

    # Adding separator character
    tape += "*"

    # Adding the 0's that represent m
    for x in range(m):
        tape += "1"

    # Adding separator character
    tape += "="

    # Adding the needed amount of ^ characters to the tape
    amount = m * n + 1
    for x in range(amount):
        tape += "^"

    # Convert tape to list for multiplication
    tape = list(tape)
    start = time.time()

    while currentState in states:

        # Find the current charracter we are dealing with
        currentCharacter = tape[pointer]
        # Find the correct transition for the character @ the currentState from the states dictionary
        transition = (states[currentState][currentCharacter])

        transition = transition.split(",")

        # Re-write rule
        tape[pointer] = transition[0]
        # Move pointer
        if transition[1] == "R":
            pointer += 1
        elif transition[1] == "L":
            pointer -= 1
        
        currentState += int(transition[2])

        # Increment counter for number of tapes produced
        counter += 1


    # Computation completed, displaying results below
    end = time.time()

    # Convert tape back to string for output
    final_tape = "".join(tape)
    final_tape = final_tape.split("=")[1]
    x = len(final_tape)

    result = final_tape.count("1")
    return result


def main():
    
    n=int(input())
    n=multiply_turing(3,n)
    result = 1
    for i in range(1,n+1):
        result=multiply_turing(result,i)
        
    result=multiply_turing(result,2)
    
    print(result)    

main()
