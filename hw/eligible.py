def eligible(infile, outfile):
    f = open(infile, 'r')
    o = open(outfile, 'w')
    for line in f:
        lsplit = line.split(',')
        name = lsplit[0]
        age = lsplit[1]
        if int(age) >= 18:
            o.write(name.strip() + ', ' +  age.strip() + '\n')

# eliglble('community.txt', 'output.txt')
