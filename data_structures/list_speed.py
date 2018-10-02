import timeit

time = 0
cnt = 100
for i in range(cnt):
    time += timeit.timeit('lst[6]', setup='lst = [1, 10, 20, 4, 100, 4, 2, 8, 100, 3, 200]')

print("Access: {}".format(time/float(cnt)))

time = 0
for i in range(cnt):
    time += timeit.timeit('4 in lst', setup='lst = [8, 10, 11, 4, 100, 4, 2, 8, 100, 3]')

print("Search: {}".format(time/float(cnt)))

