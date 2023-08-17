
def work_3(courses, mentors, durations):



    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}


    for id, course in enumerate(courses_list):
        key = course['duration']
        # durations_dict[id] = key
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)


    durations_dict = dict(sorted(durations_dict.items()))


    result_1 = []
    for duration, ids in durations_dict.items():
        for id in ids:
            result = f'{courses_list[id]["title"]} - {duration} месяцев'

            result_1.append(result)
    print(result_1)
    return result_1

if __name__ == '__main__':
    work_3()