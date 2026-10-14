from pathlib import Path
log = Path(__file__).parent / "data" / "run.log"
content = []
with open(log,"r",encoding="utf-8") as f:
    for line in f:
        content.append(line)
for i in range(50000):
    with open(log,"a",encoding="utf-8") as f:
        for line in content:
            f.write(line)

