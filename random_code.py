import streamlit as st
import pandas as pd

# Description
st.title('Random your choices -3-')
st.markdown(""" When ya cannot pick anything on your own, just depend on ya luck. """)
number = st.text_input(label = 'Your options') #number of choice

df = pd.DataFrame(columns = ['ID', 'CHOICE'])
count = list()
#print(df)

choice_num = int(number)
for i in range(choice_num):
    name_ch = st.text_input(label = 'Your options')
    df = df.append({'ID': i+1,  'CHOICE': name_ch}, ignore_index=True)
    count.append(i)
st.write(df)



