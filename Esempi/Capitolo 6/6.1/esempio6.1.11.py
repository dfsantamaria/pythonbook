def concatena(stringa:str, num: int)->str|None:
    def valida_str(stringa, num)->bool:
        if isinstance(stringa, str) and len(stringa)  > 0 \
        and isinstance(num, int) and num > 0:
            return True
        return False 
    if valida_str(stringa, num):
       return stringa*num
    return None 

print(concatena("messaggio", 2))