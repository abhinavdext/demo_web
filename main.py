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

st.text('Welcome to quiz')
answer = input('Ready to play the quiz? (yes/no) :')
score = 0
total_question = 3

if answer.lower()=='yes':
    answer = input('Question 1: what is you Favarate programming language?')
    if answer.lower()=='python':
        score+=1
        print('correct')
    else:
        print('wrong answer :(')
    
    answer = input('Question 2: Do you follow any author on python? ')
    if answer.lower()=='yes':
        score+=1
        print('correct')
    else:
        print('wrong answer :(')
    
    answer = input('Question 3: what is your favourite website for learning python?')
    if answer.lower()=='abhinavpandey':
        score+=1
        print('correct')
    else:
        print('wrong answer :(')

print('thank you for playing this game quiz, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:', mark)
print('BYE!')
    









