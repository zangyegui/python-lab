import json
from pathlib import Path

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
    p = Path(__file__).parent / "data" / "rename_test" / "config.json"
    txt = "我打你这个卖暴力游戏的家伙,NigHting"

    with open(p,'r',encoding = 'utf-8') as f:
        obj = json.load(f)
    banned_words = obj.get("banned_words")
    if not banned_words:
        raise ValueError("缺失禁词表")
    masks = obj.get("mask_map",{})
    mask_map = {w:masks.get(w,'*') for w in banned_words}

    print(filter_text(txt,mask_map))

if __name__ == "__main__":
    main()

