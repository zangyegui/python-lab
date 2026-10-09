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


p = Path(__file__).parent / "data" / "rename_test" / "config.json"
txt = "我操死你这个卖暴力武器的家伙,NigHting"
with open(p,'r',encoding = 'utf-8') as f:
    obj = json.load(f)
    for item in obj["banned_words"]:
        obj["mask_map"][item] = obj["mask_map"].get(item,'*')
    print(obj["mask_map"])
    if obj["banned_words"] == None or "banned_words" not in obj:
        raise ValueError("缺失禁词表")
    
    print(filter_text(txt,obj["mask_map"]))
