# Взять класс Student из ДЗ 12-го семинара
# для него реализовать запуск из консоли
# и логирование(уровень Debug и Error).
# Исключение ValueErrror заменить на собственные.
# Было бы неплохо, если вы покроете код тестами,
# хотя бы минимально(2-3 штуки)

import logging
import argparse

logging.basicConfig(filename='homework/hw15/log_ex01.log',
                    filemode='w', encoding='utf-8',  level=logging.DEBUG,
                    format='{asctime}, {levelname}, {msg}', style='{')


class IncorrectName(Exception):
    pass


class IncorrectScore(Exception):
    pass


class NoSubject(Exception):
    pass


class FullName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        if not value.istitle() and not value.isalpha():
            logging.error(msg=f'{IncorrectName}, {value}')
            raise IncorrectName(
                'ФИО должно состоять только из букв \
и начинаться с заглавной буквы')


class Student:
    name = FullName()

    def __init__(self, name: str, subjects_file: str) -> None:
        """
        >>> s1 = Student('Иван Иванов', 'homework/hw15/subjects.csv')
        >>> s1.name
        'Иван Иванов'
        """
        self.name = name
        logging.debug(msg=f'Создан студент: {self.name}')
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __str__(self):
        subjects_lst = []
        for subject in self.subjects.keys():
            if self.subjects[subject]['grades']\
                    or self.subjects[subject]['test_scores']:
                subjects_lst.append(subject)
        subjects = ", ".join(subjects_lst)
        return f'Студент: {self.name}\nПредметы: {subjects}'

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            data = file.read().split(',')
            for subject in data:
                self.subjects[subject] = {
                    'grades': [],
                    'test_scores': [],
                }

    def add_grade(self, subject, grade):
        if subject in self.subjects.keys():
            if 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)
                logging.debug(
                    msg=f'Новая оценка: {self.name}, {subject}, {grade}')
            else:
                logging.error(msg=f'{IncorrectScore}, {subject}, {grade}')
                raise IncorrectScore(
                    'Оценка должна быть целым числом от 2 до 5')
        else:
            raise NoSubject(f'Предмет {subject} не найден')

    def add_test_score(self, subject, test_score):
        if subject in self.subjects.keys():
            if 0 <= test_score <= 100:
                self.subjects[subject]['test_scores'].append(test_score)
                logging.debug(
                    msg=f'Новый тест: {self.name}, {subject}, {test_score}')
            else:
                logging.error(msg=f'{IncorrectScore}, {subject}, {test_score}')
                raise IncorrectScore(
                    'Результат теста должен быть целым числом от 0 до 100')
        else:
            raise NoSubject(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject):
        """
        >>> s2 = Student('Марк Аврелий', 'homework/hw15/subjects.csv')
        >>> s2.add_grade("Математика", 4)
        >>> s2.add_grade("Математика", 3)
        >>> s2.add_grade("История", 5)
        >>> s2.get_average_grade()
        4.0
        >>> s2.add_grade("История", 0)
        Traceback (most recent call last):
        ...
        IncorrectScore: Оценка должна быть целым числом от 2 до 5
        """
        if subject in self.subjects.keys():
            return (sum(self.subjects[subject]['test_scores'])
                    / len(self.subjects[subject]['test_scores']))
        else:
            raise NoSubject(f'Предмет {subject} не найден')

    def get_average_grade(self):
        """
        >>> s3 = Student('Марк Аврелий', 'homework/hw15/subjects.csv')
        >>> s3.add_test_score("Математика", 80)
        >>> s3.add_test_score("Математика", 70)
        >>> s3.get_average_test_score("Математика")
        75.0
        >>> s3.add_test_score("Математика", 170)
        Traceback (most recent call last):
        ...
        IncorrectScore: Результат теста должен быть целым числом от 0 до 100
        """
        sum_ = 0
        count = 0
        for subject in self.subjects.keys():
            sum_ += sum(self.subjects[subject]['grades'])
            count += len(self.subjects[subject]['grades'])
        return sum_ / count

    def cmd_launch(self):
        parser = argparse.ArgumentParser(prog='add_grade')
        parser.add_argument('-sbj', '--subject', default='Математика')
        parser.add_argument('-gr', '--grade', default=5)
        args = parser.parse_args()
        return self.add_grade(f'{args.subject}', int(args.grade))


if __name__ == "__main__":

    # тесты
    import doctest
    doctest.testmod(verbose=True)

    # запуск из консоли
    # python .\homework\hw15\ex01.py -sbj История -gr 4
    s5 = student = Student('Лев Толстой', 'homework/hw15/subjects.csv')
    s5.cmd_launch()
    print(s5)
    print(f"Средний балл: {s5.get_average_grade()}")

    # еще пример
    student = Student('Иван Иванов', 'homework/hw15/subjects.csv')
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    # student.add_test_score("Математика", 285)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    # student.add_test_score("История", 192)
    print(f"Средний балл: {student.get_average_grade()}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    print(student)

    Student('ван Иванов', 'homework/hw15/subjects.csv')
