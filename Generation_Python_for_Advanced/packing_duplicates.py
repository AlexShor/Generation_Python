s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()
result = [[s[0]]]
for i in range(1, len(s)):
    if result[len(result)-1][0] == s[i]:
        result[len(result)-1].extend(s[i])
    else:
        result.append([s[i]])
print(result)