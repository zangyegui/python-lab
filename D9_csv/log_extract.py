from pathlib import Path
data = Path(__file__).parent / "data"
log = data / "run.log"
errorlog = data / "error.txt"
count_info = 0
count_debug = 0
count_error = 0
with open(log,"r",encoding="utf-8") as f1,\
    open(errorlog,"a",encoding = "utf-8")as f2:
    for row in f1:#日志每一行的头都是年月日时分秒，长度固定
        if row.startswith('INFO',20):
            count_info += 1
        elif row.startswith('DEBUG',20):
            count_debug += 1
        elif row.startswith('ERROR',20):
            count_error += 1
            f2.writelines(row)

print(f"info数量{count_info},debug数量{count_debug},error数量{count_error}")