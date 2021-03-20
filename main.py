# coding=utf-8
class Fraction:

    def __init__(self):
        self.first_num = int(input('Enter the first fraction\'s numerator: '))
        self.first_denom = int(input('Enter the first fraction\'s denominator: '))
        self.second_num = int(input('Enter the second fraction\'s numerator: '))
        self.second_denom = int(input('Enter the second fraction\'s denominator: '))

        self.the_sum = 0
        self.subtraction = 0
        self.multiplication_1 = 1
        self.multiplication_2 = 1

    def sum(self):
        if self.first_denom == self.second_denom:       # if denominators are equal to each other
            self.the_sum = self.first_num + self.second_num
            if self.the_sum % self.first_denom == 0:
                self.the_sum = self.the_sum / self.first_denom
                print(self.the_sum)
            else:
                print(f'{self.the_sum}/{self.first_denom} = {self.the_sum / self.first_denom}')
        elif self.first_denom % self.second_denom == 0:     # if the first denominator is a multiple of the second one
            self.second_num = self.first_denom / self.second_denom * self.second_num
            self.the_sum = self.first_num + self.second_num
            if self.the_sum % self.first_denom == 0:
                self.the_sum = self.the_sum / self.first_denom
                print(self.the_sum)
            else:
                print(f'{self.the_sum}/{self.first_denom} = {self.the_sum / self.first_denom}')
        elif self.second_denom % self.first_denom == 0:     # if the second denominator is a multiple of the first one
            self.first_num = self.second_denom / self.first_denom * self.first_num
            self.the_sum = self.first_num + self.second_num
            if self.the_sum % self.first_denom == 0:
                self.the_sum = self.the_sum / self.first_denom
                print(self.the_sum)
            else:
                print(f'{self.the_sum}/{self.first_denom} = {self.the_sum / self.first_denom}')
        else:       # if the denominators don't equal to each other and one of them is not a multiple of the other
            self.first_num = self.second_denom * self.first_num
            self.second_num = self.first_denom * self.second_num
            self.first_denom = self.second_denom = self.first_denom * self.second_denom
            self.the_sum = self.first_num + self.second_num
            if self.the_sum % self.first_denom == 0:
                self.the_sum = int(self.the_sum / self.first_denom)
                print(self.the_sum)
            else:
                print(f'{self.the_sum}/{self.first_denom} = {self.the_sum / self.first_denom}')

    def subtraction(self):
        if self.first_denom == self.second_denom:       # if denominators are equal to each other
            self.subtraction = self.first_num + self.second_num
            if self.subtraction % self.first_denom == 0:
                self.subtraction = self.subtraction / self.first_denom
                print(self.subtraction)
            else:
                print(f'{self.subtraction}/{self.first_denom} = {self.subtraction / self.first_denom}')
        elif self.first_denom % self.second_denom == 0:     # if the first denominator is a multiple of the second one
            self.second_num = self.first_denom / self.second_denom * self.second_num
            self.subtraction = self.first_num + self.second_num
            if self.subtraction % self.first_denom == 0:
                self.subtraction = self.subtraction / self.first_denom
                print(self.subtraction)
            else:
                print(f'{self.subtraction}/{self.first_denom} = {self.subtraction / self.first_denom}')
        elif self.second_denom % self.first_denom == 0:     # if the second denominator is a multiple of the first one
            self.first_num = self.second_denom / self.first_denom * self.first_num
            self.subtraction = self.first_num + self.second_num
            if self.subtraction % self.first_denom == 0:
                self.subtraction = self.the_sum / self.first_denom
                print(self.subtraction)
            else:
                print(f'{self.subtraction}/{self.first_denom} = {self.subtraction / self.first_denom}')
        else:       # if the denominators don't equal to each other and one of them is not a multiple of the other
            self.first_num = self.second_denom * self.first_num
            self.second_num = self.first_denom * self.second_num
            self.first_denom = self.second_denom = self.first_denom * self.second_denom
            self.subtraction = self.first_num + self.second_num
            if self.subtraction % self.first_denom == 0:
                self.subtraction = int(self.the_sum / self.first_denom)
                print(self.subtraction)
            else:
                print(f'{self.subtraction}/{self.first_denom} = {self.subtraction / self.first_denom}')

    def multiplication(self):
        self.multiplication_1 = self.first_num * self.second_num
        self.multiplication_2 = self.first_denom * self.second_denom
        if self.multiplication_1 % self.multiplication_2 == 0:
            self.multiplication_1 = int(self.multiplication_1 / self.multiplication_2)
            print(self.multiplication_1)
        else:
            print(f'{self.multiplication_1}/{self.multiplication_2} = {self.multiplication_1 / self.multiplication_2}')

    def division(self):
        # when dividing 2 fractions the second fraction is turned over and multiplied by the first fraction
        self.multiplication_1 = self.first_num * self.second_denom
        self.multiplication_2 = self.first_denom * self.second_num
        if self.multiplication_1 % self.multiplication_2 == 0:
            self.multiplication_1 = int(self.multiplication_1 / self.multiplication_2)
            print(self.multiplication_1)
        else:
            print(f'{self.multiplication_1}/{self.multiplication_2} = {self.multiplication_1 / self.multiplication_2}')

summing = Fraction()
summing.division()

