import time,random,sys,os,io,numpy,math
varName = []
varCont = []
constName = []
constCont = []
lsts = []
line = 0
f = open ("ky3.kyt3",'r')
log = open ("ky3Log.kyc","w")
log.write ("")
log.close()
log = open ("ky3Log.kyc","a")
a = f.read()
ad = a.split ("\n")
il = ad[line].split (" ")
br = True
while br:
    if il[0] == "var":
        if '"'  not in il[3]:
            global math
            math = True
        if "[" in il[3]:
            lits = True
        else:
            global strn
            strn = True
        if math == True:
            num1 = int(il[3])
            num2 = int(il[5])
            operationToDo = il[4]
            fnl = 0
            if operationToDo == "+":
                fnl = num1 + num2
            elif operationToDo == "-":
                fnl = num1 - num2
            elif operationToDo == "*":
                fnl = num1 * num2
            elif operationToDo == "/":
                fnl = num1 / num2
            else:
                mathError1 = "Error on line:" + str(line + 1) + " Invalid math operation given"
                log.write (mathError1)
        varCont.append(fnl)
        if math != True:
            if il[3] in varName:
                varToReplace = varName.index (il[3])
                varCont.append(varCont[varToReplace])
                varName.append(il[1])
            elif il[3] not in varName and strn == True and lits != True:
                rmvQuo = il[3].split ('"')
                rmvdQuo = rmvQuo[1]
                varName.append (il[1])
                varCont.append(rmvdQuo)

            elif il[3] not in varName and strn == False and lits == True:
                varName.append(il[1])
                rmvBracket = il[3].split("[")
                rmvBracket2 = rmvBracket[1].split("]")
                listIndexPrint = lsts.index(rmvBracket[0])
                listFoundIndexPrint = lsts[listIndexPrint + 1].index (rmvBracket[0])
                varCont.append (lsts[listIndexPrint + 1][listFoundIndexPrint])
            else:
                varCreateListContentError = "Error on line:" + (line + 1) + "Inde"
