# -*- coding: utf-8 -*-
class PylsyTable:
    def __init__(self,attributes):
        self.Attributes=attributes
        self.Table=[]
        self.AttributesLength=[]
        self.Colsnum=len(self.Attributes)
        self.Linesnum=0
        for attribute in self.Attributes:
            row=dict()
            row[attribute]=""
            self.Table.append(row)
    def PrintDivide(self):
        for space in self.AttributesLength:
            print "+",
            for sign in range(space):
                print "-",
        print "+"
    def AddData(self,attribute,values):
        for row in self.Table:
            dictvalues=[]
            if row.has_key(attribute):
                for index in range(len(values)):
                    if type(values[index])!=str:
                        dictvalues.append(str(values[index]))
                    else:
                        dictvalues.append(values[index])
                row[attribute]=dictvalues
    def CreateTable(self):
        for row in self.Table:
            values=row.values()[0]
            if self.Linesnum<len(values):
                self.Linesnum=len(values)
            # find the length of longest word in current column
            Len = len(max(row.keys()+row.values()[0], key=len))
            self.AttributesLength.append(Len)
        self.PrintHead()
        self.PrintValue()
    def PrintHead(self):
        self.PrintDivide()
        print "|",
        for spaces,attr in zip(self.AttributesLength,self.Attributes):
            spacenum=spaces*2-1
            start=(spacenum-len(attr))/2
            for space in range(start):
                print "",
            print attr,
            end=spacenum-start-len(attr)
            for space in range(end):
                print "",
            print "|",
        print ""
        self.PrintDivide()
    def PrintValue(self):
        for line in range(self.Linesnum):
            for row,length in zip(self.Table,self.AttributesLength):
                print "|",
                valuelength=length*2-1
                value=row.values()[0]
                if len(value)!=0:
                    start=(valuelength-len(value[line]))/2
                    for space in range(start):
                        print "",
                    print value[line],
                    end=valuelength-start-len(value[line])
                    for space in range(end):
                        print "",
                else:
                    start=0
                    end=valuelength-start+1
                    for sapce in range(end):
                        print "",
            print "|"
            self.PrintDivide()
