import streamlit as st
import pickle
import numpy as np

# Streamlit Title and Description
st.title("Book Recommendation System 📚")
st.write("Get personalized book recommendations!")

# Load Artifacts with Error Handling
try:
    model = pickle.load(open('artifacts/model.pkl', 'rb'))
    book_name = pickle.load(open('artifacts/book_name.pkl', 'rb'))
    book_data_df = pickle.load(open('artifacts/book_data_df.pkl', 'rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# Recommendation Function
def recommend_book(book_name):
    try:
        # Find the index of the book in the pivot table
        book_id = np.where(book_pivot.index == book_name)[0][0]
    except IndexError:
        st.error(f"The book '{book_name}' was not found in the dataset.")
        return []

    # Get distances and suggestions using the trained model
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    # Collect recommended books
    recommended_books = []
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            recommended_books.append(j)

    # Remove the original book from recommendations if present
    if book_name in recommended_books:
        recommended_books.remove(book_name)

    return recommended_books

# User Input in Streamlit
selected_book = st.selectbox("Select a book you like:", book_name)

# Display Recommendations on Button Click
if st.button("Show Recommendations"):
    recommendations = recommend_book(selected_book)

    if recommendations:
        st.subheader("Books you might like:")
        for i, book in enumerate(recommendations, 1):
            st.write(f"{i}. {book}")
    else:
        st.warning("No recommendations found.")
