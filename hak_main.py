import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import plotly.express as px

st.title("Hello, I'm Yukyung Ha")

# sidebar
st.sidebar.title('list of categories')
select_category = st.sidebar.selectbox(
    '원하시는 카테고리를 선택하세요', 
    ['diary', 'task', 'calendar']
)
tabA, tabB, tabC, tabD = st.tabs(['Task', 'Schedule','BucketList', 'FavThings'])

#map
base_position = [37.3050595, 127.1218073]
map_data = pd.DataFrame(
    np.random.randn(5,1) / [20,20] + base_position,
    columns = ['lat', 'lon'])

#loading page
with st.spinner('Wait for it...'):
    time.sleep(0.5)

#task

def task():
    task=st.text_input("Enter your task", "")
    
    if st.button("Add", key='task') :
        st.session_state["task_list"].append(task)
        
    if "task_list" not in st.session_state:
        st.session_state["task_list"]=[]

    for i, t in enumerate(st.session_state["task_list"]):
        if st.checkbox(f"{i+1}.{t}"):
            st.session_state["task_list"].remove(t)
    
def buck():
    buck=st.text_input("Enter your bucketlist", "")
    
    if st.button("Add", key='buck') :
        st.session_state["bucket_list"].append(task)
        
    if "bucket_list" not in st.session_state:
        st.session_state["bucket_list"]=[]
        
    for i, t in enumerate(st.session_state["bucket_list"]):
        if st.checkbox(f"{i+1}. {t}"):
            st.session_state["bucket_list"].remove(t)
        

with tabA:
    st.subheader("Today's task")
    task()
    
with tabB:
    st.subheader('Schedule')
    st.date_input('일정 예약')
    st.time_input('시간 선택')

with tabC:
    st.subheader('My BucketList')
    buck()
    
with tabD:
    st.subheader('My favorite places')
    st.map(map_data)
    print(map_data)
    


