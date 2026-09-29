banned_dict = {"死":"*","暴力":"@","操":"￥","卖":"#","暴":"#"}

def filter_text(txt: str, banned: dict[str,str])->tuple[str,dict[str,int]]:
    result = []
    count_dict = {}
    banned_words = sorted(banned.keys(),key = len,reverse = True)
    i = 0
    while i < len(txt):
        matched = None
        for word in banned_words:
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
    txt = "我操死你这个卖暴力武器的家伙"
    print(filter_text(txt,banned_dict))

if __name__ == '__main__':
    main()