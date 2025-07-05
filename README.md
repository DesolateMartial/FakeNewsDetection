# 📰 Fake News Detection System

This project is a machine learning-based web application that detects whether a news article is **fake** or **real** based on its content.

## 🚀 Features
- Train a text classification model using TF-IDF and Logistic Regression
- Input raw news text and classify it in real-time
- Lightweight Flask web interface

## 🧰 Tech Stack
- Python
- Flask (Web framework)
- scikit-learn (Machine Learning)
- pandas (Data handling)
- joblib (Model persistence)

## 📁 Folder Structure
```
fake-news-detector/
├── data/                     # Dataset CSV (to be added)
├── models/                   # Trained ML model (generated after training)
├── app/                      # Flask web application
│   ├── app.py
│   └── templates/
│       └── index.html
├── train_model.py            # Model training script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 📦 Installation
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. **Install the dependencies**
```bash
pip install -r requirements.txt
```

4. **Add the dataset**
Download the dataset from [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset) and place `fake_or_real_news.csv` inside the `data/` directory.

5. **Train the model**
```bash
python train_model.py
```

6. **Run the web app**
```bash
cd app
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to use the app.

## 📊 Dataset
- **Source**: Kaggle
- **Link**: https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

## 📜 License
MIT License
