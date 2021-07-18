import serial #liberary for Serial communication
import time #liberary for using delay functions
import pyautogui#liberary for mouse and keyboard control
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    d = p.name.lower()
print(d)
if d=="com1":
   ArduinoSerial = serial.Serial('com1',9600)
if d=="com2":
   ArduinoSerial = serial.Serial('com2',9600)
if d=="com3":
   ArduinoSerial = serial.Serial('com3',9600)
if d=="com4":
   ArduinoSerial = serial.Serial('com4',9600)
if d=="com5":
   ArduinoSerial = serial.Serial('com5',9600)
if d=="com6":
   ArduinoSerial = serial.Serial('com6',9600)
if d=="com7":
   ArduinoSerial = serial.Serial('com7',9600)
if d=="com8":
   ArduinoSerial = serial.Serial('com8',9600)
if d=="com9":
   ArduinoSerial = serial.Serial('com9',9600)
if d=="com10":
   ArduinoSerial = serial.Serial('com10',9600)
if d=="com11":
   ArduinoSerial = serial.Serial('com11',9600)
if d=="com12":
   ArduinoSerial = serial.Serial('com12',9600)
if d=="com13":
   ArduinoSerial = serial.Serial('com13',9600)
if d=="com14":
   ArduinoSerial = serial.Serial('com14',9600)
if d=="com15":
   ArduinoSerial = serial.Serial('com15',9600)
if d=="com16":
   ArduinoSerial = serial.Serial('com16',9600)
if d=="com17":
   ArduinoSerial = serial.Serial('com17',9600)
if d=="com18":
   ArduinoSerial = serial.Serial('com18',9600)
if d=="com19":
   ArduinoSerial = serial.Serial('com19',9600)
if d=="com20":
   ArduinoSerial = serial.Serial('com20',9600)
if d=="com21":
   ArduinoSerial = serial.Serial('com21',9600)
if d=="com22":
   ArduinoSerial = serial.Serial('com22',9600)
if d=="com23":
   ArduinoSerial = serial.Serial('com23',9600)
if d=="com24":
   ArduinoSerial = serial.Serial('com24',9600)
if d=="com25":
   ArduinoSerial = serial.Serial('com25',9600)
if d=="com26":
   ArduinoSerial = serial.Serial('com26',9600)
if d=="com27":
   ArduinoSerial = serial.Serial('com27',9600)
if d=="com28":
   ArduinoSerial = serial.Serial('com28',9600)
if d=="com29":
   ArduinoSerial = serial.Serial('com29',9600)
if d=="com30":
   ArduinoSerial = serial.Serial('com30',9600)
if d=="com31":
   ArduinoSerial = serial.Serial('com31',9600)
if d=="com32":
   ArduinoSerial = serial.Serial('com32',9600)
if d=="com33":
   ArduinoSerial = serial.Serial('com33',9600)
if d=="com34":
   ArduinoSerial = serial.Serial('com34',9600)
if d=="com35":
   ArduinoSerial = serial.Serial('com35',9600)
if d=="com36":
   ArduinoSerial = serial.Serial('com36',9600)
if d=="com37":
   ArduinoSerial = serial.Serial('com37',9600)
if d=="com38":
   ArduinoSerial = serial.Serial('com38',9600)
if d=="com39":
   ArduinoSerial = serial.Serial('com39',9600)
if d=="com40":
   ArduinoSerial = serial.Serial('com40',9600)
if d=="com41":
   ArduinoSerial = serial.Serial('com41',9600)
if d=="com42":
   ArduinoSerial = serial.Serial('com42',9600)
if d=="com43":
   ArduinoSerial = serial.Serial('com43',9600)
if d=="com44":
   ArduinoSerial = serial.Serial('com44',9600)
if d=="com45":
   ArduinoSerial = serial.Serial('com45',9600)
if d=="com46":
   ArduinoSerial = serial.Serial('com46',9600)
if d=="com47":
   ArduinoSerial = serial.Serial('com47',9600)
if d=="com48":
   ArduinoSerial = serial.Serial('com48',9600)
if d=="com49":
   ArduinoSerial = serial.Serial('com49',9600)
if d=="com50":
   ArduinoSerial = serial.Serial('com50',9600)
if d=="com51":
   ArduinoSerial = serial.Serial('com51',9600)
if d=="com52":
   ArduinoSerial = serial.Serial('com52',9600)
