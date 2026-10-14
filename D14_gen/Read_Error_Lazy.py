from pathlib import Path

def read_error(path):
    with open(path,"r",encoding="utf-8") as f1:
        for row in f1:#日志每一行的头都是年月日时分秒，长度固定
            if row.startswith('ERROR',20):
                yield row

def main():
    log = Path(__file__).parent / "data" / "run.log"
    gen = read_error(log)
    error_list = []
    while True:
        try:
            error_list.append(next(gen))
        except Exception:
            break
    print(len(error_list))

if __name__ == "__main__":
    main() 
