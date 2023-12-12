from sem_package.ex05 import mystery_game
from sem_package.ex06 import validate_date

if __name__ == "__main__":
    print(mystery_game('Зимой и летом одним цветом',
                       ['ель', 'ёлка', 'сосна'], 3))
    print(validate_date('29.04.2024'))
