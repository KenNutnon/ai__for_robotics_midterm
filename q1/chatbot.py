
class MidtermChatBot:
    def __init__(self):
        self.main()

    def showSubjectName(self):
        print('AI for robot system')
        return

    def showStudentYear(self):
        print('6310550551 is year 4th')
        return

    def calculator(self):
        operator = input()
        a = int(input())
        b = int(input())
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        print(int(result))
        return

    def main(self):
        while True:
            command = input()
            
            if command == 'subject':
                self.showSubjectName()
            elif command == 'year':
                self.showStudentYear()
            elif command == 'calc':
                self.calculator()

if __name__ == '__main__':
    MidtermChatBot()
