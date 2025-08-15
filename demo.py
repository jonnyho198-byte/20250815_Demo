import numpy as np
import pandas as pd
import streamlit as st

st.title("HELLO TAIWAN")
st.write("123")
st.write("## 123")
st.write("# 123")
st.write("## 123")
st.write("### 123")
st.write("#### 123")
st.write("##### 123")
st.write("###### 123")

arr1= np.array([1,2,3,4,5,6])
st.write(arr1)

df1=pd.DataFrame([[11,22,33,44],[50,60,70,80]])
st.write(df1)
st.table(df1)

st.write("## 核取方塊")
r1 = st.checkbox("外帶")
if r1:
    st.info("外帶") 
else:
    st.info("內用")

check = st.columns(2)
txt = ''
with check[0]:
    r11 = st.checkbox("A")
    if r11:
       txt+=" A "
with check[1]:
    r12 = st.checkbox("B")
    if r12:
       txt+=" B "
st.info(txt)

st.write("## 選項按鈕")
b1 = st.radio("飲料:",("咖啡",'果汁','奶茶'))
st.info(b1)

b2 = st.radio("飲料:",("咖啡",'果汁','奶茶'),key="b2")
st.info(b2)

st.write("## 滑桿")
rum = st.slider("請選擇數量:",1.0,5.0,0.5)
st.info(rum)

st.sidebar.write("## 下拉選單")
city = st.sidebar.selectbox("居住地",("台北","台南","其他"))
if city=="台北":
    st.sidebar.info("A")
if city=="台南":
    st.sidebar.info("D")
else:
    st.sidebar.info("OTHERS")

st.write("## 按鈕")
a = st.number_input("num...")
b = st.number_input("num...",key='b')
if st.button("相加"):
    st.write("### ",a+b)