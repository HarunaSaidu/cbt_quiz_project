from django.contrib import admin
from .models import Question, QuizAttempt, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'correct_answer', 'created_at']
    search_fields = ['question_text']
    list_filter = ['created_at']


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'school', 'score', 'total_questions', 'percentage', 'attempted_at']
    search_fields = ['student_name', 'school']
    list_filter = ['attempted_at']
    readonly_fields = ['attempted_at']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['attempt', 'question', 'selected_answer', 'is_correct']
    list_filter = ['is_correct']
