from data import question_data

class Question:

    def __init__(self, question, answer):
        self.text = question
        self.answer = answer
 
    def get_question():
        return self.text

    def get_answer():
        return self.answer
    
question_bank = []

for qa in question_data:
    #print(qa["text"])
    new_question = Question(qa["text"], qa["answer"])
    question_bank.append(new_question)

print(question_bank[-1].text)
print(question_bank[-1].answer)
