"""Task Two"""

from datetime import date

allowed_types = ["multiple-choice", "technical", "presentation"]


class Trainee():
    """Trainee class"""

    def __init__(self, name: str, email: str, date_of_birth: date,
                 assessments: list[Assessment] = None):
        self.name = name
        if "@" not in email or ".com" not in email:
            raise TypeError("Please enter a valid email.")
        self.email = email
        self.date_of_birth = date_of_birth
        if assessments is None:
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
        """Find assessment by name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment

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
    """Assessment Class"""

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
    """MCQ Subclass"""

    def __init__(self, name: str, score: float = 0):
        self.score = score
        self.name = name
        self.type = allowed_types[0]

    def calculate_score(self):
        """Calculates MCQ score"""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Technical Assessment subclass"""

    def __init__(self, name: str, score: float = 0):
        self.score = score
        self.name = name
        self.type = allowed_types[1]

    def calculate_score(self):
        """Calculates technical assessment score"""
        return self.score


class PresentationAssessment(Assessment):
    """Presentation assessment subclass"""

    def __init__(self, name: str, score: float = 0):
        self.score = score
        self.name = name
        self.type = allowed_types[2]

    def calculate_score(self):
        """Calculates presentation assessment score"""
        return self.score * 0.6


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
