from models.lesson_models import LessonModel
from models.lesson_progress_models import LessonProgressModel


def calculate_course_progress(student, course):
    total = LessonModel.objects.filter(course=course).count()

    if total == 0:
        return 0

    completed = LessonProgressModel.objects.filter(
        student=student, lesson__course=course, is_completed=True
    ).count()

    return round((completed / total) * 100)
