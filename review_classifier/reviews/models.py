from django.db import models

class Review(models.Model):
    text = models.TextField()  # Текст отзыва
    predicted_rating = models.IntegerField()  # Предсказанный рейтинг от 1 до 10
    sentiment = models.CharField(max_length=10)  # Положительный или отрицательный отзыв ("positive" или "negative")

    def __str__(self):
        return f"Review: {self.text[:50]}... | Rating: {self.predicted_rating} | Sentiment: {self.sentiment}"
