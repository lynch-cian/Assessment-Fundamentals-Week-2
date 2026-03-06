"""Task 3"""
from datetime import date

allowed_types = ["multiple-choice", "technical", "presentation"]


class Marking():
    """Marking class"""

    def __init__(self, quiz: Quiz, assessment: Assessment = None) -> None:
        self._quiz = quiz
        if assessment is None:
            self.assessment = self.generate_assessment()
        else:
            self.assessment = assessment

    def mark(self) -> int:
        """Returns score percentage for quiz"""
        score = 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                score += 1
        if score == 0:
            return 0
        return score / len(self._quiz.questions) * 100

    def generate_assessment(self) -> Assessment:
        """Returns Assessment object with correct type"""
        if self._quiz.type == allowed_types[0]:
            assessment = MultipleChoiceAssessment(self._quiz.name)
        if self._quiz.type == allowed_types[1]:
            assessment = TechnicalAssessment(self._quiz.name)
        if self._quiz.type == allowed_types[2]:
            assessment = PresentationAssessment(self._quiz.name)
        else:
            raise ValueError("Must be correct type.")
        return assessment


class Trainee():
    """Trainee subclass"""

    def __init__(self, name: str, email: str, date_of_birth: date,
                 assessments: list[Assessment] = None):
        self.name = name
        if "@" not in email or ".com" not in email:
            raise TypeError("Please enter a valid email.")
        self.email = email
        self.date_of_birth = date_of_birth
        if assessments is None:
            for assessment in assessments:
                if not isinstance(assessment, Assessment):
                    raise TypeError(
                        "All assessments must be subclass of Assessment.")
            self.assessments = []
        else:
            self.assessments = assessments

    def get_age(self) -> int:
        """Returns trainee's age"""
        today = date.today()
        age = int(today.year) - self.date_of_birth.year - \
            ((int(today.month), int(today.day)) <
             (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """Adds assessment to trainee"""
        if not isinstance(assessment, Assessment):
            raise TypeError("Must be Assessment object")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> None:
        """Finds assessment by name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Finds assessments of inputted type"""
        assessment_list = []
        if type not in allowed_types:
            raise ValueError("Assessment type not found.")
        for assessment in self.assessments:
            if assessment.type == type:
                assessment_list.append(assessment)
        return assessment_list


class Assessment():
    """Assessment class"""

    def __init__(self, name: str, type: str, score: float):
        self.name = name
        if type in allowed_types:
            self.type = type
        else:
            raise ValueError("Type must be in allowed types.")
        if 0 >= score <= 100:
            self.score = score
        else:
            raise ValueError("Score must be between 0-100")


class MultipleChoiceAssessment(Assessment):
    """MQC subclass"""

    def __init__(self, name: str, score: float = 100):
        self.score = score
        self.name = name
        self.type = allowed_types[0]

    def calculate_score(self) -> int:
        """Calculates MCQ score"""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Technical assessment subclass"""

    def __init__(self, name: str, score: float = 1000):
        self.score = score
        self.name = name
        self.type = allowed_types[1]

    def calculate_score(self) -> int:
        """Returns technical assessment score"""
        return self.score


class PresentationAssessment(Assessment):
    """Presentation assessment subclass"""

    def __init__(self, name: str, score: float = 100):
        self.score = score
        self.name = name
        self.type = allowed_types[2]

    def calculate_score(self) -> int:
        """Returns presentation assessment score"""
        return self.score * 0.6


class Question:
    """Question class"""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Quiz class"""

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
