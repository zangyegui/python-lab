from pathlib import Path
data = Path(__file__).parent / 'data'
old = data / 'old.md'
new = data / "new.md"


def md_diff(old_md,new_md):
    new_list = []
    with open(old_md,'r',encoding = 'utf-8') as f1,\
         open(new_md,'r',encoding='utf-8') as f2:
        old_list = [In.strip() for In in f1]
        new_list = [In.strip() for In in f2]
        old_set = set(old_list)
        new_set = set(new_list)
        difference_lines=["===只在旧版==="]
        for i,old in enumerate(old_list):
            if old.strip() not in new_set:
                difference_lines.append((f"- line{i},被删除{old!r}"))
        difference_lines.append("===只在新版===")
        for j,new in enumerate(new_list):
            if new.strip() not in old_set:
                difference_lines.append(f"+ line{j},新增加{new!r}")
        return difference_lines

def main():
    for line in md_diff(old,new):
        print(line)

if __name__ == '__main__':
    main()       

                
                 
                    