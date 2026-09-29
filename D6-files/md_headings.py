from pathlib import Path
DATA = Path(__file__).parent / 'data'
p = DATA / 'demo.md'
if not p.exists():
    raise FileNotFoundError(f"文件路径不存在:{p!r}")

with open(p,'r',encoding = 'utf-8') as f:
    for line in f:
        level = len(line) - len(line.lstrip('#'))
        content = line.lstrip('#').strip()
        if level > 0 and line.lstrip('#').startswith(' ') :
            print(f"H[{level}] {content}")