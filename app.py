from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


plt.style.use('seaborn')

@st.cache(allow_output_mutation=True)
def load_data():
    df= read_csv("googleplaystore.csv")
    return df

st.image("head.jpg")


st.sidebar.header("Project Options")

options = ['Top Categories','Rating','Total Reviews on each App',
            'Installs','Distributed value of installs on each Category',' Scatter plot on Total reviews on each app',
            'App types','Android Versions','Categories'
    
    ]

choice = st.sidebar.selectbox("select an option",options)

df =load_data()


if choice == options[0]:
    
    st.info(''' The Google Play Store apps data analysis provides enough 
    potential to drive apps making businesses to succeed. Actionable stats
    can be drawn for developers to work on and capture the Android market.
    The data set that I have taken in this article is a web
    scrapped data of 10 thousand Playstore applications to analyze the 
     android competition.''')
    st.header("Top Categories on Playstore")

    st.image("category.png")

    
    st.info('''So we got 34 category on this dataset and from those  categories , there is around 2000 app with family category, followed 
    by game category with 1200 app. And this ‘1.9’ Category,i don’t know what it is, but it only had 1 app so far, so its not visible on the graph.
    ''')
    
    
   
elif choice == options[1]:
    fig,ax=plt.subplots()
    df['Rating'].replace(to_replace=[19.0], value=[1.9],inplace=True)
    sns.distplot(df.Rating) 
    plt.title("RATINGS OF APPS")                                  
    st.pyplot(fig)

    

elif choice == options[2]:

    fig,ax=plt.subplots()
    df.head(15).plot.bar(x='App',y='Rating',figsize=(25,20),ax=ax)
    plt.title("RATINGS OF APPS")
    plt.xlabel("APPS")
    plt.ylabel("RATING")
    st.pyplot(fig)

elif choice == options[3]:
    fig,ax=plt.subplots()
    plt.figure(figsize=(12,12))
    sum_inst = df.groupby(['Category'])['installs'].sum().sort_values(ascending=False)
    sns.barplot(x=sum_inst, y=sum_inst.index, data=df,ax=ax) 
    st.pyplot(fig)

elif choice == options[4]:
    fig,ax=plt.subplots()
    df['Installs'].replace(to_replace=['0', 'Free'], value=['0+','0+'],inplace=True)
    Installs = []

    for x in df.Installs:
         x = x.replace(',', '')
         Installs.append(x[:-1])

    Installs = list(map(float, Installs))
    df['installs'] = Installs
    sns.distplot(Installs)              
    st.pyplot(fig)

elif choice == options[5]:
    fig,ax=plt.subplots()
    df.head(20).plot.scatter(x='Reviews',y='App',s=30,figsize=(18,8),color='red',ax=ax)             
    st.pyplot(fig)

elif choice == options[6]:
    fig,ax=plt.subplots()
    df.Type.unique()
    df['Type'].replace(to_replace=['0'], value=['Free'],inplace=True)
    df['Type'].fillna('Free', inplace=True)
    print(df.groupby('Category')['Type'].value_counts())
    Type_cat = df.groupby('Category')['Type'].value_counts().unstack().plot.barh(figsize=(10,20), width=0.7,ax=ax)         
    st.pyplot(fig)

elif choice == options[7]:
    fig,ax=plt.subplots()
    Type_cat = df.groupby('Category')['Android Ver'].value_counts().unstack().plot.barh(figsize=(10,18), width=1,ax=ax)         
    st.pyplot(fig)

elif choice == options[8]:
    fig,ax=plt.subplots()
    df['Category'].value_counts().head(10).plot.pie(
                             figsize=(8,7),
                             startangle=90,
                             wedgeprops={'width':.5},
                             radius=1,
                             autopct='%.1f%%',
                             pctdistance=.9,
                             
                             textprops={'color':'black'},ax=ax
)
    plt.title("CATEGORIES")             
    st.pyplot(fig)
    

elif choice == options[9]:
    fig,ax=plt.subplots()
    df['Type'].value_counts().head(10).plot.pie(
                             figsize=(8,7),
                             startangle=90,
                             wedgeprops={'width':.5},
                             radius=1,
                             autopct='%.1f%%',
                             pctdistance=.9,
                             
                             textprops={'color':'red'},ax=ax
)   
    plt.title(" APP TYPES")
    st.pyplot(fig)







