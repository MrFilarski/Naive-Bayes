import csv
from abc import ABC
from dataclasses import dataclass


@dataclass
class Data:
    decision: str
    attributes: list[str]


def create_data(lines: list) -> list[Data]:
    data: list[list[str]] = [row for row in csv.reader(lines)]
    return [Data(attributes=line[1:], decision=line[0]) for line in data]


@dataclass()
class Set_Class(ABC):
    collection: list[Data]


class Train(Set_Class):

    def get_set_decisions(self) -> set:
        return set([data.decision for data in self.collection])

    def count_set_attribute(self, index) -> int:
        return len(set([data.attributes[index] for data in self.collection]))
        pass

    def count_attributes_with_decision(self, index: int, searching: str, decision: str) -> int:

        count = 0
        for row in self.collection:
            for i, x in enumerate(row.attributes):
                if x == searching and i == index:
                    if row.decision == decision:
                        count += 1

        return count
        pass

    def count_decision_in_decisions(self, searching: str):
        favorable = 0
        for data in self.collection:
            if data.decision == searching:
                favorable += 1

        return favorable, len(self.collection)

    pass


class Test(Set_Class):
    pass
