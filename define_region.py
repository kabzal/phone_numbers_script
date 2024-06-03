import pandas as pd


# Функция для определения региона по номеру телефона
def define_region(number, df_regions):
    number = str(number)[1:] # Исключаем из номера первую цифру (обычно 7 или 8)

    # Итерируемся по строкам df_region, у которых поле 'АВС/ DEF'
    # совпадает с первыми тремя цифрами номера
    for index, row in df_regions[df_regions['АВС/ DEF'] == int(number[:3])].iterrows():
        if (
                number.startswith(str(row['АВС/ DEF'])) and
                row['До'] >= int(number[3:]) >= row['От']
        ):
            return row['Регион'] # Если номер соответствует диапазону, берется соответствующий регион
    return 'Регион не найден'


