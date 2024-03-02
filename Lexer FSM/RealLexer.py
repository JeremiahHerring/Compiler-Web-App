from Separator import separators
from Operator import operators

class RealLexer:
    def __init__(self):
        self.states = {'1', '2', '3', '4'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        self.start_state = '1'
        self.accepting_state = {'4'}
        self.current_state = self.start_state
        self.transition_table = {
            ('1', 'digit'): '2',
            ('2', 'digit'): '2',
            ('2', '.'): '3',
            ('3', 'digit'): '4',
            ('4', 'digit'): '4',
        }

    # Identify char
    def process_input(self, char):
        if char.isdigit():
            return 'digit'
        elif char == '.':
            return '.'
        else:
            return None

    def process_char(self, char):
        input_type = self.process_input(char)

        if input_type is None:
            self.current_state = 'reject'
        elif (self.current_state, input_type) in self.transition_table:
            self.current_state = self.transition_table[(self.current_state, input_type)]
        else:
            self.current_state = 'reject'

        input_char_terminates_token = (
            char in separators or char in operators or char.isspace()
        ) and self.current_state not in self.accepting_state

        return input_char_terminates_token, self.current_state

    # Function to validate or invalidate real number
    def validate_real(self, inputStr):
        input_char_terminates_token = False
        prev_accepting_state = self.start_state

        for char in inputStr:
            terminates_token, current_state = self.process_char(char)

            if terminates_token:
                input_char_terminates_token = True

            if current_state in self.accepting_state:
                prev_accepting_state = current_state

        is_valid = prev_accepting_state in self.accepting_state or (
            input_char_terminates_token and prev_accepting_state == self.start_state
        )

        return is_valid, input_char_terminates_token

if __name__ == "__main__":
    lexerInstance = RealLexer()

    real = "1.1"
    
    for char in real:
        is_valid, input_char_terminates_token = lexerInstance.validate_real(char)
        print(f"Char: {char}, Is Valid: {is_valid}, Terminates Token: {input_char_terminates_token}")
