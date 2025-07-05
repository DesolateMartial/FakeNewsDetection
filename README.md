# 📰 Fake News Detection System

This project is a Fake News Detection web app built using **Flask** and **Machine Learning**. It classifies news articles as **FAKE** or **REAL** based on the content.

## 📂 Features
- Train a Logistic Regression model using TF-IDF vectorization
- Use real-world news data
- Simple web interface to enter custom news text
- Real-time classification

## 🔧 Installation
```bash
# Clone the repository
https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Run the web app
cd app
python app.py
```

## 📊 Dataset
Used: [Kaggle Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

## 📁 Project Structure
```
fake-news-detector/
├── data/
│   └── fake_or_real_news.csv
├── models/
│   └── logistic_model.pkl
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
├── train_model.py
├── requirements.txt
└── README.md
```

## 🧠 Model
- TF-IDF for vectorization
- Logistic Regression for classification

## 📜 License
MIT License
