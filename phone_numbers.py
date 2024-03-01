import pandas as pd
import time

start = time.time()
print(start)

# Загрузка данных из файлов Excel
df_numbers = pd.read_excel('Номера0.xlsx')
df_regions = pd.read_excel('оптимизированная_таблица2.xlsx')


# Функция для определения региона по номеру телефона
def define_region(number):
    number = str(number)[1:]
    for index, row in df_regions[df_regions['АВС/ DEF'] == int(number[:3])].iterrows():
        if (
            number.startswith(str(row['АВС/ DEF'])) and
            int(number[3:]) <= row['До'] and
            int(number[3:]) >= row['От']
        ):
            return row['Регион']
    return 'Регион не найден'


# Добавление столбца с регионами к первой таблице
df_numbers['Регион'] = df_numbers['Номер'].apply(define_region)


# Сохранение результата в новый файл Excel
df_numbers.to_excel(f'Результат_янв_фев_4.xlsx', index=False)

end = time.time()

print(end - start)
