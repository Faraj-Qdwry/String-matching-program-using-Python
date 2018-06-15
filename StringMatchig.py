# 1 filtering words in (accidents.tst and saving into filtered)
# packages to install

# pip install nltk
# pip install stopwords
# python -m pip install --upgrade pip
# pip install plotly
# pip install plotly --upgrade

import string
from nltk.corpus import stopwords
import plotly
import plotly.graph_objs as go

filetoCheck = "business2.txt"
 #1
with open(filetoCheck, 'r') as inFile, open('filteredtext.txt', 'w') as outFile:
    for line in inFile.readlines():
        print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                        if len(word) >= 4 and word not in stopwords.words('english')]), file=outFile)

# ============================= 2  printing cecked & filteredtext.txt contents

checked = open(filetoCheck)
accidentswds = []
for lin in checked:
    lin = lin.rstrip()
    # print(lin)
    for wor in lin.split():
        accidentswds.append(wor)



accidentsFile = open('filteredtext.txt')
filteredwds = []
for lin in accidentsFile:
    lin = lin.rstrip()
    # print(lin)
    for wor in lin.split():
        filteredwds.append(wor)

print(accidentswds)
print(filteredwds)

# ================= ploting    Filtered Words      +     With stop-Words

withStopWords = len(accidentswds)
filteredWords = len(filteredwds)

print(str(filteredWords) + "\n" + str(withStopWords) + "\n\n")

data = [go.Bar(
    x=['Filtered Words', 'With stop-Words'],
    y=[filteredWords, withStopWords],
)]

plotly.offline.plot(data, filename='filtered-stopwords-bar.html')

# checking the FilteredWords how many are positive and how many are negative
# getting positive words from the file

positiveFile = open('posfile.txt')
positivewords = []
for lin in positiveFile:
    lin = lin.rstrip()
    # print(lin)
    for wor in lin.split(', '):
        # print(wor.lower())
        positivewords.append(wor)

# getting the negative words from the file
negativeFile = open('negfile.txt')
negativewords = []
for lin in negativeFile:
    lin = lin.rstrip()
    # print(lin)
    for wor in lin.split(', '):
        # print(wor.lower())
        negativewords.append(wor)

# checking
print(str(len(positivewords)) + " pos + neg " + str(len(negativewords)))

posativity, negativitiy, neither = 0, 0, 0

print("")
for word in filteredwds:
    word = word.lower()
    if positivewords.__contains__(word):
        posativity += 1
    elif negativewords.__contains__(word):
        negativitiy += 1
        print("Negative word --> " + word)
    else:
        neither += 1

print("")

print("( "+str(posativity)+"Positive Words ) -- ( ", str(negativitiy)+" Negative word ) -- ( ", str(neither)+" Natural Words )")

# ==============================  ploting positive negative and natural words

data = [go.Bar(
    x=['Negative word', 'Positive Words', 'Natural Words'],
    y=[negativitiy, posativity,neither]
)]

plotly.offline.plot(data, filename='pos-neg-non.html')
