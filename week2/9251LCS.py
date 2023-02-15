w1 = input()
w2 = input()

def stack(word):
    result = [[]]
    for i in word:
        for j in range(len(result)):
            zip = result[j]
            result.append(zip + [i])
    return result

result1 = stack(w1)
result2 = stack(w2)

final = []
for i in result1:
    if i in result2:
        final.append(len(i))
print(max(final))
    
