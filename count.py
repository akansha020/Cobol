for i in range(1, 10):
    if(i%5==0):
        continue
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
