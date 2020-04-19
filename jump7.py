for i in range(1,101):
    if i % 7 == 0 or  i //10 == 7 or i % 7  == 10: #这里掉了个冒号，试了半
        continue
    else:
        print(i)
