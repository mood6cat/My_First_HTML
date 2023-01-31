import json

def load_candidates():
    '''
    �������� ������ �� �����
    '''
    # ��������� �� json
    with open('candidates.json', 'r', encoding='utf-8') as file:  # ��������� ���� �� ������
        data = json.load(file)  # ��������� �� ����� ������ � ������� data
        return data


def get_all():
    """
    ������� ���� ����������
    :return: ��������� load_candidates
    """
    return load_candidates()

def get_by_pk(pk):
    '''
    :param pk: ��� ����, ����� ������� ��������� �� ���������� pk - ����������� ������
    :return: ������ ��������� �� pk
    '''
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return

# def get_by_skill(skill_name):
#     '''
#     :param skill_name: �����
#     :return:������� ������ ���������� �� ������
#     '''
#     # candidates = []
#     # for candidate in load_candidates():
#     #     if skill_name.lower() in candidate['skills'].lower().split(', '):
#     #         candidates.append(candidate)
#     #         return candidates


def get_by_skill(skill):
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(", ")
        if skill in skills:
            result.append(candidate)
    return result
print(get_by_skill("python"))

def get_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        names = candidate['name'].lower()
        if candidate_name in names:
            result.append(candidate)
    return result

