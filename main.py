import re

#СНИЛС в виде ХХХ-ХХХ-ХХХ ХХ

REGULAR = r"^\d{3}\-\d{3}\-\d{3} \d{2}$"

filename="test_snils.txt"

def match_snils(snils:str):
    return re.match(REGULAR,snils) is not None # вернет снилс, если найдет его

def find_snils_in_file():
    with open(filename,"r") as file:
        snils_arr = []
        for line in file:
            if match_snils(line):
                snils_arr.append(line[:-1])
    return snils_arr
def find_snils_on_site(URL:str):
    pass

def main():
    arr=find_snils_in_file()
    print(arr)
if __name__=="__main__":
    main()