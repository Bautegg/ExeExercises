def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    rounded_scores = [round(score) for score in student_scores]
    return rounded_scores

def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    return len([1 for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """


    return [score for score in student_scores if score >= threshold]

def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    step = (highest - 40) / 4
    list = []
    for i in range(41,highest, round(step)):
        list.append(i)

    return list


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """


    list = []
    for index, name, in enumerate(student_names):
            list.append( f'{index + 1}. {name}: {student_scores[index]}' )
    return list
    # print(student_count)
    # for i in range(1, student_count + 1, 1):
    #     print( i )
    # for score in student_scores:
    #     print(score)
    # for name in student_names:
    #     print(name)
    # list.append([f'{i}. {name}: {score}'])
    # print(list)

    # for score in student_scores:
    #     for index, name, in enumerate(student_names):
    #         list.append(f'{index+1}. {name}: {score}')

def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for index, list in enumerate(student_info):
        if list[1] != 100:
            continue
        if list[1] == 100:
            return student_info[index]
    return []



if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'rounded scores: {round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])}' )
    print( f'count failed students: {count_failed_students([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])}' )
    print( f'above treshold: {above_threshold([90,40,55,70,30,68,70,75,83,96], 90)}' )
    print( f'letter_grades: {letter_grades(88)}' )
    print( f"student ranking: {student_ranking([100, 99, 90, 84, 66, 53, 47],['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred'])}" )
    print( f'perfect score: {perfect_score([["Nice",34],["Tony", 80], ["Alex", 100]])}')