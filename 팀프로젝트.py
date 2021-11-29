lList = ['독일어', '프랑스어', '러시아어']
print('현재 단어장에 있는 언어는 다음과 같습니다.')
print(lList)
print()
lan = input('어떤 언어로 검색하시겠습니까? ')
print()
vList = ['고양이', '강아지', '케이크', '사과', '컵', '의자', '건물', '숟가락', '기쁜', '슬픈']
print('현재 단어장에 있는 단어는 다음과 같습니다.')
print()

gList = {'고양이': 'Katze', '강아지': 'Welpe', '케이크': 'Kuchen', '사과': 'Äpfel', '컵': 'Becher',
         '의자': 'Stuhl', '건물': 'Gebäude', '기쁜': 'fröhlich', '슬픈': 'Traurig', '숟가락': 'Löffel'}
fList = {'고양이': 'chat', '강아지': 'chiot', '케이크': 'gâteau', '사과': 'pomme', '컵':'verre',
         '의자':'chaise', '건물':'bâtiment', '기쁜':'joie', '슬픈':'tristesse', '숟가락':'cuiller'}
rList = {'고양이': 'кот', '강아지': 'собака', '케이크': 'торт', '사과': 'яблоко', '컵': 'стакан',
         '의자': 'стул', '건물': 'здание', '기쁜': 'радость', '슬픈': 'грусть', '숟가락': 'ложка'}

if lan == '독일어':
    mylan = input(str(list(gList.keys())) + '중 검색할 단어는? ')
    print()
    print('검색하신 %s의 %s 단어는 %s입니다.' % (mylan, lan, gList[mylan]))
    import time
    time.sleep(1)
elif lan == '프랑스어':
    mylan = input(str(list(fList.keys())) + '중 검색할 단어는? ')
    print()
    print('검색하신 %s의 %s 단어는 %s입니다.' % (mylan, lan, fList[mylan]))
    import time
    time.sleep(1)
else:
    mylan = input(str(list(rList.keys())) + '중 검색할 단어는? ')
    print()
    print('검색하신 %s의 %s 단어는 %s입니다.' % (mylan, lan, rList[mylan]))
    import time
    time.sleep(1)
print()

