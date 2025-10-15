from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, QuizAttempt, Answer
import random
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def index(request):
    """Landing page with instructions"""
    return render(request, 'quiz/index.html')


def start_quiz(request):
    """Initialize quiz session and select random questions"""
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        school = request.POST.get('school', '')
        email = request.POST.get('email', '')
        
        if not student_name:
            return redirect('index')
        
        # Store student info in session
        request.session['student_name'] = student_name
        request.session['school'] = 'Isanbi High School'
        request.session['email'] = email
        request.session['start_time'] = datetime.now().isoformat()
        
        # Select 10 random questions from pool of 25
        all_questions = list(Question.objects.all())
        if len(all_questions) < 10:
            # If less than 10 questions in DB, use all
            selected_questions = all_questions
        else:
            selected_questions = random.sample(all_questions, 10)
        
        # Store question IDs in session
        request.session['question_ids'] = [q.id for q in selected_questions]
        request.session['current_question'] = 0
        request.session['answers'] = {}
        
        return redirect('quiz')
    
    return redirect('index')


def quiz(request):
    """Display quiz questions"""
    if 'question_ids' not in request.session:
        return redirect('index')
    
    question_ids = request.session['question_ids']
    current_idx = request.session.get('current_question', 0)
    
    if current_idx >= len(question_ids):
        return redirect('submit_quiz')
    
    question = Question.objects.get(id=question_ids[current_idx])
    
    # Get previously selected answer if any
    answers = request.session.get('answers', {})
    selected = answers.get(str(question.id), '')
    
    context = {
        'question': question,
        'question_number': current_idx + 1,
        'total_questions': len(question_ids),
        'selected_answer': selected,
        'student_name': request.session.get('student_name', ''),
    }
    
    return render(request, 'quiz/quiz.html', context)


def save_answer(request):
    """Save answer and move to next question"""
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')
        action = request.POST.get('action', 'next')
        
        if question_id and answer:
            answers = request.session.get('answers', {})
            answers[question_id] = answer
            request.session['answers'] = answers
        
        current_idx = request.session.get('current_question', 0)
        
        if action == 'previous':
            request.session['current_question'] = max(0, current_idx - 1)
        elif action == 'next':
            request.session['current_question'] = current_idx + 1
        
        return redirect('quiz')
    
    return redirect('index')


def submit_quiz(request):
    """Calculate score and save results"""
    if 'question_ids' not in request.session:
        return redirect('index')
    
    question_ids = request.session['question_ids']
    answers = request.session.get('answers', {})
    
    # Calculate time taken
    start_time = datetime.fromisoformat(request.session.get('start_time'))
    time_taken = int((datetime.now() - start_time).total_seconds())
    
    # Create quiz attempt
    attempt = QuizAttempt.objects.create(
        student_name=request.session.get('student_name', 'Anonymous'),
        school=request.session.get('school', ''),
        email=request.session.get('email', ''),
        score=0,
        total_questions=len(question_ids),
        time_taken=time_taken
    )
    
    score = 0
    results = []
    
    for qid in question_ids:
        question = Question.objects.get(id=qid)
        selected = answers.get(str(qid), '')
        is_correct = selected == question.correct_answer
        
        if is_correct:
            score += 1
        
        # Save individual answer
        Answer.objects.create(
            attempt=attempt,
            question=question,
            selected_answer=selected,
            is_correct=is_correct
        )
        
        results.append({
            'question': question,
            'selected': selected,
            'correct': question.correct_answer,
            'is_correct': is_correct,
        })
    
    # Update score
    attempt.score = score
    attempt.save()
    
    # Clear session
    for key in ['question_ids', 'current_question', 'answers', 'start_time']:
        if key in request.session:
            del request.session[key]
    
    context = {
        'attempt': attempt,
        'results': results,
        'percentage': attempt.percentage,
    }
    
    return render(request, 'quiz/result.html', context)


def leaderboard(request):
    """Display top scores"""
    top_attempts = QuizAttempt.objects.order_by('-score', 'time_taken')[:10]
    
    context = {
        'attempts': top_attempts,
    }
    
    return render(request, 'quiz/leaderboard.html', context)
