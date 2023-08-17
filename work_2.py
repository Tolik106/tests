def work_2(courses, mentors):


    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = list(set(all_names_list))


    all_names_sorted = sorted(unique_names)
    all_names_str = ', '.join(all_names_sorted)
    result = (f'Уникальные имена преподавателей: {all_names_str}')
    print(result)
    return result

if __name__ == '__main__':

    work_2()