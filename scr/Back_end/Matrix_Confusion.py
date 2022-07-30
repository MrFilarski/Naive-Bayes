from dataclasses import dataclass
from scr.Front_end import Gui


@dataclass
class Matrix_Confusion:
    positive_class: str

    true_positive: int = 0
    false_negative: int = 0
    false_positive: int = 0
    true_negative: int = 0

    def count(self, result_of_classificatory: str, correct_answer: str):
        print(f"{correct_answer=}   {self.positive_class=}")
        correct: bool = result_of_classificatory.__eq__(correct_answer)
        positive: bool = result_of_classificatory.__eq__(self.positive_class)
        print(f"{correct=}     {positive=}")

        if correct:
            if positive:
                self.true_positive += 1
            else:
                self.true_negative += 1
        else:
            if positive:
                self.false_positive += 1
            else:
                self.false_negative += 1

    def __str__(self):
        headers = ["classified ->", f"{self.positive_class}", f"!{self.positive_class}"]
        data = [
            [f"{self.positive_class}", f"{self.true_positive}", f"{self.false_negative}"],
            [f"!{self.positive_class}", f"{self.false_positive}", f"{self.true_negative}"]
        ]
        return Gui.print_table(headers, data)


class Statistic:
    accuracy: float
    precision: float
    recall: float
    f_measure: float

    def __init__(self, m: Matrix_Confusion):
        tp, fn = m.true_positive, m.false_negative
        fp, tn = m.false_positive, m.true_negative

        self.accuracy = (tp + tn) / (tp + tn + fp + fn)
        self.precision = tp / (tp + fp)
        self.recall = tp / (tp + fn)

        p, r = self.precision, self.recall
        self.f_measure = 2 * p * r / (p + r)

    def __str__(self):
        n: int = 2
        return f"""
     A = {round(self.accuracy, n)}
     P = {round(self.precision, n)}
     R = {round(self.recall, n)}
     F = {round(self.f_measure, n)}"""
