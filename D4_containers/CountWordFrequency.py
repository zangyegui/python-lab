# def word_freq(text):
#     ls = text.lower().split()
#     for s in ls:
#         s.strip(",.")   ##易错点
#         if s == None:
#             ls.remove(s)
#     d = {}
#     for w in ls:
#         d[w] = d.get(w,0) + 1
#     return d

def word_freq(text):
    d = {}
    for w in text.lower().split():   # 小写 + 切词
        w = w.strip(".,")            # Bug1：接住返回值
        if not w:                    # Bug2：剥空了的词跳过
            continue                 # Bug3：不删列表，跳过即可
        d[w] = d.get(w, 0) + 1
    return d


s = "Mental rotation of visual stimuli is well studied. The key characteristic of mental rotation of visual stimuli is the linear relationship between the time required to perform a rotation task and the required angle of rotation, as shown first by Shepard and Metzler "

for word,count in sorted(word_freq(s).items(),key = lambda x: x[1],reverse=True):
    print(f"\'{word}\':{count}",end = ' ')