if d=="com53":
   ArduinoSerial = serial.Serial('com53',9600)
if d=="com54":
   ArduinoSerial = serial.Serial('com54',9600)
if d=="com55":
   ArduinoSerial = serial.Serial('com55',9600)
if d=="com56":
   ArduinoSerial = serial.Serial('com56',9600)
if d=="com57":
   ArduinoSerial = serial.Serial('com57',9600)
if d=="com58":
   ArduinoSerial = serial.Serial('com58',9600)
if d=="com59":
   ArduinoSerial = serial.Serial('com59',9600)
if d=="com60":
   ArduinoSerial = serial.Serial('com60',9600)
if d=="com61":
   ArduinoSerial = serial.Serial('com61',9600)
if d=="com62":
   ArduinoSerial = serial.Serial('com62',9600)
if d=="com63":
   ArduinoSerial = serial.Serial('com63',9600)
if d=="com64":
   ArduinoSerial = serial.Serial('com64',9600)
if d=="com65":
   ArduinoSerial = serial.Serial('com65',9600)
if d=="com66":
   ArduinoSerial = serial.Serial('com66',9600)
if d=="com67":
   ArduinoSerial = serial.Serial('com67',9600)
if d=="com68":
   ArduinoSerial = serial.Serial('com68',9600)
if d=="com69":
   ArduinoSerial = serial.Serial('com69',9600)
if d=="com70":
   ArduinoSerial = serial.Serial('com70',9600)
if d=="com71":
   ArduinoSerial = serial.Serial('com71',9600)
if d=="com72":
   ArduinoSerial = serial.Serial('com72',9600)
if d=="com73":
   ArduinoSerial = serial.Serial('com73',9600)
if d=="com74":
   ArduinoSerial = serial.Serial('com74',9600)
if d=="com75":
   ArduinoSerial = serial.Serial('com75',9600)
if d=="com76":
   ArduinoSerial = serial.Serial('com76',9600)
if d=="com77":
   ArduinoSerial = serial.Serial('com77',9600)
if d=="com78":
   ArduinoSerial = serial.Serial('com78',9600)
if d=="com79":
   ArduinoSerial = serial.Serial('com79',9600)
if d=="com80":
   ArduinoSerial = serial.Serial('com80',9600)
if d=="com81":
   ArduinoSerial = serial.Serial('com81',9600)
if d=="com82":
   ArduinoSerial = serial.Serial('com82',9600)
if d=="com83":
   ArduinoSerial = serial.Serial('com83',9600)
if d=="com84":
   ArduinoSerial = serial.Serial('com84',9600)
if d=="com85":
   ArduinoSerial = serial.Serial('com85',9600)
if d=="com86":
   ArduinoSerial = serial.Serial('com86',9600)
if d=="com87":
   ArduinoSerial = serial.Serial('com87',9600)
if d=="com88":
   ArduinoSerial = serial.Serial('com88',9600)
if d=="com89":
   ArduinoSerial = serial.Serial('com89',9600)
if d=="com90":
   ArduinoSerial = serial.Serial('com90',9600)
if d=="com91":
   ArduinoSerial = serial.Serial('com91',9600)
if d=="com92":
   ArduinoSerial = serial.Serial('com92',9600)
if d=="com93":
   ArduinoSerial = serial.Serial('com93',9600)
if d=="com94":
   ArduinoSerial = serial.Serial('com94',9600)
if d=="com95":
   ArduinoSerial = serial.Serial('com95',9600)
if d=="com96":
   ArduinoSerial = serial.Serial('com96',9600)
if d=="com97":
   ArduinoSerial = serial.Serial('com97',9600)
if d=="com98":
   ArduinoSerial = serial.Serial('com98',9600)
if d=="com99":
   ArduinoSerial = serial.Serial('com99',9600)
if d=="com100":
   ArduinoSerial = serial.Serial('com100',9600)
if d=="com101":
   ArduinoSerial = serial.Serial('com101',9600)
if d=="com102":
   ArduinoSerial = serial.Serial('com102',9600)
if d=="com103":
   ArduinoSerial = serial.Serial('com103',9600)
if d=="com104":
   ArduinoSerial = serial.Serial('com104',9600)
if d=="com105":
   ArduinoSerial = serial.Serial('com105',9600)
if d=="com106":
   ArduinoSerial = serial.Serial('com106',9600)
if d=="com107":
   ArduinoSerial = serial.Serial('com107',9600)
