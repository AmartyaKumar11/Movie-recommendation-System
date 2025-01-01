import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c0f37493ef9c3bccf0d6b0bdb8906a1b&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return "https://via.placeholder.com/500"  # Placeholder image if no poster is found

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Ensure 'movie_id' is a column in your DataFrame
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

# Load the movies dictionary and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit App
st.title('🎬 Movie Recommender System')

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

# Display recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.subheader('Here are the recommended movies:')

    # Create a grid layout for recommendations
    for i in range(0, len(names), 2):  # Two items per row
        cols = st.columns(2)  # Create two columns per row
        for col, name, poster in zip(cols, names[i:i+2], posters[i:i+2]):
            with col:
                st.image(poster, use_container_width=True)
                st.write(f"**{name}**")
