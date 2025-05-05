import glob, csv
files = glob.glob("*.pdf")
exams = [x for x in files if x[0].isdigit()]
examnumbers = [x[:x.index('_')] for x in exams]
examnumbers.sort(key=int)
header = ['Student', 'Raw Score', 'Notes', 'Initial Grade', 'Curved Grade']
contents = [[x, ' ', ' ', ' ', ' '] for x in examnumbers]
with open('gradesheet.csv', 'w') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(header)
    csvwriter.writerows(contents)
