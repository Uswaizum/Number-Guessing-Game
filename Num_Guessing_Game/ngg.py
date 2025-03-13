import streamlit as st 
import random

#logic building
def Num_Guessing_Game(user_value,comp_value):
    if user_value > 20 or user_value < 1: 
        st.write("Please Enter a correct value")
        st.write(f"User Value:{user_value}")
        st.write(f"Comp Value:{comp_value}")
        
    elif user_value == comp_value:
        st.write("You Win!")
        st.write(f"User Value:{user_value}")
        st.write(f"Comp Value:{comp_value}")

    elif user_value > comp_value:
         st.write("Your value is greater than computer value!")
         st.write(f"User Value:{user_value}")
         st.write(f"Comp Value:{comp_value}")

    else:
        st.write("Your value is less than computer value!")
        st.write(f"User Value:{user_value}")
        st.write(f"Comp Value:{comp_value}")
    
st.title ("Number Guessing Game")
user_value = st.number_input("Enter a value between 1-20",min_value=0)
comp_value = random.randint(1,20)
if st.button("Compute Result"):
        Num_Guessing_Game(user_value, comp_value)