while True:
    thing2 = str(input('나만의 단어장을 추가적으로 이용하실 경우 Y, 아닐 경우 N을 입력해주세요. ' ))
    print()
    thing3 = 'Y'
    if thing2 == 'Y':
        print('그럼 이용하실 서비스를 선택해주세요.')
        service = ['단어 재검색', '새 단어 등록', '퀴즈 풀어보기']
        print(service)
    else:
        print('감사합니다.프로그램을 종료해주세요.')
        break

    answer = str(input())
    print()

    if answer == '단어 재검색':
        lan = input('어떤 언어로 검색하시겠습니까? ')
        print()
        vList = ['고양이', '강아지', '케이크', '사과', '컵', '의자', '건물', '숟가락', '기쁜', '슬픈']
        print('현재 단어장에 있는 단어는 다음과 같습니다.')
        print()

        gList = {'고양이': 'Katze', '강아지': 'Welpe', '케이크': 'Kuchen', '사과': 'Äpfel', '컵': 'Becher',
                 '의자': 'Stuhl', '건물': 'Gebäude', '기쁜': 'fröhlich', '슬픈': 'Traurig', '숟가락': 'Löffel'}
        fList = {'고양이': 'chat', '강아지': 'chiot', '케이크': 'gâteau', '사과': 'pomme', '컵':'verre',
                 '의자':'chaise', '건물':'bâtiment', '기쁜':'joie', '슬픈':'tristesse', '숟가락':'cuiller'}
        rList = {'고양이': 'кот', '강아지': 'собака', '케이크': 'торт', '사과': 'яблоко', '컵': 'стакан',
                 '의자': 'стул', '건물': 'здание', '기쁜': 'радость', '슬픈': 'грусть', '숟가락': 'ложка'}

        if lan == '독일어':
            mylan = input(str(list(gList.keys())) + '중 검색할 단어는? ')
            print()
            print('검색하신 %s의 %s 단어는 %s입니다.' % (mylan, lan, gList[mylan]))
        elif lan == '프랑스어':
            mylan = input(str(list(fList.keys())) + '중 검색할 단어는? ')
            print()
            print('검색하신 %s의 %s 단어는 %s입니다.' % (mylan, lan, fList[mylan]))
        else:
            mylan = input(str(list(rList.keys())) + '중 검색할 단어는? ')
            print()
            print('검색하신 %s의 %s 단어는 %s입니다.' % (mylan, lan, rList[mylan]))
        print()
    
    elif answer == '새 단어 등록':
        gList = {'고양이': 'Katze', '강아지': 'Welpe', '케이크': 'Kuchen', '사과': 'Äpfel', '컵': 'Becher',
                 '의자': 'Stuhl', '건물': 'Gebäude', '기쁜': 'fröhlich', '슬픈': 'Traurig', '숟가락': 'Löffel'}
        fList = {'고양이': 'chat', '강아지': 'chiot', '케이크': 'gâteau', '사과': 'pomme', '컵':'verre',
                 '의자':'chaise', '건물':'bâtiment', '기쁜':'joie', '슬픈':'tristesse', '숟가락':'cuiller'}
        rList = {'고양이': 'кот', '강아지': 'собака', '케이크': 'торт', '사과': 'яблоко', '컵': 'стакан',
                 '의자': 'стул', '건물': 'здание', '기쁜': 'радость', '슬픈': 'грусть', '숟가락': 'ложка'}
        lan = input('어느 언어 단어장에 등록하시겠습니까? ' )
        print()
        if lan == '독일어':
             mean = str(input('등록하실 단어의 뜻을 입력해주세요. '))
             word = str(input('등록하실 단어를 입력해주세요. '))
             print()
             print('등록되었습니다.')
             gList[mean] = word
             print(gList)

        elif lan == '프랑스어':
            mean = str(input('등록하실 단어의 뜻을 입력해주세요. '))
            word = str(input('등록하실 단어를 입력해주세요. '))
            print()
            print('등록되었습니다.')
            fList[mean] = word
            print(fList)
        else:
            mean = str(input('등록하실 단어의 뜻을 입력해주세요. '))
            word = str(input('등록하실 단어를 입력해주세요. '))
            print()
            print('등록되었습니다.')
            rList[mean] = word
            print(rList)
        print()
    else:
        lList = ['독일어', '프랑스어', '러시아어']
        lan = input('퀴즈는 단어장에 있는 언어로만 출제됩니다. 어떤 언어의 퀴즈를 푸시겠습니까? ')
        print()

        if lan == '독일어':
            import random
            import time
            answer = 0
            wrong = 0
            gList = {'Löffel':'숟가락','fröhlich': '기쁜','Äpfel': '사과','Welpe': '강아지','Stuhl': '의자'}
            print('문제는 총 5문제 출제됩니다. 그럼 시작하겠습니다. ')
            time.sleep(2)
            print()
            for i in gList:
                user_value = input(f"{i}의 뜻을 입력하시오 :")
                
                if user_value == gList[i]:
                    print("정답입니다.")
                    answer = answer+1
                    print()
                    time.sleep(1)
                else:
                    print("찾을 수 없는 단어 또는 틀린 단어입니다.")
                    wrong = wrong+1
                    print()
                    time.sleep(1)
            print('맞춘 갯수는 %d개이고 틀린 갯수는 %d개 입니다.' % (answer,wrong))
            time.sleep(1)
            print()

        elif lan == '프랑스어':
            import random
            import time
            answer = 0
            wrong = 0
            fList = {'gâteau':'케이크', 'verre':'컵', 'bâtiment':'건물', 'tristesse':'슬픈','chat':'고양이'}
            print('문제는 총 5문제 출제됩니다. 그럼 시작하겠습니다. ')
            time.sleep(2)
            print()
            for i in fList:
                user_value = input(f"{i}의 뜻을 입력하시오 :")
                
                if user_value == fList[i]:
                    print("정답입니다.")
                    answer = answer+1
                    print()
                    time.sleep(1)
                else:
                    print("찾을 수 없는 단어 또는 틀린 단어입니다.")
                    wrong = wrong+1
                    print()
                    time.sleep(1)
            print('맞춘 갯수는 %d개이고 틀린 갯수는 %d개 입니다.' % (answer,wrong))
            time.sleep(1)
            print()

        else:
            import random
            import time
            answer = 0
            wrong = 0
            rList = {'стул':'의자', 'радость':'기쁜', 'ложка': '숟가락', 'стакан': '컵', 'торт': '케이크'}
            print('문제는 총 5문제 출제됩니다. 그럼 시작하겠습니다. ')
            time.sleep(2)
            print()
            for i in rList:
                user_value = input(f"{i}의 뜻을 입력하시오 :")
                
                if user_value == rList[i]:
                    print("정답입니다.")
                    answer = answer+1
                    print()
                    time.sleep(1)
                else:
                    print("찾을 수 없는 단어 또는 틀린 단어입니다.")
                    wrong = wrong+1
                    print()
                    time.sleep(1)
            print('맞춘 갯수는 %d개이고 틀린 갯수는 %d개 입니다.' % (answer,wrong))
            time.sleep(1)
            print()









































































                
                
