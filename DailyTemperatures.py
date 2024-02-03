temperatures  = [73,74,75,71,69,72,76,73]


def dailyTempeartures(temperatures):
    count = 1
    lst = []
    for i in range (len(temperatures)-1):
        if temperatures[i+1] > temperatures[i]:
            count += 1
        lst.append(count)


    return lst

print(dailyTempeartures(temperatures))