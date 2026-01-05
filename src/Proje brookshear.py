
kod=[]
#geçerli olan haneler
Harf=['A', 'B', 'C' , 'D' , 'E' , 'F', '0' , '1' , '2' , '3' , '4' , '5', '6' , '7' , '8' , '9']


while True:
    #alınan kod büyük harfa çeviriyor
    kod=input("4 haneli bir HEX kodu giriniz:").upper()

    #hataları kontrol eder
    #uzunluğunu kontrol eder
    if len(kod)>4:
        print("Fazla hane girdiniz!") 
        
    elif len(kod)<4:
        print("Eksik hane girdiniz!")
        
    #harf ve sayıdan başka hane girilip girilmediğini kontrol eder
    elif any(not element.isalnum() for element in kod):
        print("Harf ve sayidan baska eleman girdiniz!")
        
    #geğerli harflerden başka harf girilip girilmediğini kontrol eder
    elif any(element not in Harf for element in kod):
        print("Yanlis harf girdiniz!(Sadece A-F girilebilir)")
    
    #opcode alıp uygun açıklama seçip ekrana yazılıyor
    else:
       match kod[0]:
            case '1':
                Adres=kod[2]+kod[3]
                Register=kod[1]
                print(Adres , "adresindeki bellek hücresinin icerigini,",Register,"numarali kaydediciye(Register) yukle.") 
                break
            case '2':
                Adres=kod[2]+kod[3]
                Register=kod[1]
                print(Adres,"degerini", Register ,"numarali kaydediciye(Register) yukle") 
                break
            case '3':
                Adres=kod[2]+kod[3]
                Register=kod[1]
                print(Register,"numarali register iceriginin belleğin ",Adres," adresine yukle.") 
                break
            case '4':
                if kod[1]!='0':
                    print("Yanlis kod yazdiniz!(Opcode 4 ise takip edecek hane 0 olmalidir)")
                    
                else:
                    Register1=kod[2]
                    Register2=kod[3]
                    print( Register1 ," registerinin iceriginin register ",Register2,"'e kopyala.")
                    break
            case '5':
                Register=kod[1]
                Register1=kod[2]
                Register2=kod[3]
                print(Register1," ve ",Register2," numarali registerlerdeki ikili sayilari topla ve sonucun ",Register," numarali registera yükle.")
                break
            case '6':
                Register=kod[1]
                Register1=kod[2]
                Register2=kod[3]
                print(Register1," numarali register ve ",Register2," registerindeki degerlerin kayan-nokta degerleri olarak toplan ve sonucun ",Register," numarali registera yukle.")
                break
            case '7':
                Register=kod[1]
                Register1=kod[2]
                Register2=kod[3]
                print("Register ",Register1," ve ",Register2," deki icerigin OR islemine al ve sonucu ",Register," numarali registera yukle.")
                break
            case '8':
                Register=kod[1]
                Register1=kod[2]
                Register2=kod[3]
                print("Register ",Register1," ve ",Register2," deki icerigin AND islemine al ve sonucu ",Register," numarali registera yükle.")
                break
            case '9':
                Register=kod[1]
                Register1=kod[2]
                Register2=kod[3]
                print("Register ",Register1," ve ",Register2," deki icerigin XOR islemine al ve sonucu ",Register," numarali registera yükle.")
                break
            case 'A':
                if kod[2]!='0':
                    print("Yanlis kod yazdiniz!(Opcode A ise ucuncu hane 0 olmalidir)")
                    
                else:
                    Register=kod[1]
                    Kaydiri=kod[3]
                    print(Register," numarali registerin icerigini dongusel biçimde ", Kaydiri," bit saga kaydir.")
                    break
            case 'B':
                Adres=kod[2]+kod[3]
                Register=kod[1]
                print(Register," numarali register ile 0 numarali regiterdeki içerikleri kariştirin. Eşit ise, ",Adres," deseni program sayacina yukle.")
                break
            case 'C':
                if kod[1]!='0' or kod[2]!='0' or kod[3]!='0':
                    print("Yanlis kod yazdiniz!(Opcode C ise tum sonraki haneler 0 olmalidir.)")
                    
                else:
                    print("Yurutmeyi durdur.")
                    break
                
                

      


