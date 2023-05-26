# Average of sort out elements that are divisible by seven (1,100)

# x = []
# for i in range(1,100):
#     if i%7==0:
#         x.append(i)
#
# total = sum(x)
# print('total of sum:',total)
# avg = total / len(x)
# print('THe average of :',avg)
# total of sum: 735
# THe average of : 52.5


sum = 0
i1 = 0

for i in range(1,100):
    if i%7==0:
        sum = sum+i
        i1 = i1 + 1
        print('iteration of:', i1)
        print('sum of :', sum)
        print()


print('sum of divisible of 7:',sum)
Avg = sum/i1
print('Average of :',Avg)



# iteration of: 1
# sum of : 7
#
# iteration of: 2
# sum of : 21
#
# iteration of: 3
# sum of : 42
#
# iteration of: 4
# sum of : 70
#
# iteration of: 5
# sum of : 105
#
# iteration of: 6
# sum of : 147
#
# iteration of: 7
# sum of : 196
#
# iteration of: 8
# sum of : 252
#
# iteration of: 9
# sum of : 315
#
# iteration of: 10
# sum of : 385
#
# iteration of: 11
# sum of : 462
#
# iteration of: 12
# sum of : 546
#
# iteration of: 13
# sum of : 637
#
# iteration of: 14
# sum of : 735
#
# sum of divisible of 7: 735
# Average of : 52.5

