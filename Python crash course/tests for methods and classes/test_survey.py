from survey import AnonymousSurvey
import unittest

class TEstAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'what language did you first learn?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Spanish', 'English', 'Italian']

    def test_store_single_response(self):
        #question = 'Which is the first lang you learned?'
        #my_survey = AnonymousSurvey(question)
        #Puedo comentar las dos lineas de arriba porque fueron reemplazadas por el metodo setUp
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        #question = 'Programming langs you know'
        #my_survey = AnonymousSurvey(question)
        #responses = ['Basic', 'VB', 'Python']
        #Idem, el setup de la pregunta y las posibles respuestas queda a cargo del metodo setUp de arriba de todo
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
