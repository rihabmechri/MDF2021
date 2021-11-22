import re
lines = [
    "5",
    "1 08:45-12:59",
    "3 11:09-11:28",
    "5 09:26-09:56",
    "5 16:15-16:34",
    "3 08:40-10:12"
]
N = lines[0]


def ParseTime(timeString):
    '''
        in: timeString (day hh:mm-hh:mm)
        out: timeList [day, total min of the start, total min of the end]
    '''
    p = re.compile(r'\d+')
    listTime = list(map(int, p.findall(timeString)))
    return [
        listTime[0], listTime[1] * 60 +
        listTime[2], listTime[3] * 60 + listTime[4]
    ]


def CastTime(timeList):
    day = timeList[0]
    times = []
    times += [timeList[1] // 60]
    times += [timeList[1] % 60]
    times += [timeList[2] // 60]
    times += [timeList[2] % 60]
    return '{0} {1}:{2}-{3}:{4}'.format(day, *map(lambda x: str(x).rjust(2, '0'), times))


def solve(lines):
    calendar = [[0 for i in range(10*60)] for j in range(5)]

    for line in lines[1:]:
        time = ParseTime(line)
        for minute in range(time[1] - 8* 60, time[2] - 8 * 60 + 1):
            calendar[time[0] - 1][minute] = 1

    found = False
    for day in range(5):
        for minute in range(9 * 60):
            if all(calendar[day][minute + x] == 0 for x in range(60)):
                rep = CastTime([day+1, minute + 8*60, minute + 9*60 - 1])
                found = True
                break
        if found:
            break

    return rep


print(solve(lines))
