import csv
import numpy as np

mark = []
m = 0
sc = {}
score = {}
words = []
line = []
weight = np.array([[1],[10],[20]])

def rolling_window(seq,window_size):
    it = iter(seq)
    win = [next(it) for t in range(window_size)]
    yield win
    for e in it:
        win[:-1] = win[1:]
        win[-1] = e
        # print(win)
        yield win

def window_dict(dic):
    for j in range(len(dic)):  # line
        check=[]
        if len(dic[j])<3:
            s=len(dic[j])
        else:
            s=3
        for size in range(s):    # size 0-max len of line||max lenght in dic
            point = 0
            for w in rolling_window(dic[j],size+1):  # start roll the window
                # check point
                if '-'.join(w) in sc:
                    point+=sc['-'.join(w)]
                # else:
                #     point-=1
            check.append(point)
        while len(check) < 3:
            check.append(0)
        # check[0]=check[0]/len(dic[j])
        # check[1]=check[1]/(len(dic[j])-1)
        # check[2]=check[2]/(len(dic[j])-2)
        mark.append(check)

def csv2key():
    sc.clear()
    with open('percentage.csv','r') as readfile:
        reader = csv.reader(readfile)
        lines = list(reader)
        for i in range(len(lines)):
            sc[lines[i][0]]=float(lines[i][1])
            words.append(lines[i][0].split('-'))
    readfile.close()

def word2list():
    exam = open('text.txt','r')
    for read in exam:
        a = read.split(',')
        for i in range(len(a)):
            a[i]=a[i][:5]
        line.append(a)
    exam.close()

csv2key()
word2list()
# print(line)

window_dict(line)

mark = np.array(mark)
# print(mark)
# print(weight)
ans = mark.dot(weight)
print()
# print(ans)

# result = np.where(ans == max(ans))

# print()
# for i in result[0]:
#     print(line[i])

for i in range(len(line)):
    score['-'.join(line[i])]=ans[i][0]

# for key in score.keys():
#     print("%s : %s" % (score[key],key))

for k in sorted(score.items(), key = lambda kv:(kv[1], kv[0]),reverse = True):
    print("%s : %s" % (k[1],k[0]))


print()