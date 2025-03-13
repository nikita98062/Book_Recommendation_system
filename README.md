# Book Recommendation System 📚

A sophisticated machine learning-based system that provides personalized book recommendations to users based on their preferences and reading history.

## Features ✨

- **Content-Based Filtering**: Recommends books based on book descriptions, authors, and genres
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- **Real-Time Recommendations**: Instant book suggestions as you input preferences
- **Detailed Book Information**: View book covers, ratings, and descriptions
- **Search Functionality**: Easy search for books by title or author
- **Rating System**: Rate books and get better personalized recommendations

## Live Demo 🌐

[Book Recommendation System](https://bookrecommendationsystem-dhkrovxqssdnkjcjbo95ue.streamlit.app/)

## Technologies Used 🛠️

- Python 3.8+
- Streamlit
- Pandas
- Scikit-learn
- NLTK
- NumPy

## Installation 💻

1. Clone the repository
```bash
git clone https://github.com/yourusername/Book_Recommendation_system.git
cd Book_Recommendation_system
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage 🚀

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Screenshots 📸

![App Screenshot](demo.png)

## Dataset 📊

The system uses a comprehensive dataset containing:
- 10,000+ books
- User ratings
- Book metadata (title, author, genre, etc.)

## How It Works 🔍

1. **Data Preprocessing**
   - Text cleaning and normalization
   - Feature extraction from book descriptions
   - Handling missing values

2. **Recommendation Engine**
   - Content-based filtering using TF-IDF
   - Cosine similarity calculations
   - Book feature vector generation

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📫

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/Book_Recommendation_system](https://github.com/yourusername/Book_Recommendation_system)

## Acknowledgments 🙏

- Dataset source
- Contributing libraries
- Inspiration