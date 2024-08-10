import pyautogui
import pyperclip
import time
import os

# 안내
print('Manga Auto Downloader (Ver. 1.1)    제작: YCLK')
time.sleep(3)

# 저장 안내
answer = input("저장한 설정 값을 불러오시겠습니까? (Y/N):")

if answer == "N" or "n" : 
    # 스크롤바 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 스크롤 바 최상단에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    ScrollTopX, ScrollTopY = pyautogui.position()
    os.system('cls')

    # 스크롤바 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 스크롤 바 하단에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    ScrollBottomX, ScrollBottomY = pyautogui.position()
    os.system('cls')

    # 확장 프로그램 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 Image Downloader 확장 프로그램에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    ExtentionX, ExtentionY = pyautogui.position()
    os.system('cls')

    # Select all 체크박스 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 Select all 체크박스에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    SelectX, SelectY = pyautogui.position()
    os.system('cls')

    # 폴더 이름 지정 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 Save to subfolder 란에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    FolderX, FolderY = pyautogui.position()
    os.system('cls')

    # 다운로드 버튼 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 Download 버튼 위에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    DownloadX, DownloadY = pyautogui.position()
    os.system('cls')

    # 다음화 버튼 좌표 입력
    time_cnt = 5

    while time_cnt:
        print(str(time_cnt) + '초 후에 플랫폼 다음화 버튼 위에 마우스를 위치하세요')
        time_cnt -= 1
        time.sleep(1)

    NextX, NextY = pyautogui.position()
    os.system('cls')

    # 이미지 로드 시간 입력
    delayLoadTime = int(input('이미지 로드 대기 시간을 지정해 주세요 (사진이 많을 수록 길게 지정, 10초 권장): '))

    # 다운로드 대기 시간 입력
    delayDownloadTime = int(input('이미지 다운로드 대기 시간을 지정해 주세요 (사진이 많을 수록 길게 지정, 20초 권장): '))
else : 
    loaded_variables = {}
    with open("variables.txt", "r") as file:
        for line in file:
            key, value = line.strip().split('=')
            # 문자열을 정수로 변환하거나 그대로 두기 (예제에서는 정수만)
            if value.isdigit():
                value = int(value)
            loaded_variables[key] = value

# 만화 제목 입력
mangaTitle = input('저장할 작품의 이름을 지정해 주세요: ')

# 시작하는 화 입력
chapterNumber = int(input('시작하는 화를 지정해 주세요: '))

#끝나는 화 입력
finishChapter = int(input('끝나는 화를 지정해 주세요: '))
os.system('cls')

# 다운로드 시간 표시
time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 다운로드가 시작됩니다')
    time_cnt -= 1
    time.sleep(1)
os.system('cls')

# num변수 선언
num = 0

while num < finishChapter:
    num += 1

    pyautogui.moveTo(ScrollTopX, ScrollTopY, duration=0.3)
    pyautogui.dragTo(ScrollBottomX, ScrollBottomY, duration=5)

    # 확장 프로그램 클릭
    pyautogui.moveTo(ExtentionX, ExtentionY, duration=0.3)
    pyautogui.click()

    time_cnt = delayLoadTime

    while time_cnt:
        print('로드가 완료될 때까지 ' + str(time_cnt) + '초를 기다립니다')
        time_cnt -= 1
        time.sleep(1)
    os.system('cls')

    # height를 110이상으로
    # pyautogui.moveTo(286, 164, duration=0.3)
    # pyautogui.click()
    # pyautogui.press('right', presses=11)
    
    # select all 선택
    pyautogui.moveTo(SelectX, SelectY, duration=0.3)
    pyautogui.click()

    # 폴더 입력 선택
    pyautogui.moveTo(FolderX, FolderY, duration=0.3)
    pyautogui.click()
    
    # 폴더 입력 지우기
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    # 저장 폴더 제목 입력
    pyperclip.copy(mangaTitle)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write('-')
    pyautogui.write(str(chapterNumber))
    chapterNumber += 1
    pyperclip.copy('화')
    pyautogui.hotkey('ctrl', 'v')

    # 다운로드 클릭
    pyautogui.moveTo(DownloadX, DownloadY, duration=0.3)
    pyautogui.click()

    # 확장 프로그램 종료
    pyautogui.moveTo(ExtentionX, ExtentionY, duration=0.3)
    pyautogui.click()

    time_cnt = delayDownloadTime

    while time_cnt:
        print('다운로드가 완료될 때까지 ' + str(time_cnt) + '초를 기다립니다')
        time_cnt -= 1
        time.sleep(1)
    os.system('cls')

    # 다음화 클릭
    pyautogui.moveTo(NextX, NextY, duration=0.3)
    pyautogui.click()