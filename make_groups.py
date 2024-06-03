import pandas as pd


def make_groups(file_path):
    # Загрузка данных из файла Excel
    df = pd.read_excel(file_path)

    # Создаем пустой список для хранения групп
    groups = []

    # Итерируем по строкам и формируем группы
    for i in range(len(df)):
        if not groups or (df.at[i, 'АВС/ DEF'] == groups[-1]['АВС/ DEF']
                          and df.at[i, 'От'] == groups[-1]['До'] + 1
                          and df.at[i, 'Регион'] == groups[-1]['Регион']):
            # Добавляем текущую строку к последней группе или создаем новую группу
            if not groups:
                groups.append({
                    'АВС/ DEF': df.at[i, 'АВС/ DEF'],
                    'От': df.at[i, 'От'],
                    'До': df.at[i, 'До'],
                    'Регион': df.at[i, 'Регион']
                })
            else:
                groups[-1]['До'] = df.at[i, 'До'] # Если подходящая группа есть, расширяем диапазон
        else:
            # Создаем новую группу
            groups.append({
                'АВС/ DEF': df.at[i, 'АВС/ DEF'],
                'От': df.at[i, 'От'],
                'До': df.at[i, 'До'],
                'Регион': df.at[i, 'Регион']
            })

    # Создаем DataFrame из списка групп
    result_df = pd.DataFrame(groups)

    # Сохранение результата в новый файл Excel
    result_df.to_excel('оптимизированная_таблица.xlsx', index=False)
