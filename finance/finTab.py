import csv
import os

def getFiles(dir_path):
  import os
  res = []
  for path in os.listdir(dir_path):
      if os.path.isfile(os.path.join(dir_path, path)):
          res.append(path)
  return res

annotators = ['Kushagra', 'Leena', 'Sulagna']
maxData = 0
data = {}



for i in range(len(annotators)):
    name = annotators[i]
    dirPath = name
    fileList = getFiles(dirPath)

    for fileName in fileList:
        file = open(dirPath+'/'+fileName, 'r')
        cr = csv.reader(file)

        line = 0
        for i in cr:
            if line > 0:
                tableNum = eval(i[0].split('-')[1])
                refText = i[1].strip()
                maxData = max(maxData, tableNum)
                data[tableNum] = refText
            line += 1
        file.close()


print('Maximum Number of Tables: ', maxData)

file = open('refFinTab.txt', 'w', encoding='utf-8')
for i in range(maxData):
    try:
        file.write(data[i])
    except KeyError:
        pass
    file.write('\n')
file.close()
