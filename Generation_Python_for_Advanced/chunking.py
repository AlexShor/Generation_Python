s = input().split()
n = int(input())


def checked(string, ch):
    result = [[s[0]]]
    k = 0
    for i in range(1, len(string)):
        if i < ch:
            result[k].extend(string[i])
        else:
            result.append([string[i]])
            k += 1
            if ch > 1: ch += n
    return result


print(checked(s, n))