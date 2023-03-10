import json

def load_candidates():
    # '''
    # Загрузит данные из файла
    # '''
    # # загрузить из json
    with open('candidates.json', 'r', encoding='utf-8') as file:  # открываем файл на чтение
        data = json.load(file)  # загружаем из файла данные в словарь data
        return data


def get_all():
    # """
    # Покажет всех кандидатов
    # :return: результат load_candidates
    # """
    return load_candidates()

def get_by_pk(pk):
    # '''
    # :param pk: для того, чтобы вывести кандидата по введенному pk - порядковому номеру
    # :return: вернет кандидата по pk
    # '''
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return "None"

def get_by_skill(skill):
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(", ")
        if skill in skills:
            result.append(candidate)
    return result


def get_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


