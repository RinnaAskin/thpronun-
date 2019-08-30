import csv

sc = {}
words = []
n = []

def dic2list():
    th_read =[]
    with open('except.tsv','rt', encoding = "utf-8") as thaiRead:
        rd = csv.reader(thaiRead, delimiter='\t')
        for row in rd:
            th_read.append(row[1])
    thaiRead.close()
    # print(len(th_read))
    for line in range(len(th_read)):
        if ';' in th_read[line]:
            multi = th_read[line].split(';')
            del th_read[line]
            for n in range(len(multi)):
                th_read.insert(line+n,multi[n])
    for word in th_read:
        if ',' in word:
            a = word.split(',')
            for i in range(len(a)):
                a[i]=a[i][:5]
            words.append(a)
        else:
            b=[]
            b.append(word[:5])
            words.append(b)


def rolling_window(seq,window_size):
    it = iter(seq)
    win = [next(it) for t in range(window_size)]
    yield win
    for e in it:
        win[:-1] = win[1:]
        win[-1] = e
        # print(win)
        yield win
        

def csv2key():
    sc.clear()
    with open('test.csv','r') as readfile:
        reader = csv.reader(readfile)
        lines = list(reader)
        for i in range(len(lines)):
            sc[lines[i][0]]=int(lines[i][1])
    readfile.close()

def window_dict(dic):
    for j in range(len(dic)):
        if len(dic[j])<3:
            s=len(dic[j])
        else:
            s=3
        for size in range(s):
            for w in rolling_window(dic[j],size+1):
                # check point
                if '-'.join(w) in sc:
                    sc['-'.join(w)]+=1
                else:
                    sc['-'.join(w)]=1

def add_dict():
    with open('test.csv','w') as f:
        for key in sc.keys():
            f.write("%s,%s\n" % (key,sc[key]))
    f.close()

def dic2per():
    with open('percentage.csv','w') as p:
        for key in sc.keys():
            p.write("%s,%s\n" % (key,sc[key]/n[len(key.split('-'))-1]))
    p.close()

def get_sum():
    a=0
    b=0
    c=0
    for w in sc.keys():
        line = len(w.split('-'))
        if line == 1:
            a+=sc[w]
        elif line == 2:
            b+=sc[w]
        else:
            c+=sc[w]
    n.append(a)
    n.append(b)
    n.append(c)


# dic2list()
# window_dict(words)
# add_dict()
csv2key()
get_sum()
print(n)
dic2per()