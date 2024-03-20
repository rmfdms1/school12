import random
f=open('voca.txt','r',encoding='UTF-8')
raw_data=f.read()
f.close()
print(raw_data.split('\n')[-1])
data_list=raw_data.split('\n')
data_list=data_list[:-1]
while True:
    r_index=random.randrange(0,len(data_list))
    word=data_list[r_index].replace(u'\xa0',u' ').split(' ')[1]
    if len(word) <= 6 :break
word=word.upper()
#단어의 글자 수만큼 밑줄을 긋는다
word_show="_"*len(word)
print(word_show)
try_num=0
ok_list=[]
no_list=[]
while True:
    #b가 단어에 포함될거 같은 알파벳을 하나 말한다
    ans=input().upper()
    print(ans)
    #알파벳이 단어에 포함되면 밑줄에 알파벳을 채워놓고
    #포함되지 않는다면 사람을 1회씩 그린다
    result=word.find(ans)
    print(result)
    if result == -1: #없음
        print('오답')
        try_num +=1
        no_list.append(ans)
    else :#있음
        print('정답')
        ok_list.append(ans)
        for i in range(len(word)):
            if word[i]==ans:
                word_show= word_show[:i]+ans+ word_show[i+1:]
                #asdfg ->asDfg -> as + D +fg
        print(word_show)
    #사람이 먼저 완성되면 출제자 A가 이긴다.
    if try_num==19:break
    #단어가 먼저 완성되면 맞힌 사람 B가 이긴다