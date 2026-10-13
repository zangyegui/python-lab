import json
from pathlib import Path
from dataclasses import dataclass
from functools import wraps
import time


def timer(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start = time.perf_counter()
            result = func(*args,**kwargs)
            interval = time.perf_counter() - start
            print(f"{func.__name__}耗时{interval}秒")
            return result
        return wrapper

@dataclass
class SensitiveFilter:
    #调用方并没有变短，甚至变长了，需要先实例化对象，但这样更标准化，禁词表和过滤方法封装在一起，方便使用
    #词表的维护责任归对象了，属于过滤波器对象的属性
    #当函数的参数和方法本身并没有强关联的时候，比如函数的参数是普通的整数，列表等，没有特定格式要求，直接使用裸函数更轻便
    banned:dict[str,str]
    
    @timer
    def filter(self,text:str)->tuple[str,dict[str,int]]:
        '中文词汇过滤无边界，存在误伤，正式版本修复这个问题'
        result = []
        count_dict = {}
        banned_words = sorted(self.banned.keys(),key = len,reverse = True)
        i = 0
        txt = text.lower()
        while i < len(txt):
            matched = None
            for word in banned_words:
                if not word:
                    continue
                if txt.startswith(word,i):
                    matched = word
                    break
            if matched is not None:
                result.append(self.banned[matched])
                count_dict[matched] = count_dict.get(matched,0)+1
                i += len(matched)
            else:
                result.append(txt[i])
                i += 1
        return (''.join(result),count_dict)

def main():
    text = []
    path_config = Path(__file__).parent / "config.json"
    path_target = Path(__file__).parent / "target.txt"
    with open(path_config,'r',encoding='utf-8') as f:
        obj = json.load(f)
    with open (path_target,'r',encoding = "utf-8") as f:
        for line in f:
            text.append(line.strip())
    words_filter1 = SensitiveFilter(obj["mask_map1"])
    print(SensitiveFilter.filter.__name__)
    print(words_filter1.filter(f"{' '.join(text)}"))
    


if __name__ == "__main__":
    main()