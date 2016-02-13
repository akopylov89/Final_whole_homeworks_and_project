def bubble_sort(sorted_list):
    n = 1
    while n < len(sorted_list):
        for i in range(len(sorted_list)-n):
            if sorted_list[i] > sorted_list[i+1]:
                sorted_list[i],sorted_list[i+1] = sorted_list[i+1],sorted_list[i]
        n += 1

def python_sort(sorted_list):
    sorted_list.sort()

if __name__ == '__main__':
    import datetime
    import random
    N = [100, 1000,3000]
    f = open('results.csv', 'w+')
    a = []
    b = []
    for n in N:
        for i in range(5):
            sorted_list = range(n)
            random.shuffle(sorted_list)
            start = datetime.datetime.now()
            bubble_sort(sorted_list)
            finish = datetime.datetime.now()
            c = str(finish-start)
            c = c.split(':')
            if c[2][0] == '0':
                a.append(float(c[2][1:]))
            else:
                a.append(float(c[2]))
            sorted_list = range(n)
            random.shuffle(sorted_list)
            start2 = datetime.datetime.now()
            python_sort(sorted_list)
            finish2 = datetime.datetime.now()
            d = str(finish2-start2)
            d = d.split(':')
            if d[2][0] == '0':
                b.append(float(d[2][1:]))
            else:
                b.append(float(d[2]))
    a.sort()
    b.sort()
    sorted_a = a[1:4]+a[6:9]+a[11:14]
    sorted_b = b[1:4]+b[6:9]+b[11:14]
    number = [100,100,100, 1000,1000,1000,3000,3000,3000]
    sort1 = a[1:4]
    sort2 = a[6:9]
    sort3 = a[11:14]
    psort1 = b[1:4]
    psort2 = b[6:9]
    psort3 = b[11:14]
    data = [sort1,sort2,sort3]
    data2=[psort1,psort2,psort3]
    for i in number:
        f.write("%s" % i)
        for j in data:
            f.write("%s" % j)
        for k in data2:
            f.write("%s" % k)
        f.write('\n')
    f.close()

