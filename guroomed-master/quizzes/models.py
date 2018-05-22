from django.db import models
from django.contrib.auth.models import User
from drafts.models import CurriculumSection


class Quizzes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_section_id =  models.ForeignKey(CurriculumSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateField(auto_now=True)
    
class QuestionTypes(models.Model):
    name = models.CharField(max_length=70)

class Questions(models.Model):
    quiz_id = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    type_id = models.ForeignKey(QuestionTypes, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    status = models.BooleanField()
    order = models.IntegerField(2)

class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField()
    status = models.BooleanField()
    order = models.IntegerField(2)

class QuizProgress(models.Model):
    quiz_id = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(2)
    score_outof = models.IntegerField(2)
    status = models.BooleanField() # 0 is failed, 1 is passed
    correct_questions = models.CharField(max_length=500)
    wrong_questions = models.CharField(max_length=500)
    skipped_questions = models.CharField(max_length=500)