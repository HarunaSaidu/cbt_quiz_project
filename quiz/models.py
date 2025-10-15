from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ])
    explanation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]

    class Meta:
        ordering = ['?']  # Random ordering


class QuizAttempt(models.Model):
    student_name = models.CharField(max_length=100)
    school = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    score = models.IntegerField()
    total_questions = models.IntegerField(default=10)
    attempted_at = models.DateTimeField(auto_now_add=True)
    time_taken = models.IntegerField(help_text="Time in seconds")

    def __str__(self):
        return f"{self.student_name} - {self.score}/{self.total_questions}"

    @property
    def percentage(self):
        if self.score == 0 or self.total_questions == 0:
            return 0
        return (self.score / self.total_questions) * 100

    class Meta:
        ordering = ['-attempted_at']


class Answer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.attempt.student_name} - Q{self.question.id}"
