import json
import requests

class InterTest(object):
    
    def __init__(self):
        '''
        Def  header
        '''
        self.header={"Content-Type":"application/json"}

    def requestInterface(self,*kwargs):
        ''' receive rowtuple
         kwargs[0]          data/Body
         kwargs[1]          result
         kwargs[2]          vericode
         kwargs[3]          url
         kwargs[4]          TestModel
         kwargs[5]          number
        '''
        try:
            re = requests.post(url=kwargs[3], headers=self.header, json=kwargs[0])
            re = json.loads(re.text)
        except Exception:
            print(f"{kwargs[4]}\t\tRequest Invalid\t{kwargs[5]}")
        else:
            if kwargs[2] == "vericode":
                self.header["AuthToken"]=re["body"]["token"]  #Get token and add to header
                #print(f"vericode={re['body']['token']}")

            try:
                if re["errCode"] == kwargs[1]["errCode"] and re["errMsg"] == kwargs[1]["errMsg"]:
                    re=str(re)
                    re = re.replace("{","{\n\t")
                    re = re.replace(",",",\n\t")
                    re = re.replace("}","\n\t}\n")
                    print(f"{kwargs[4]},\n\t{re}")
                    #print(f"{kwargs[4]}\n\tsuccess:{kwargs[5]}")
                else:
                    print(f"Request:\tURL={kwargs[3]},\n\t headers={self.header}, \n\t Body={kwargs[0]}\n")
                    print(f"Return:{re}\n")
                    print(f"{kwargs[4]}\t\tfalse:{kwargs[5]}\t{re['errMsg']}")

            except KeyError:
                print(f"KeyError re={re}")
            except Exception:
                print(f"Param Error\t\t{kwargs[5]}")
                print(re["errCode"],re["errMsg"])



if __name__ == "__main__":
    path="File/interface.xlsx"
    intertest=InterTest()
    intertest.requestInterface(path)
