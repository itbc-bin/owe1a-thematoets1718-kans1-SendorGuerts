def main():
    file = open("yeast_genes.csv")
    yeastcsvdata = read_file(file)
    not_validated(yeastcsvdata)
    ion_involved(yeastcsvdata)
def read_file(file):
    yeastcsvdata = []
    for line in file:
        line = line.split(',')
        yeastcsvdata.append(line)
    return yeastcsvdata
def not_validated(yeastcsvdata):
    aantalverified = 0
    aantalnotverified = 0
    acc_code_notverified = []
    for sublijst in yeastcsvdata:
        if "Verified" in sublijst:
            aantalverified += 1
        else:
            aantalnotverified += 1
            acc_code_notverified.append(sublijst[0])
    print("Number of unverified genes: ", aantalnotverified)
    print("accesscodes of unverified genes: ")
    for i in acc_code_notverified:
          print (i)
    return aantalnotverified, acc_code_notverified
def ion_involved(yeastcsvdata):
    aantalion = 0
    for line in yeastcsvdata:
        if "Verified" not in line:
            if "ion" in line:
                aantalion += 1
    print("Number involved in ion precesses: ", aantalion)
    return aantalion
main()