if d=="com108":
   ArduinoSerial = serial.Serial('com108',9600)
if d=="com109":
   ArduinoSerial = serial.Serial('com109',9600)
if d=="com110":
   ArduinoSerial = serial.Serial('com110',9600)
if d=="com111":
   ArduinoSerial = serial.Serial('com111',9600)
if d=="com112":
   ArduinoSerial = serial.Serial('com112',9600)
if d=="com113":
   ArduinoSerial = serial.Serial('com113',9600)
if d=="com114":
   ArduinoSerial = serial.Serial('com114',9600)
if d=="com115":
   ArduinoSerial = serial.Serial('com115',9600)
if d=="com116":
   ArduinoSerial = serial.Serial('com116',9600)
if d=="com117":
   ArduinoSerial = serial.Serial('com117',9600)
if d=="com118":
   ArduinoSerial = serial.Serial('com118',9600)
if d=="com119":
   ArduinoSerial = serial.Serial('com119',9600)
if d=="com120":
   ArduinoSerial = serial.Serial('com120',9600)
if d=="com121":
   ArduinoSerial = serial.Serial('com121',9600)
if d=="com122":
   ArduinoSerial = serial.Serial('com122',9600)
if d=="com123":
   ArduinoSerial = serial.Serial('com123',9600)
if d=="com124":
   ArduinoSerial = serial.Serial('com124',9600)
if d=="com125":
   ArduinoSerial = serial.Serial('com125',9600)
if d=="com126":
   ArduinoSerial = serial.Serial('com126',9600)
if d=="com127":
   ArduinoSerial = serial.Serial('com127',9600)
if d=="com128":
   ArduinoSerial = serial.Serial('com128',9600)
if d=="com129":
   ArduinoSerial = serial.Serial('com129',9600)
if d=="com130":
   ArduinoSerial = serial.Serial('com130',9600)
if d=="com131":
   ArduinoSerial = serial.Serial('com131',9600)
if d=="com132":
   ArduinoSerial = serial.Serial('com132',9600)
if d=="com133":
   ArduinoSerial = serial.Serial('com133',9600)
if d=="com134":
   ArduinoSerial = serial.Serial('com134',9600)
if d=="com135":
   ArduinoSerial = serial.Serial('com135',9600)
if d=="com136":
   ArduinoSerial = serial.Serial('com136',9600)
if d=="com137":
   ArduinoSerial = serial.Serial('com137',9600)
if d=="com138":
   ArduinoSerial = serial.Serial('com138',9600)
if d=="com139":
   ArduinoSerial = serial.Serial('com139',9600)
if d=="com140":
   ArduinoSerial = serial.Serial('com140',9600)
if d=="com141":
   ArduinoSerial = serial.Serial('com141',9600)
if d=="com142":
   ArduinoSerial = serial.Serial('com142',9600)
if d=="com143":
   ArduinoSerial = serial.Serial('com143',9600)
if d=="com144":
   ArduinoSerial = serial.Serial('com144',9600)
if d=="com145":
   ArduinoSerial = serial.Serial('com145',9600)
if d=="com146":
   ArduinoSerial = serial.Serial('com146',9600)
if d=="com147":
   ArduinoSerial = serial.Serial('com147',9600)
if d=="com148":
   ArduinoSerial = serial.Serial('com148',9600)
if d=="com149":
   ArduinoSerial = serial.Serial('com149',9600)
if d=="com150":
   ArduinoSerial = serial.Serial('com150',9600)
if d=="com151":
   ArduinoSerial = serial.Serial('com151',9600)
if d=="com152":
   ArduinoSerial = serial.Serial('com152',9600)
if d=="com153":
   ArduinoSerial = serial.Serial('com153',9600)
if d=="com154":
   ArduinoSerial = serial.Serial('com154',9600)
if d=="com155":
   ArduinoSerial = serial.Serial('com155',9600)
if d=="com156":
   ArduinoSerial = serial.Serial('com156',9600)
if d=="com157":
   ArduinoSerial = serial.Serial('com157',9600)
if d=="com158":
   ArduinoSerial = serial.Serial('com158',9600)
if d=="com159":
   ArduinoSerial = serial.Serial('com159',9600)
if d=="com160":
   ArduinoSerial = serial.Serial('com160',9600)
if d=="com161":
   ArduinoSerial = serial.Serial('com161',9600)
