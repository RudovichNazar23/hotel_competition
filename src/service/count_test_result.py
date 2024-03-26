def count_test_result(answers: list):
    correct_answers = [*filter(lambda x: x.is_correct, answers)]
    competition_test_result = 0

    if len(correct_answers):
        competition_test_result = len(correct_answers) / len(answers) * 100

    return competition_test_result
