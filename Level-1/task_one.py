from datetime import date


class Trainee():
    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list[Assessment] = []):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments

    def get_age(self) -> int:
        today = date.today()
        age = int(today.year) - self.date_of_birth.year - \
            ((int(today.month), int(today.day)) <
             (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        self.assessments.append(assessment)
        return None

    def get_assessment(self, name: str) -> None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


class Assessment():
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        allowed_types = ["multiple-choice", "technical", "presentation"]
        if type in allowed_types:
            self.type = type
        else:
            raise ValueError("Type must be in allowed types.")
        if score >= 0 and score <= 100:
            self.score = score
        else:
            raise ValueError("Score must be between 0-100")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
