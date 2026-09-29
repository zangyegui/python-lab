from pathlib import Path

DATA = Path(__file__).parent / "data"
p = DATA / "corpus.txt"
if not p.exists():
    raise FileNotFoundError(f"path not exists!{p!r}")#文件地址错误后续代码没有执行意义会一直错
line_count = 0
not_blank_lines = 0
words_count = 0
char_length = 0
with open (p,'r',encoding = 'utf-8' )  as f:
    while(True):
        line_str = f.readline()
        if(line_str != ''):
            line_count +=1
            if(line_str.strip()):
                not_blank_lines += 1
            words = line_str.split()
            for word in words:
                word = word.strip(",.?")
                char_length += len(word)
            words_count += len(words)
            
        else:
            break
print(line_count,not_blank_lines,words_count,char_length)


