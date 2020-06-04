class Calculator:

    path_txt = 'calc_cache.txt'
    path_csv = 'calc_cache.csv'

    ''' Advanced calculator '''
    @staticmethod
    def input_value():
        ''' Input value and check if it integer or float and not equal 0 '''
        NULL = '0'
        while True:
            val = input()
            if val.isdigit() and val != NULL:
                int_val = int(val)
                return int_val
            else:
                if val == '0':
                    print('Not equal 0!!!')
                try:
                    if val != NULL:
                        float_val = float(val)
                        return float_val
                except ValueError:
                    print('It must be a number and not equal 0!')
                    continue

    def __init__(self):
        ''' Brain of calculator. Here are all processes interconnected.
        Input operation, input value(s), calculate, caching and print the result.
         '''
        self.sign_x = ['x!','sqrtx','sinx','cosx','tgx','ctgx']
        self.sign = self.enter_sign()
        if self.sign in self.sign_x:
            print('Enter the first number:')
            self.a = Calculator.input_value()
        else:
            print('Enter the first number:')
            self.a = Calculator.input_value()
            print('Enter the second number: ')
            self.b = Calculator.input_value()
        self.result = self.do_operation()
        self.print_result()
        self.caching()
        while True:
            convert = input('Convert cache of calculating to csv file? Y/N').lower()
            if convert == 'y':
                self.convert_to_csv()
                break
            elif convert == 'n':
                break
            else:
                continue

    def enter_sign(self):
        ''' Selection of the operation associated with your input '''
        while True:
            signs = ['+','-','/','*','%','//',
                     'x!','x**y','sqrtx','logxy',
                     'sinx','cosx','tgx','ctgx']
            self.sign = input('Enter the option would you prefer from list => \n'
                         f'{signs}\n')
            if self.sign.lower() in signs:
                return self.sign.lower()
            else:
                print('Wrong option!')
                continue

    def do_operation(self):
        ''' Function for a make calculation '''
        import math
        if self.sign == '+':
            self.result = self.a + self.b
            return self.result
        elif self.sign == '-':
            self.result = self.a - self.b
            return self.result
        elif self.sign == '/':
            self.result = self.a / self.b
            return round(self.result,2)
        elif self.sign == '*':
            self.result = self.a * self.b
            return round(self.result,2)
        elif self.sign == '%':
            self.result = self.a % self.b
            return self.result
        elif self.sign == '//':
            self.result = self.a // self.b
            return self.result
        elif self.sign == 'x!':
            self.result = math.factorial(self.a)
            return self.result
        elif self.sign == 'x**y':
            self.result = math.pow(self.a,self.b)
            return self.result
        elif self.sign == 'sqrtx':
            self.result = math.sqrt(self.a)
            return round(self.result,2)
        elif self.sign == 'logxy':
            self.result = math.log(self.a,self.b)
            return self.result
        elif self.sign == 'sinx':
            self.result = math.sin(self.a)
            return round(self.result,2)
        elif self.sign == 'cosx':
            self.result = math.cos(self.a)
            return round(self.result,2)
        elif self.sign == 'tgx':
            self.result = math.tan(self.a)
            return round(self.result,2)
        elif self.sign == 'ctgx':
            self.result = (math.cos(self.a)/math.sin(self.a))
            return round(self.result,2)

    def print_result(self):
        ''' Printing the result of calculation '''
        if self.sign in self.sign_x:
            print(f'{self.a} {self.sign} = {self.result}')
        else:
            print(f'{self.a} {self.sign} {self.b} = {self.result}')

    def caching(self):
        ''' Caching the result to txt file. '''
        from contextlib import redirect_stdout
        f = open(Calculator.path_txt, 'a')
        with redirect_stdout(f):
            self.print_result()
        print('Caching successful.')

    def convert_to_csv(self):

        import csv
        with open(Calculator.path_txt, 'r') as in_file:
            stripped = [line.strip() for line in in_file]
            lines = [line.split(',') for line in stripped if line]
            with open(Calculator.path_csv,'w') as csv_file:
                writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
                writer.writerow(['Operations'])
                for line in lines:
                    writer.writerow(line)

'''
Start calculator with loop(n). 
You must enter the value of the variable n.
'''
calc = Calculator
while True:
    try:
        calculations = int(input('How many operations should you calculate?'))
        calculate = 0
        while calculate < calculations:
            calc()
            calculate += 1
    except:
        print('It must be a number!!!')
        continue
    else:
        print('Finish calculating!')
        break

input()