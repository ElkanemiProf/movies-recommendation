import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import streamlit as st

df = pd.read_csv('movies.csv')

# selecting relevant columns for recommendation
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# replacing null values with null strings
for feature in selected_features:
    df[feature] = df[feature].fillna('')

# combining all the 5 selected features
combined_features = df['genres'] + ' ' + df['keywords'] + ' ' + df['tagline'] + ' ' + df['cast'] + ' ' + df[
    'director']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)


# Create a function to get the recommendations
def get_recommendations(movie_name):
    # creating a list of all the movies name in the dataset
    list_of_all_titles = df['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]
    index_of_the_movie = df[df.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    print('movies suggested for you: \n')

    i = 1
    movies_list = []
    no_list = ['No items matches your movie']
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = df[df.index == index]['title'].values[0]
        if (i < 30):
            movies_list.append(title_from_index)
            print(i, '.', title_from_index)
            i += 1
    if len(movies_list) ==0:
        return no_list
    else:
        return movies_list


# Create a main function
def main():
    st.title("Movie Recommendation System")

    # Get the user's movie choice
    movie_choice = st.text_input("Enter a movie title:")

    # Show the recommendations
    if st.button("Recommend"):
        recommendations = get_recommendations(movie_choice)
        st.write("Recommended Movies:")
        for recommendation in recommendations:
            st.write("- " + recommendation)


if __name__ == "__main__":
    main()
