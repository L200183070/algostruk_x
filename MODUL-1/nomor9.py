def kelipatan(x):
    for i in range (x):
        if(i<=0):
            pass
        elif (i%3==0 and i%5==0):
            print ('Phython UMS')
        elif(i%3==0):
            print ('Phyton')
        elif (i%5==0):
            print ('UMS')
        else:
            print (i)
