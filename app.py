import streamlit as st
import pickle
import numpy as np

pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

company=st.selectbox('Brand',df['Company'].unique())

type=st.selectbox('Type',df['TypeName'].unique())
ram=st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])
weight=st.number_input('weight of the laptop')
touchscreen=st.selectbox('Touchscreen',['No','Yes'])
ips=st.selectbox('IPS',['No','Yes'])
screen_size=st.number_input('Screen Size',value=15.6)
resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x900','3848x1800','2880x1800','2560x1600','2560x1440'])
cpu=st.selectbox('CPU',df['Cpu brand'].unique())
hdd=st.selectbox('HDD(in GB)',[0,128,256,512,102,2089])
ssd=st.selectbox('SSD(in GB)',[0,128,256,512,102,2089])
gpu=st.selectbox('GPU',df['Gpu Brand'].unique())
os=st.selectbox('os',df['os'].unique())
if st.button('Predict Price'):

    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='Yes':
        ips=1
    else:
        ips=0
    X_res=int(resolution.split('x')[0])
    Y_res=int(resolution.split('x')[1])

    ppi=((X_res**2)+(Y_res**2))**1/2/screen_size
    query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query=query.reshape(1,12)
    st.title("The Predicted Price is " + str(int(np.exp(pipe.predict(query)))))