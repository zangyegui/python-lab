class Paper:
    def __init__(self,title:str,authors:list[str],year:int,citations:int):
        self.title = title
        self.authors = authors
        self.year = year
        self.citations = citations

    def __repr__(self):
        return f"《{self.title}》作者:{'、'.join(self.authors)}"

    def __lt__(self,other):
        return self.citations < other.citations

    def cite_brief(self) -> str:
        if len(self.title.split()) < 2:
            raise ValueError(f"请检查标题长度不能小于2!{self.title!r}")
        return f"{self.authors[0]}({self.year}) {self.title.split()[0]} {self.title.split()[1]} ..." 

def main():
    piano = Paper("Tactile Reading: Real-Time Piano Playing with Electrotactile Aids for BVI Users",["My lover","Me"],2026,9)
    grasp = Paper("Tactile Grasp: ...",["My Lover"],2026,30)
    align = Paper("Tactile align: ...",["My lover","Me"],2026,10)
    graduate = Paper("Multi-finger tactile ...",["Me"],2025,0)
    model = Paper("Modeling the Noticeability of User-Avatar Movement Inconsistencyfor Sense of Body Ownership Intervention",["ZHIPENG LI", "YU JIANG"],2022,103)
    print(piano.cite_brief())
    print(piano)
    for paper in sorted([piano,grasp,align,graduate,model],reverse=True):
        print(f"文章：{paper.cite_brief()},引用数:{paper.citations}")

if __name__ == "__main__":
    main()
