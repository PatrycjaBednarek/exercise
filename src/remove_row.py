
# remove first row from tsv

with open(r"C:\Users\patry\OneDrive\Documents\GitHub\imdb\data\data.tsv",'r', encoding="utf-8") as f:
    with open("dataa.tsv",'w',  encoding="utf-8") as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)