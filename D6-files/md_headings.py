from pathlib import Path
DATA = Path(__file__).parent / 'data'
p = DATA / 'demo.md'
if not p.exists():
    raise FileNotFoundError(f"文件路径不存在:{p!r}")

with open(p,'r',encoding = 'utf-8') as f:
    for line in f:
        count = 1
        if(line.startswith('#')):
            for i in range(len(line)):
                if line[i+1] == '#':
                    count += 1
                else:
                    if line[i+1] == ' ':
                        print(f"H[{count}] {line[i+2:]}")
                    break

        else:
            pass