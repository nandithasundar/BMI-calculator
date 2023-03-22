import streamlit as st



st.set_page_config(page_title="BMI Calculator", page_icon=":muscle:", layout="wide")
st.title("BMI index")

g = ['Male','Female']
h = ["Reading books","Blogging","Dancing","Singing","Listening to music",
        "Playing musical instruments","Learning new languages", "Shopping","Traveling",
        "Hiking","Exercising","Drawing","Cooking","Gardening","Walking","Fishing","Photography"]

with st.form(key="form1"):
    name = st.text_input(label="Name")
    gender = st.radio('Gender', g)
    age = st.slider("Age:",min_value=1, max_value=100)
    address = st.text_input(label="Address")
    hobbies = st.multiselect("Hobbies", h)
    weight = st.number_input('Weight in kg:')
    height = st.number_input('Height in cms: ')
    submit = st.form_submit_button(label="Submit")

if(submit):
    if(gender == 'Male'):
        st.subheader("Hello Mr.{}".format(name))
    else:
        st.subheader("Hello Ms.{}".format(name))

    bmi = weight / (height/100)**2

    st.success(f"Your BMI is {bmi}")

    if bmi <= 18.5:
        st.write("Oops! You are underweight.")
    elif bmi <= 24.9:
        st.write("Awesome! You are healthy.")
    elif bmi <= 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")




