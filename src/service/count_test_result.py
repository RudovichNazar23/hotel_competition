def count_test_result(test_questions, user_answers: list):
    test_correct_answers = []

    for question in test_questions:
        test_correct_answers.append(*filter(lambda x: x.is_correct, question.answer_set.all()))

    user_correct_answers = [*filter(lambda x: x.is_correct, user_answers)]
    competition_test_result = 0

    if len(user_correct_answers):
        competition_test_result = len(user_correct_answers) / len(test_correct_answers) * 100

    return competition_test_result
