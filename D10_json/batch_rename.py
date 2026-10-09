from pathlib import Path

def choice_input(s):
    while True:
        choice = input(s)
        if choice.lower() in ['y','n']:
            return choice
        
folder = Path(__file__).parent / "data" / "rename_test"
plan = []
i = 0
print("请确认改名清单:")
for f in folder.iterdir():
    if f.suffix == ".txt":
        i += 1
        new_name = f"炼丹语料_{i:03d}.txt"
        plan.append((f,folder / new_name))
for old,new in plan:
    print(f"{old.name}→{new.name}")

choice = choice_input("Are you sure you want to rename in bulk? Y/N\n")

if choice.lower() == 'y':
    for old,new in plan:
        if new.exists():
            print("target name exists!")
            continue
        old.rename(new)
