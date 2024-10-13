from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
import joblib  # Для загрузки обученной модели
import os

# Получаем абсолютный путь к корню проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к файлам модели и векторизатора
model_path = os.path.join(BASE_DIR, '../model.pkl')  # Уровень выше папки проекта
vectorizer_path = os.path.join(BASE_DIR, '../vectorizer.pkl')

# Загрузка модели и векторизатора
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
def classify_review(text):
    vectorized_text = vectorizer.transform([text])
    predicted_sentiment = model.predict(vectorized_text)[0]
    probability = model.predict_proba(vectorized_text)[0][1]

    # Присвоение рейтинга на основе вероятности
    if probability > 0.9:
        predicted_rating = 10
    elif probability > 0.8:
        predicted_rating = 9
    elif probability > 0.7:
        predicted_rating = 8
    elif probability > 0.6:
        predicted_rating = 7
    elif probability > 0.5:
        predicted_rating = 6
    elif probability > 0.4:
        predicted_rating = 5
    elif probability > 0.3:
        predicted_rating = 4
    elif probability > 0.2:
        predicted_rating = 3
    elif probability > 0.1:
        predicted_rating = 2
    else:
        predicted_rating = 1

    sentiment = "positive" if predicted_sentiment == 1 else "negative"
    return sentiment, predicted_rating

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['review_text']
            sentiment, predicted_rating = classify_review(review_text)
            
            # Сохранение в базу данных
            new_review = Review(text=review_text, predicted_rating=predicted_rating, sentiment=sentiment)
            new_review.save()
            
            return render(request, 'review_result.html', {'review': new_review})
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})
