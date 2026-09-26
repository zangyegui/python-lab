def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if  n % i == 0:
            return False
    return True

def word_freq(text):
    d = {}
    for w in text.lower().split():   # 小写 + 切词
        w = w.strip(".,")            # Bug1：接住返回值
        if not w:                    # Bug2：剥空了的词跳过
            continue                 # Bug3：不删列表，跳过即可
        d[w] = d.get(w, 0) + 1
    return d

if __name__ == '__main__':
    print("该工具已加载")