if d=="com162":
   ArduinoSerial = serial.Serial('com162',9600)
if d=="com163":
   ArduinoSerial = serial.Serial('com163',9600)
if d=="com164":
   ArduinoSerial = serial.Serial('com164',9600)
if d=="com165":
   ArduinoSerial = serial.Serial('com165',9600)
if d=="com166":
   ArduinoSerial = serial.Serial('com166',9600)
if d=="com167":
   ArduinoSerial = serial.Serial('com167',9600)
if d=="com168":
   ArduinoSerial = serial.Serial('com168',9600)
if d=="com169":
   ArduinoSerial = serial.Serial('com169',9600)
if d=="com170":
   ArduinoSerial = serial.Serial('com170',9600)
if d=="com171":
   ArduinoSerial = serial.Serial('com171',9600)
if d=="com172":
   ArduinoSerial = serial.Serial('com172',9600)
if d=="com173":
   ArduinoSerial = serial.Serial('com173',9600)
if d=="com174":
   ArduinoSerial = serial.Serial('com174',9600)
if d=="com175":
   ArduinoSerial = serial.Serial('com175',9600)
if d=="com176":
   ArduinoSerial = serial.Serial('com176',9600)
if d=="com177":
   ArduinoSerial = serial.Serial('com177',9600)
if d=="com178":
   ArduinoSerial = serial.Serial('com178',9600)
if d=="com179":
   ArduinoSerial = serial.Serial('com179',9600)
if d=="com180":
   ArduinoSerial = serial.Serial('com180',9600)
if d=="com181":
   ArduinoSerial = serial.Serial('com181',9600)
if d=="com182":
   ArduinoSerial = serial.Serial('com182',9600)
if d=="com183":
   ArduinoSerial = serial.Serial('com183',9600)
if d=="com184":
   ArduinoSerial = serial.Serial('com184',9600)
if d=="com185":
   ArduinoSerial = serial.Serial('com185',9600)
if d=="com186":
   ArduinoSerial = serial.Serial('com186',9600)
if d=="com187":
   ArduinoSerial = serial.Serial('com187',9600)
if d=="com188":
   ArduinoSerial = serial.Serial('com188',9600)
if d=="com189":
   ArduinoSerial = serial.Serial('com189',9600)
if d=="com190":
   ArduinoSerial = serial.Serial('com190',9600)
if d=="com191":
   ArduinoSerial = serial.Serial('com191',9600)
if d=="com192":
   ArduinoSerial = serial.Serial('com192',9600)
if d=="com193":
   ArduinoSerial = serial.Serial('com193',9600)
if d=="com194":
   ArduinoSerial = serial.Serial('com194',9600)
if d=="com195":
   ArduinoSerial = serial.Serial('com195',9600)
if d=="com196":
   ArduinoSerial = serial.Serial('com196',9600)
if d=="com197":
   ArduinoSerial = serial.Serial('com197',9600)
if d=="com198":
   ArduinoSe9ial = serial.Serial('com198',9600)
if d=="com199":
   ArduinoSerial = serial.Serial('com199',9600)
if d=="com200":
   ArduinoSerial = serial.Serial('com200',9600)
if d=="com201":
   ArduinoSerial = serial.Serial('com201',9600)
if d=="com202":
   ArduinoSerial = serial.Serial('com202',9600)
if d=="com203":
   ArduinoSerial = serial.Serial('com203',9600)
if d=="com204":
   ArduinoSerial = serial.Serial('com204',9600)
if d=="com205":
   ArduinoSerial = serial.Serial('com205',9600)
if d=="com206":
   ArduinoSerial = serial.Serial('com206',9600)
if d=="com207":
   ArduinoSerial = serial.Serial('com207',9600)
if d=="com208":
   ArduinoSerial = serial.Serial('com208',9600)
if d=="com209":
   ArduinoSerial = serial.Serial('com209',9600)
if d=="com210":
   ArduinoSerial = serial.Serial('com210',9600)
if d=="com211":
   ArduinoSerial = serial.Serial('com211',9600)
if d=="com212":
   ArduinoSerial = serial.Serial('com212',9600)
if d=="com213":
   ArduinoSerial = serial.Serial('com213',9600)
if d=="com214":
   ArduinoSerial = serial.Serial('com214',9600)
if d=="com215":
   ArduinoSerial = serial.Serial('com215',9600)
if d=="com216":
   ArduinoSerial = serial.Serial('com216',9600)
