from survey import AnonymousSurvey

question = 'Which was your first programming lang'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('these are the results')
my_survey.show_results()