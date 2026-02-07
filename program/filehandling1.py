def unique(f):
    word=""
    uni=set()
    frequ=[]
    for i in f.read():
        i=i.lower()
        if i not in " ,.!\n" :
            word+=i
        else:
                frequ.append(word)
                uni.add(word)
                word=""
    if word:
        frequ.append(word)
        uni.add(word)
    return uni,frequ


def frequency(f,frequ):
    res={}
    avoid=["is","and", "in", "of", "the", "for","a","it","its","which"]
    for i in frequ:
        if i!="" and i not in avoid:
             if i in res:
                  res[i]+=1
             else:
                  res[i]=1
    return res,sum(1 for i in frequ if i!= "")


f=open(r"C:Docs\Sample_Text.txt", "r")

uni,frequ=unique(f)
top,count=frequency(f,frequ)
top5= dict(sorted(top.items(), key=lambda x:x[1], reverse=True)[:5])
print("No.of total words present in file:", count, )
print("No of unique words:", len(uni),)
print("Top 5 most frequent words: ", top5)
f.close()