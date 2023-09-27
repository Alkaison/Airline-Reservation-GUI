import re, json, sqlite3

class UserWallet():
    def textvalidator(self, type, objs):
        numreg = '[^0-9]'
        match type:
            case 'amount':
                objs[0].text = re.sub(numreg, '', objs[0].text)
                if objs[0].text.strip() == '':
                    objs[1].disabled = True
                elif re.sub('\D', '', objs[0].text.strip()) == '0':
                    objs[0].text = ''
                    objs[1].disabled = True
                elif int(objs[0].text.strip()) > 100000 :
                    objs[0].text = objs[0].text.strip()[0:-1]
                else:
                    objs[1].disabled = False
            case 'pin':
                objs[0].text = re.sub(numreg, '', objs[0].text)
                if objs[0].text.strip() == '':
                    objs[1].disabled = True
                elif len(objs[0].text.strip()) < 6 :
                    objs[1].disabled = True
                elif len(objs[0].text.strip()) == 6 :
                    objs[1].disabled = False
                elif len(objs[0].text.strip()) > 6 :
                    objs[0].text = objs[0].text.strip()[0:-1]
                    
                    

