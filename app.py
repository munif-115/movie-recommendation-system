import streamlit as st
import pickle
import pandas as pd
import base64
import requests
main_bg = "im2.jpg"
main_bg_ext = "jpg"

side_bg = "im2.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8eed8ea6fd712358361b62374fef08a4&language=en-US'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def system(movie2):
    index2=movie[movie['title']==movie2].index[0]
    name=sorted(enumerate(similiarity[index2]),reverse=True,key=lambda x:x[1])[1:6]
    movies_list=[]
    movie_poster=[]
    for i in name:
        movies_list.append(movie.iloc[i[0]].title)
        movie_poster.append(fetch_poster(movie.iloc[i[0]].movie_id))
    return movies_list,movie_poster   
    

similiarity=pickle.load(open("similiarity",'rb'))
movie_dict=pickle.load(open('movies_dict','rb'))
movie=pd.DataFrame(movie_dict)

st.text('This is a movie recommendation system, i made it for practice pupose-Munif')
st.title('See Your Favaourite Movies')

selected_movie_name = st.selectbox(
    'Select a movie',
     (movie['title'].values))

if st.button('Reccomend'):
     names,poster=system(selected_movie_name)
     col1, col2, col3,col4,col5 = st.columns(5)
     with col1:
         
         st.header(names[0])
         st.image(poster[0])
     with col1:  
         st.header(names[1])
         st.image(poster[1])    
     with col1:    
         st.header(names[2])
         st.image(poster[2])      
          
     with col1: 
         st.header(names[3])
         st.image(poster[3])     
   
     with col1:
         st.header(names[4])
         st.image(poster[4])      
        
          
     
  
       
     
