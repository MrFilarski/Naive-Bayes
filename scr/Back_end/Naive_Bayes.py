from scr.Back_end.Data_classes import Train


class Classifier:
    def __init__(self, train_set: Train):
        self.train_set = train_set

    def classify(self, to_classify: list[str]) -> str:
        dictionary = {}
        for y in self.train_set.get_set_decisions():
            dictionary[y] = self.__probability_of_decision(y, to_classify)
        return max(dictionary, key=dictionary.get)

    def __probability_of_decision(self, y, x: list[str]) -> float:
        print(y)
        precision = 2
        favorable, possible = self.train_set.count_decision_in_decisions(y)
        result_y: float = favorable / possible
        print(round(result_y, precision), end=' * ')
        final = result_y
        possible = favorable
        for index, attribute in enumerate(x):
            favorable = self.train_set.count_attributes_with_decision(index, attribute, y)
            if favorable == 0:
                favorable += 1
                possible += self.train_set.count_set_attribute(index)

            result_x = favorable / possible
            final *= result_x
            if index != len(x) - 1:
                print(round(result_x, precision), sep=' * ', end=' * ')
            else:
                print(round(result_x, precision), sep=' * ', end=' = ')
        print(round(final, precision))
        print()
        return final
