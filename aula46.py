for i in range(10):
    if i == 2:
        print ('i é 2, pulandooo')
        continue

    if i == 8:
        print ('i é 8, você não chegará no else')
        break    

    for j in range(1, 3):
        print (i, j)

else:
    print ('for completo!!')
