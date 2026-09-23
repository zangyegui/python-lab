def ScoreGroup(dic):
    D  = {"优秀":[],"良好":[],"及格":[],"不及格":[]}
    for person,value in dic.items():
        if value >= 90:
            D["优秀"].append(person)
        elif value >= 80:
            D["良好"].append(person)
        elif value >= 60:
            D["及格"].append(person)
        else:
            D["不及格"].append(person)
    return D
    

#测试用例
d = {"A":60,"B":50,"C":70,"D":85,"F":90,"G":95,"H":99}
D = ScoreGroup(d)
print(D)