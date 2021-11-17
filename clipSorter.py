import os
import shutil

path = 'B:\\braul\Videos\Valorant'

listOfFiles = os.listdir(path)

listOfDic = {}

for file in listOfFiles:
    listOfDic[file] = len(os.listdir(path + "\\" + file))
    # print(file + ": " + str(len(os.listdir(path + "\\" + file))))

listOfDicSort = dict(sorted(listOfDic.items(), key=lambda item: item[1]))
listOfDicSort = dict(reversed(list(listOfDicSort.items())))

for file in listOfDicSort:
    print(file + ': ' + str(listOfDicSort[file]))
    

for file in listOfFiles:
    if '2020' in file:
        if '-01-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Jan - 2020')
        elif '-02-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Feb - 2020')
        elif '-03-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Mar - 2020')
        elif '-04-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'April - 2020')
        elif '-05-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'May - 2020')
        elif '-06-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'June - 2020')
        elif '-07-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'July - 2020')
        elif '-08-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Aug - 2020')
        elif '-09-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Sep - 2020')
        elif '-10-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Oct - 2020')
        elif '-11-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Nov - 2020')
        elif '-12-' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Dev - 2020')
    if '2021' in file:
        if '2021.01.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Jan - 2021')
        elif '2021.02.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Feb - 2021')
        elif '2021.03.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Mar - 2021')
        elif '2021.04.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'April - 2021')
        elif '2021.05.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'May - 2021')
        elif '2021.06.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'June - 2021')
        elif '2021.07.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'July - 2021')
        elif '2021.08.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Aug - 2021')
        elif '2021.09.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Sep - 2021')
        elif '2021.10.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Oct - 2021')
        elif '2021.11.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Nov - 2021')
        elif '2021.12.' in file:
            shutil.move(path + '\\' + file, path + '\\' + 'Dec - 2021')

