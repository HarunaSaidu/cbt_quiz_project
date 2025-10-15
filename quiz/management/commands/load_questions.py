"""
# Create this file for easy question loading
# Directory: quiz/management/commands/load_questions.py

from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Load sample questions into database'

    def handle(self, *args, **kwargs):
        questions_data = [
            # Copy all questions from populate_questions.py here
            # (Same data as above)
        ]
        
        # Clear existing questions (optional)
        # Question.objects.all().delete()
        
        for q_data in questions_data:
            Question.objects.create(**q_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(questions_data)} questions')
        )
"""