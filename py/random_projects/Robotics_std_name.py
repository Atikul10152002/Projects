with open("/Users/atikul/Downloads/Robotics Roster - Sheet1.csv", "r") as f:
    lines = f.readlines()
    for line in lines: 
        line = line.split(",")
        print(f' \"{line[0].title()} {line[1].title()}",')


