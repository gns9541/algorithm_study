N = int(input())
t = [list(map(int, input().split())) for _ in range(N)]
t = sorted(t, key = lambda x : (x[1], x[0]))
# print(time_sort)
end = 0
cnt = 0
for a, b in t:
    if a >= end:
        cnt += 1
        end = b
print(cnt)

# time_lst = sum(time,[])
# lst_fianl = []
# for i in range(N):
#     lst = [time[i]]
#     j = 0
#     while j<N:
#         if time[i][1] > time[j][0]:
#             j += 1
#         elif time[i][1] <= time[j][0]:
#             lst.append(time[j])
#             i = j
#         if j == N or time[i][1] == max(time_lst):
#             break
#     lst_fianl.append(len(lst))
# print(max(lst_fianl))