if d=="com217":
   ArduinoSerial = serial.Serial('com217',9600)
if d=="com218":
   ArduinoSerial = serial.Serial('com218',9600)
if d=="com219":
   ArduinoSerial = serial.Serial('com219',9600)
if d=="com220":
   ArduinoSerial = serial.Serial('com220',9600)
if d=="com221":
   ArduinoSerial = serial.Serial('com221',9600)
if d=="com222":
   ArduinoSerial = serial.Serial('com222',9600)
if d=="com223":
   ArduinoSerial = serial.Serial('com223',9600)
if d=="com224":
   ArduinoSerial = serial.Serial('com224',9600)
if d=="com225":
   ArduinoSerial = serial.Serial('com225',9600)
if d=="com226":
   ArduinoSerial = serial.Serial('com226',9600)
if d=="com227":
   ArduinoSerial = serial.Serial('com227',9600)
if d=="com228":
   ArduinoSerial = serial.Serial('com228',9600)
if d=="com229":
   ArduinoSerial = serial.Serial('com229',9600)
if d=="com230":
   ArduinoSerial = serial.Serial('com230',9600)
if d=="com231":
   ArduinoSerial = serial.Serial('com231',9600)
if d=="com232":
   ArduinoSerial = serial.Serial('com232',9600)
if d=="com233":
   ArduinoSerial = serial.Serial('com233',9600)
if d=="com234":
   ArduinoSerial = serial.Serial('com234',9600)
if d=="com235":
   ArduinoSerial = serial.Serial('com235',9600)
if d=="com236":
   ArduinoSerial = serial.Serial('com236',9600)
if d=="com237":
   ArduinoSerial = serial.Serial('com237',9600)
if d=="com238":
   ArduinoSerial = serial.Serial('com238',9600)
if d=="com239":
   ArduinoSerial = serial.Serial('com239',9600)
if d=="com240":
   ArduinoSerial = serial.Serial('com240',9600)
if d=="com241":
   ArduinoSerial = serial.Serial('com241',9600)
if d=="com242":
   ArduinoSerial = serial.Serial('com242',9600)
if d=="com243":
   ArduinoSerial = serial.Serial('com243',9600)
if d=="com244":
   ArduinoSerial = serial.Serial('com244',9600)
if d=="com245":
   ArduinoSerial = serial.Serial('com245',9600)
if d=="com246":
   ArduinoSerial = serial.Serial('com246',9600)
if d=="com247":
   ArduinoSerial = serial.Serial('com247',9600)
if d=="com248":
   ArduinoSerial = serial.Serial('com248',9600)
if d=="com249":
   ArduinoSerial = serial.Serial('com249',9600)
if d=="com250":
   ArduinoSerial = serial.Serial('com250',9600)
if d=="com251":
   ArduinoSerial = serial.Serial('com251',9600)
if d=="com252":
   ArduinoSerial = serial.Serial('com252',9600)
if d=="com253":
   ArduinoSerial = serial.Serial('com253',9600)
if d=="com254":
   ArduinoSerial = serial.Serial('com254',9600)
if d=="com255":
   ArduinoSerial = serial.Serial('com255',9600)
if d=="com256":
   ArduinoSerial = serial.Serial('com256',9600)

time.sleep(2)#wait for 2 seconds for the communication to get established
while 1:
    incoming = (ArduinoSerial.readline())#read the serial data
    kachra = incoming.decode('utf-8')#decodes serial data
    bhalu=kachra.split()#splits data by spaces and makes them element of an array
    if len(bhalu) == 3:
       g = 2
       j = 15
    if len(bhalu) == 4:
       g = 3
       j = int(bhalu[1])
    if bhalu[0]=='left' and int(bhalu[g])>0:
       for i in range(1, j):
           pyautogui.move(-1, 0)
    if bhalu[0]=='right' and int(bhalu[g])>0:
       for t in range(1, j):
           pyautogui.move(1, 0)
    if bhalu[0]=='up' and int(bhalu[g])>0:
       for p in range(1, j):
           pyautogui.move(0, -1)
    if bhalu[0]=='down' and int(bhalu[g])>0:
       for f in range(1, j):
           pyautogui.move(0, 1)
    if bhalu[0]=='dclick' and int(bhalu[g])>0:
       pyautogui.doubleClick()
    if bhalu[0]=='hold' and int(bhalu[g])>0:
       pyautogui.move(0, 0)