print('Выввод информации о промежутке времени.')
sec = int(input('duration = '))
h = (sec // 3600)
m = (sec // 60) % 60
s = (sec % 60)
print(str(h) + ' hour')
print(str(m) + ' min')
print(str(s) + ' sec')