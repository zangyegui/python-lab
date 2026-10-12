class ValidationError(Exception):
    def __init__(self, field,value,reason):
        super().__init__(f"{field}={value!r}不合法:{reason}")
        self.field = field
        self.value = value
        self.reason = reason
def validate_score(score):
    if isinstance(score,(int,float)):
        if 0<= score <= 100:
            return True
        else:
            raise ValidationError("score",score,"score not in [0,100]!")
    else:
        raise TypeError(f"{score!r} is not a number!")
def validate_username(name):
    if isinstance(name,str):
        if 3 <= len(name) <= 20:
            return True
        else:
           raise ValidationError("name",name,"thec length of name is not in [3,20]!") 
    else:
        raise TypeError(f"{name} is not str!")

def main():
    try:
        print(validate_score(5))
    except ValidationError as e:
        print(e)
    except TypeError as e:
         print(e)
    
    try:
        print(validate_score('5'))
    except ValidationError as e:
        print(e)
    except TypeError as e:
             print(e)

    try:
        print(validate_score(101))
    except ValidationError as e:
            print(e)
    except TypeError as e:
             print(e)

    try:
        print(validate_username("zangyegui"))
    except ValidationError as e:
            print(e)
    except TypeError as e:
             print(e)

    try:
        print(validate_username("zy"))
    except ValidationError as e:
            print(e)
    except TypeError as e:
             print(e)
        
    try:
        print(validate_username(6))
    except ValidationError as e:
            print(e)
    except TypeError as e:
             print(e)

if __name__ == '__main__':
    main()

