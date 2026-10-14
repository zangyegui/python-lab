from pathlib import Path

def read_error(path):
    error_list = []
    with open(path,"r",encoding="utf-8") as f1:
        for row in f1:#日志每一行的头都是年月日时分秒，长度固定
            if row.startswith('ERROR',20):
                error_list.append(row)
    return error_list

def main():
    log = Path(__file__).parent / "data" / "run.log"
    print(len(read_error(log)))

if __name__ == "__main__":
    main()  