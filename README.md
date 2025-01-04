# movies-recommendation is an app that recommends movies for you based on what you have watched. Was deployed with streamlit. 
## This project implements a Movie Recommendation System using Python and Streamlit. The system takes a user's input of a movie title and suggests similar movies based on content features such as genres, keywords, tagline, cast, and director. Here's how it works:

1. Data Preprocessing: It reads a dataset (movies.csv) and processes key columns by combining their information into a single text feature.


2. Feature Extraction: The combined features are transformed into numerical vectors using TF-IDF Vectorization to measure the importance of words.


3. Similarity Calculation: It computes the similarity scores between movies using cosine similarity, which identifies the closeness of movies based on their features.


4. Recommendation Logic: The system finds the closest match to the user's input and recommends up to 30 similar movies ranked by similarity scores.


5. Streamlit Integration: The app provides a user-friendly interface where users can input a movie title, click a button, and view a list of recommended movies.
