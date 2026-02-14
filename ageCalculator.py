# # Requirment : 1. install straemlit
# >>>>>>>>>>>>2.install  relativedelta
# >>>>>>>>>>>>>>>3. install  dateutil
# Run : streamlit run filename

import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import date
from PIL import Image


img = Image.open("AGE.webp")
st.image(img,width=800)

# title of Project st.title () and if using html st.markdown (use value : unsafe_allow_html =bool value)
st.markdown (""" <h1 style = "text-align:center;"> Age Calculattor </h1>""",unsafe_allow_html=True)

# Styling for the container layout 

# st.markdown("""<style>
#     .main-Container {
#         background-color: #FFF5F2; /* Light peach/pink background */
#         padding: 30px;
#         border-radius: 10px;
#         border: 1px solid #FADBD8;
#         text-align: center;
#     }
#     </style>""", unsafe_allow_html=True)
st.markdown("""<style>
    /* This targets the 'group' of items inside your container */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        background-color: #FFF5F2; 
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #FADBD8;
    }
    </style>""", unsafe_allow_html=True)

# Use container 
with st.container(border=True):
    
    # st.markdown('<div class= "main-Container">',unsafe_allow_html=True)

  # date of birth function 
    dob = st.date_input(
    "Enter Your Age :" ,
    # set minimum year,month and date
    min_value= date (1990,1,1), 
    # set maximum year, month, date
    max_value= date.today(),
    value= date(2000, 1, 1)
    )

# button for check age 
    if st.button ("CALCULATE"):
       today = date.today()
       age = relativedelta(today, dob)
       st.success (f"Hello  user your year {age.years}, Months {age.months} and day {age.days}")

    # st.markdown('</div>',unsafe_allow_html=True)  