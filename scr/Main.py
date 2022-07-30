from scr.Back_end import Data_classes, FileManager, Naive_Bayes
from scr.Back_end.Data_classes import Data, Train, Test
from scr.Back_end.Matrix_Confusion import Matrix_Confusion, Statistic

print("Naive Bayes")


def main():
    train: Train = Train(collection=Data_classes.create_data(FileManager.get_from_url("agaricus-lepiota.data")))
    test: Test = Test(collection=Data_classes.create_data(FileManager.get_from_url("agaricus-lepiota.test.data")))
    print(train.collection[0], sep="\n")
    matrix = Matrix_Confusion(positive_class='p')
    execute(train, test, matrix)


def execute(train, test, matrix):
    for index, example in enumerate(test.collection):
        classify = Naive_Bayes.Classifier(train).classify(example.attributes)
        print(f"{classify=}")
        matrix.count(result_of_classificatory=classify, correct_answer=example.decision)
        print(matrix)
    print(Statistic(matrix))
    pass


def example_data():
    print("example")
    train = Train(
        [
            Data(attributes=["True", "True", "True"], decision="Mammal", ),
            Data(attributes=["True", "True", "True"], decision="Mammal", ),

            Data(attributes=["True", "True", "False"], decision="Reptile"),

            Data(attributes=["False", "True", "True"], decision="Mammal"),
            Data(attributes=["True", "True", "True"], decision="Mammal"),
            Data(attributes=["True", "True", "True"], decision="Mammal", ),

            Data(attributes=["True", "False", "False"], decision="Reptile"),
            Data(attributes=["True", "True", "False"], decision="Reptile"),

            Data(attributes=["True", "True", "True"], decision="Mammal"),
            Data(attributes=["False", "False", "True"], decision="Reptile"),
        ]
    )

    test = Test([Data(attributes=["True", "True", "False"], decision="Mammal")])
    print(test.collection[0])
    matrix = Matrix_Confusion(positive_class='Mammal')
    execute(train, test, matrix)

    """
    print(train.count_attributes_with_decision(index=0, searching='True', decision="Mammal"))
    print(train.count_decision_in_decisions(searching="Mammal"))
    """


def check_matrix():
    print("Sprawdzanie matrixa")
    matrix = Matrix_Confusion(
        "Reptile",
        true_positive=50, false_negative=6,
        false_positive=4, true_negative=40
    )
    print(matrix)
    print(Statistic(matrix))


if __name__ == "__main__":
    main()
    # example_data()
    # check_matrix()
