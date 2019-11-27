import xlrd
import json
from Common.inter import InterTest


class ReadExcel(object):

    def __init__(self):
        self.number=1
        self.Is=InterTest()

    def Fileread(self,filePath):
        '''
        Read Excel
        '''
        FileObject = xlrd.open_workbook(filePath)
        sh = FileObject.sheet_by_name("Test")
        nr = sh.nrows
        for i in range(1,nr):
            getRow = sh.row_values(i)
            self.number += 2
            #self.number += 1

            if getRow[0] == "URL" or getRow[0] == "url":
                '''
                initialize URL
                '''
                self.url = getRow[2]
            else:
                '''     
                Data Transmission Json
                getRow[2]       information body
                getRow[3]       information assertion
                '''
                try:    #transition to Json
                    jsonData = json.loads(getRow[2])
                    result = json.loads(getRow[3])
                    jsonData["Sign"] = "9527"

                except json.decoder.JSONDecodeError:
                    print(f"json Format Error{self.number}")

                except Exception:
                    print(f"Unknow Error{self.number}")

                else:
                    # No exceptions will be executed
                    if getRow[0] == "assertion":
                        '''
                        Just Assertion
                        '''
                        self.Is.requestInterface(jsonData,result,getRow[0],self.url,getRow[6],self.number)

                    elif getRow[0] == "vericode":
                        '''
                        Get Verition Code
                        '''
                        vericode = input("Vericode: ")
                        jsonData["Body"]["code"] = vericode
                        self.bool=1
                        self.Is.requestInterface(jsonData,result,getRow[0],self.url,getRow[6],self.number)

                    else:
                        pass



if __name__ == "__main__":
    PATH="path"
    read=ReadExcel()
    read.Fileread(PATH)
