def concatena(stringa:str, num: int)->str|None:
    def valida_str(str_valida:str, num_valido:int)->bool:
        if isinstance(str_valida, str) and len(str_valida) > 0 \
        and isinstance(num_valido, int) and num_valido > 0:
            return True
        return False 
    if valida_str(stringa, num):
       return stringa*num
    return None 

print(concatena("messaggio", 2))