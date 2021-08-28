import streamlit as st
st.set_page_config(layout="wide")
import pickle
import pandas as pd
import base64
import requests
import ast
main_bg = "white.jpg"
main_bg_ext = "jpg"

side_bg = "white.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
         
        background-repeat: no-repeat;
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
    overview2=[]
    actors=[]
    date=[]
    for i in name:
        movies_list.append(movie.iloc[i[0]].title)
        movie_poster.append(fetch_poster(movie.iloc[i[0]].movie_id))
        overview2.append(model.iloc[i[0]].overview)
        actors.append(credits.iloc[i[0]].cast)
        date.append(model.iloc[i[0]].release_date)
    return movies_list,movie_poster,overview2,actors,date
    

similiarity=pickle.load(open("similiarity",'rb'))
movie_dict=pickle.load(open('movies_dict','rb'))
movie=pd.DataFrame(movie_dict)
#this is for overview
model=pd.read_csv('tmdb_5000_movies.csv')
model=model[['overview','release_date']]
#this is for actor name
credits=pd.read_csv('tmdb_5000_credits.csv')
credits=credits[['cast']]
def for_cast(cast_name):
    list_for_cast=[]
    counter=0
    for i in ast.literal_eval(cast_name):
        if counter!=3:
            list_for_cast.append(i['name'])
            counter+=1
        else:
            break
    return list_for_cast
credits['cast']=credits['cast'].apply(for_cast)


st.text('This is a movie recommendation system, i made it for practice pupose-Munif')
st.title('Find Your Favaourite Movies')


selected_movie_name = st.selectbox(
    'Select a movie',
     (movie['title'].values))

if st.button('Reccomend'):
     names,poster,overview,actors,date=system(selected_movie_name)
     col1, col2, col3,col4,col5 = st.columns(5)
     with col1:
        # st.beta_columns([6,1])
         #st.set_page_config(layout="wide")
         st.header(names[0])
         st.image(poster[0])
         st.write(date[0])
         st.header("Overview")
         st.write(overview[0])
         #option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
         st.header("Actors")
         st.dataframe(actors[0])
     with col2:  
         st.header(names[1])
         st.image(poster[1])
         st.write(date[1])
         st.header("Overview")
         st.write(overview[1])
         st.header("Actors")
         st.write(pd.Series(actors[1], index=[1,2,3]))
     with col3:    
         st.header(names[2])
         st.image(poster[2])
         st.write(date[2])
         st.header("Overview")
         st.write(overview[2])
         st.header("Actors")
         st.write(pd.Series(actors[2], index=[1,2,3]))
          
     with col4: 
         st.header(names[3])
         st.image(poster[3])
         st.write(date[3])
         st.header("Overview")
         st.write(overview[3])
         st.header("Actors")
         st.write(pd.Series(actors[3], index=[1,2,3]))
   
     with col5:
         st.header(names[4])
         st.image(poster[4]) 
         st.write(date[4])
         st.header("Overview")
         st.write(overview[4])
         st.header("Actors")
         st.write(pd.Series(actors[4], index=[1,2,3]))
    
          
     
  
       
     
