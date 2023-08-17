def work_1(courses, mentors):


    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])


    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    top = []
    for top_3_el in top_3:
        top.append(f'{top_3_el[0]}: {top_3_el[1]} раз(а)')
    result = (', '.join(top))
    print(type(result))
    return result

if __name__ == '__main__':

    work_1()