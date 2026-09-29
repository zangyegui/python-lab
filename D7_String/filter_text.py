banned_dict = {"死":"*","暴力":"@","操":"￥","卖":"#","暴":"#","night":"sister"}#故意测试长短敏感词，替换规则随便设置的，不想全变成*

def filter_text(txt: str, banned: dict[str,str])->tuple[str,dict[str,int]]:
    '中文词汇过滤无边界，存在误伤，正式版本修复这个问题'
    result = []
    count_dict = {}
    banned_words = sorted(banned.keys(),key = len,reverse = True)
    i = 0
    txt = txt.lower()
    while i < len(txt):
        matched = None
        for word in banned_words:
            if not word:
                continue
            if txt.startswith(word,i):
                matched = word
                break
        if matched is not None:
            result.append(banned[matched])
            count_dict[matched] = count_dict.get(matched,0)+1
            i += len(matched)
        else:
            result.append(txt[i])
            i += 1
    return (''.join(result),count_dict)

def main():
    txt = "我操死你这个卖暴力武器的家伙,NigHting"
    print(filter_text(txt,banned_dict))

if __name__ == '__main__':
    main()