import streamlit as st
import datetime

x = datetime.datetime.now()
print('date and time = ',x)

st.title('Abhinav Pandey')


st.info("Introduction")
#st.button("About", type="primary")
if(st.button("About", type='primary')):
    #st.text("intro")
    st.markdown("To work with perseverance,measuring up to the expectation of the company and Interested to working team environment and contributing to the objectives of organization that offers a challenging and opportunity as a Python Developer.")
    

#st.subheader("To work with perseverance,measuring up to the expectation of the company and Interested to workin team environment and contributing to the objectives of organization that offers a challenging and opportunity as a Python Developer.")
    
    st.markdown("Around 5+ years of relevant experience as a Web/Application Developer and coding with analytical programming using Python, Django. Good Experience on Automation Testing using API Automation using Python and UI Automation Experienced with full software development life-cycle,architecting scalable platforms,object-oriented programming,database design and agile methodologies.")

    st.markdown("Involved in Analysis, Design, Coding, Modifications and Implementations of user requirements.")

    st.header('Technical skills')

    st.markdown('Web Frameworks = Django,Flask   \n   Web Technologies = Html,css  \n    Programming Language = Python  \nVersion Control = Git, GitHub  \n  Database = SQL, MongoDB, MySQL  \nIDEs/ Development Tool = Vs Code, PyCharm, Eclipse, Visual Studio, PyScripter  \nOperating Systems = Windows, Linux  \nTesting Tools = Postman, selenium  \nIssue Tracker = jira')

# BMI CALCULATOR 
st.title('Welcome to BMI Calculator')

weight = st.number_input("Enter your weight (in kgs)")
 
status = st.radio('Select your height format: ',

                  ('cms', 'meters', 'feet'))
 
if(status == 'cms'):


    height = st.number_input('Centimeters')
 

    try:

        bmi = weight / ((height/100)**2)

    except:

        st.text("Enter some value of height")
 

elif(status == 'meters'):

    height = st.number_input('Meters')
 

    try:

        bmi = weight / (height ** 2)

    except:

        st.text("Enter some value of height")
 

else:

    height = st.number_input('Feet')

    try:

        bmi = weight / (((height/3.28))**2)

    except:

        st.text("Enter some value of height")
 
if(st.button('Calculate BMI')):
 
    st.text("Your BMI Index is {}.".format(bmi))
 
    if(bmi < 16):

        st.error("You are Extremely Underweight")

    elif(bmi >= 16 and bmi < 18.5):

        st.warning("You are Underweight")

    elif(bmi >= 18.5 and bmi < 25):

        st.success("Healthy")

    elif(bmi >= 25 and bmi < 30):

        st.warning("Overweight")

    elif(bmi >= 30):

        st.error("Extremely Overweight")

st. write("<a href='   https://x.com/avhinavpandey?t=3aU7VK3Zelqhewv9D1158w&s=09 ' id='my-link'>twitter</a>", unsafe_allow_html=True)

#######

st.text('game')

import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the current board state is a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# Function to get a list of available moves
def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# Function to evaluate the board state for the minimax algorithm
def evaluate(board):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif check_tie(board):
        return 0
    else:
        return None

# Minimax algorithm implementation
def minimax(board, depth, maximizing_player):
    if depth == 0 or evaluate(board) is not None:
        return evaluate(board)

    if maximizing_player:
        max_eval = float("-inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            eval = minimax(board, depth - 1, False)
            board[move[0]][move[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "O"
            eval = minimax(board, depth - 1, True)
            board[move[0]][move[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval

# Function to make the AI's move using the minimax algorithm
def ai_move(board):
    best_move = None
    best_eval = float("-inf")
    for move in available_moves(board):
        board[move[0]][move[1]] = "X"
        eval = minimax(board, 9, False)
        board[move[0]][move[1]] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
    board[best_move[0]][best_move[1]] = "X"

# Main function to run the game
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "O"
        print_board(board)

        # Check for player win or tie
        if check_win(board, "O"):
            print("Congratulations! You win!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_move(board)
        print_board(board)

        # Check for AI win or tie
        if check_win(board, "X"):
            print("AI wins! Better luck next time.")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
            
