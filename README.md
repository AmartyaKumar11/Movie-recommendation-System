# 🎬 Movie Recommender System

A content-based movie recommendation system built with Streamlit that suggests similar movies based on your selection. The system uses TMDB API to fetch movie posters and provides visual recommendations.

## 🌟 Features

- Interactive movie selection from a curated database
- Real-time movie recommendations based on content similarity
- Movie poster visualization using TMDB API
- Responsive grid layout for recommendations
- Easy-to-use interface with Streamlit

## 🔧 Technical Architecture

- **Frontend**: Streamlit
- **Backend**: Python
- **APIs**: TMDB (The Movie Database) API
- **Machine Learning**: Content-based filtering using similarity matrices
- **Dataset**: TMDB 5000 Movie Dataset from Kaggle

## 📊 Dataset

The movie data used in this project comes from the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download) on Kaggle. This dataset includes:
- Movie metadata (title, genre, cast, crew, etc.)
- Movie ratings and popularity scores
- Over 5000 movies spanning multiple years and genres

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Local Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Set up TMDB API key
- Get your API key from [TMDB](https://www.themoviedb.org/documentation/api)
- Replace the API key in the code or set it as an environment variable

5. Run the application
```bash
streamlit run app.py
```

### Deployment Setup

The repository includes deployment files for Heroku:

- `setup.sh`: Contains Streamlit configuration
- `Procfile`: Specifies the commands to run the app
- `requirements.txt`: Lists all Python dependencies

To deploy on Heroku:

1. Create a Heroku account and install Heroku CLI
2. Login to Heroku
```bash
heroku login
```

3. Create a new Heroku app
```bash
heroku create your-app-name
```

4. Push to Heroku
```bash
git push heroku main
```

## 📁 Project Structure

```
movie-recommender/
├── app.py                # Main Streamlit application
├── movie_dict.pkl        # Preprocessed movie data
├── similarity.pkl        # Similarity matrix
├── requirements.txt      # Python dependencies
├── setup.sh             # Streamlit configuration
├── Procfile             # Heroku deployment file
└── README.md            # Project documentation
```

## 🛠️ Requirements

The main requirements are listed in `requirements.txt`:
- streamlit
- pandas
- requests
- pickle-mixin
- scikit-learn
- numpy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- TMDB for providing the movie database API
- Kaggle for providing the TMDB 5000 Movie Dataset
- Streamlit for the awesome web framework
- All contributors and supporters of the project

