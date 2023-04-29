if __name__ == '__main__':
    # Get number of students
    n = int(input("enter a number:"))

    # Create a nested list to store name and grades of students
    nested_list = []

    # Add name and grade of each student to the nested list
    for i in range(n):
        name = input("name:")
        score = float(input())
        nested_list.append([name, score])

    # Find the second lowest grade
    scores = set([x[1] for x in nested_list])
    second_lowest = sorted(scores)[1]

    # Get names of students with the second lowest grade
    names = [x[0] for x in nested_list if x[1] == second_lowest]

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)