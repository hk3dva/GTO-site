import pandas as pd

gto = pd.read_excel('D:/GTO/gto_site/static/' + 'table.xlsx', sheet_name=None)

def clean(line): #предварительная отчистка данных для сравнения
    new = line[line.find('от') + 3 :].split()
    new.pop(1)
    new.pop(-1)
    return new

def comp(intList, age):  #функция сравнения возрастов
    b = 200
    if intList[1] != 'и':
        b = int(intList[1])
    return int(intList[0]) <= age <= b

def get_standard(df, age):  #возвращает df по возрасту
    for sheet in df.keys():
        if comp(clean(df[sheet].iloc[0][1]), age):
            return df[sheet]

def init(df):  # первичное преобразование таблицы
    #Замена Nan в строке пола
    for index, el in enumerate(df.iloc[1][1:]):
        if pd.isna(el):
            df.iloc[1][index + 1] = df.iloc[1][index]

    #Замена Nan в строке номера упражнения
    for index, el in enumerate(df.iloc[2][1:]):
        if pd.isna(el):
            df.iloc[2][index + 1] = df.iloc[2][index]
    return df

def gender_df(df, g = 0):  # получает в качестве параметров таблицу и пол  0 - М,  1 - Ж
    res = [0,]
    if not g:
        gender = df.iloc[1][1]
    else:
        gender = df.iloc[1][-1]
    for index, el in enumerate(df.iloc[1][1:]):
        if el == gender:
            res.append(index + 1)
    return df.iloc[:, res]

def get_sport_type_column(df, name): # получить колонку по определенному виду спорта
    res = [0,]
    for index, el in enumerate(df.iloc[3][1:]):
        if el == name:
            res.append(index + 1)
    return df.iloc[:, res]

def get_sport_type(df): # Получение видов спорта из df
    resList = []
    prev = df.iloc[2][1:][0]
    res = []
    for index, el in enumerate(df.iloc[2][1:]):
        if el != prev:
            resList.append(res)
            res = []
            prev = el
        res.append(df.iloc[3][1:][index])
    resList.append(res)
    return resList