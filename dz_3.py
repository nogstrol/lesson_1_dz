percent = 'процент'
count = 1
while count <= 100:
    if count > 4 and count < 20:
        print(count, percent + 'процентов')
    elif count % 10 == 1:
        print(count, percent)
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
        print(count, percent + 'процента')
    else:
        print(count, percent + 'процентов')
    count +=1