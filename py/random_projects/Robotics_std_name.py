names = []
with open("names", "r") as f:
    lines = f.readlines()
    for line in lines: 
        line = line.split(" ")
        print(f' \"{line[0].title()} {line[1][:-1].title()}",')
        # print(line[0].title() + " " + line[1].title())


# 


