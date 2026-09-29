import difflib
from pathlib import Path
data = Path(__file__).parent / 'data'
old = data / 'old.md'
new = data / "new.md"
with open(old,'r',encoding = 'utf-8') as f1,\
    open(new,'r',encoding='utf-8') as f2:
    old_lines = [In.strip() for In in f1]
    new_lines = [In.strip() for In in f2]
    diff = difflib.unified_diff(
    old_lines, new_lines,
    fromfile="old.md", tofile="new.md",   # 让 --- +++ 头部显示文件名
    lineterm="",
)
print("\n".join(diff))