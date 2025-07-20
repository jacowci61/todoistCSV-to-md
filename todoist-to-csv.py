import os
import pandas

def ParseTodoistData(file):
    file = file.drop([0,1], axis = 0) # removes rows
    columnsToExtract = [1,2,3] # indicies of columns to extract (1 task name, 2 task description, 3 priority)
    extractedData = pandas.DataFrame()
    for i in range(len(columnsToExtract)):
        extractedData[i] = file.iloc[:,columnsToExtract[i]]
    extractedData.reset_index(inplace = True, drop = True)
    return extractedData

# region Variables
todoistCSV = pandas.read_csv (r"C:\...\inputFile.csv")
todoistDF = ParseTodoistData(todoistCSV)
todoistSTR = []
_tempstr = ""
flag = 0
script_dir = os.path.dirname (os.path.abspath(__file__))
outputFile = open(os.path.join(script_dir, 'TodoistExport.md'), 'w')
# endregion

for i in range(len(todoistDF)-1):
    if (i==0):
        _tempstr += str("- [ ] " + todoistDF.iat[i,0] + "\n")
        for j in range(len(todoistDF.columns)):        
            if (j!=0) & ((todoistDF.isnull().iloc[i,j]) == False):
                # todoistSTR.append("\t" + str(todoistDF.iat[i,j]) + "\n")
                _tempstr += str("\t" + str(todoistDF.iat[i,j]) + "\n")
            else:
                continue
        todoistSTR.append(_tempstr)
        _tempstr = ""
    else:
        if (flag != 0):
            todoistSTR.append(_tempstr)
            _tempstr = ""
        _tempstr += ("- [ ] " + str(todoistDF.iat[i,0]) + "\n")
        for j in range(len(todoistDF.columns)):        
            if (j!=0) & ((todoistDF.isnull().iloc[i,j]) == False):
                # todoistSTR.append("\t" + str(todoistDF.iat[i,j]) + "\n")
                _tempstr += str("\t" + str(todoistDF.iat[i,j]) + "\n")
            else:
                continue
        if (flag == 0):
            todoistSTR.append(_tempstr)
            _tempstr = ""
            flag = 0
outputFile.writelines(todoistSTR)
outputFile.flush()