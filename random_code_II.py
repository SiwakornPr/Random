import streamlit as st
import pandas as pd
import random as rd
from stqdm import stqdm
from time import sleep

#open localhost with auto reload
### streamlit run random_code.py --server.port 80 config runOnSave true ###
##Note: There are many configs. https://docs.streamlit.io/en/stable/streamlit_configuration.html

# Description
st.title('Random your choices -3-')

#Heading
"""
## When ya cannot pick anything on your own, just depend on ya luck.
"""


## Input stage
st.markdown('Please input your options with (,) to separate your choices (///v///)')
text = st.text_input(label = 'Input example: a,b,c') #number of choice


## Data aggregation
df = pd.DataFrame(columns = ['ID', 'CHOICE'])
count = list()
df_input = dict() #pandas
data_chart = list()
#print(df)
choice = text.split(',')
num_choice = len(choice)
num_result = st.number_input(label = 'Number of the result', min_value = 1, max_value = num_choice, step= 1)
if num_result > 1:
    probability = (1/num_choice) * num_result
else:
    probability = 1/num_choice
#print(choice)

## 
for i in range(num_choice):
    chart_input = {"value": '', "name": ''}
    df_input[i+1] = choice[i].strip()
    chart_input["value"], chart_input["name"] = probability, choice[i]
    data_chart.append(chart_input)
#print(df_input)
#print(data_chart)
#st.write(data_chart)
for k, v in df_input.items():
    df = df.append({'ID': k,  'CHOICE': v}, ignore_index=True)
#print(df) #df as pandas
st.write(df)


##chart input preparation

## chart
from streamlit_echarts import st_echarts
#col1 = st.beta_columns([1])
#with col1:
option = {
                "tooltip": {"trigger": 'item'},
                "legend": {"top": '0%', "left": 'center'},
                "series": [
                     {"name": 'Probability',
                      "type": 'pie',
                      "radius": ['40%', "75%"],

                      "avoidLabelOverlap": "false",
                      "itemstyle": {"borderRadius": "10",
                                    "borderColor": '#fff',
                                    "borderwidth": "2"},
                      #"label": {"show": "false",
                                #"position": 'none'},
                      "emphasis": {"label": {"show": "true",
                                             "fontSize": '30',
                                             "fontWeight": 'bold'}
                                   },
                      "labelline": {"show": "true"},
                      "data": data_chart
                      }
                 ]
              }
st_echarts(options=option, key = "1")



## random stage
def random(contribute, n):
    result_list = list()
    random_list = contribute #list without replacement
    for i in range(n):
        result = rd.choice(random_list)
        result_list.append(result)
        random_list.remove(result)
    return result_list

st.markdown('Just click!')
if st.button("RANDOM CONFIRM!!!"):
    stqdm.pandas()
    pd.Series(range(100)).progress_map(lambda x: sleep(0.015))
    #pd.DataFrame({"a": range(100)}).progress_apply(lambda x: sleep(0.01), axis=1)
    print_result = random(choice, num_result) #using choice list
    """ ## Your choice is """
    n = 0
    for i in print_result:
        n = n+1
        st.write(n, i)
