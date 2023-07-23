import pyautogui
import pyperclip
import time
import os

# 안내
print('Manga Auto Downloader (Ver. 1.1)    제작: YCLK')
time.sleep(3)

# 확장 프로그램 좌표 입력
time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 Image Downloader 확장 프로그램에 마우스를 위치하세요')
    time_cnt -= 1
    time.sleep(1)

print(pyautogui.position())

ExtentionX = int(input('x좌표를 입력해 주세요: '))
ExtentionY = int(input('y좌표를 입력해 주세요: '))
os.system('cls')

# Select all 체크박스 좌표 입력
time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 Select all 체크박스에 마우스를 위치하세요')
    time_cnt -= 1
    time.sleep(1)

print(pyautogui.position())

SelectX = int(input('x좌표를 입력해 주세요: '))
SelectY = int(input('y좌표를 입력해 주세요: '))
os.system('cls')

# 폴더 이름 지정 좌표 입력
time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 Save to subfolder 란에 마우스를 위치하세요')
    time_cnt -= 1
    time.sleep(1)

print(pyautogui.position())

FolderX = int(input('x좌표를 입력해 주세요: '))
FolderY = int(input('y좌표를 입력해 주세요: '))
os.system('cls')

# 다운로드 버튼 좌표 입력
time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 Download 버튼 위에 마우스를 위치하세요')
    time_cnt -= 1
    time.sleep(1)

print(pyautogui.position())

DownloadX = int(input('x좌표를 입력해 주세요: '))
DownloadY = int(input('y좌표를 입력해 주세요: '))
os.system('cls')

# 다음화 버튼 좌표 입력
time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 플랫폼 다음화 버튼 위에 마우스를 위치하세요')
    time_cnt -= 1
    time.sleep(1)

print(pyautogui.position())

NextX = int(input('x좌표를 입력해 주세요: '))
NextY = int(input('y좌표를 입력해 주세요: '))
os.system('cls')

# 만화 제목 입력
mangaTitle = input('저장할 작품의 이름을 지정해 주세요: ')

# 이미지 로드 시간 입력
delayLoadTime = int(input('이미지 로드 대기 시간을 지정해 주세요 (사진이 많을 수록 길게 지정 10초 정도): '))

# 다운로드 대기 시간 입력
delayDownloadTime = int(input('이미지 다운로드 대기 시간을 지정해 주세요 (사진이 많을 수록 길게 지정 20초 정도): '))

# 시작하는 화 입력
numb = int(input('시작하는 화를 지정해 주세요: '))

#끝나는 화 입력
num1 = int(input('끝나는 화를 지정해 주세요: '))
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

while num < num1:
    num += 1

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
    pyautogui.write(str(numb))
    numb += 1
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
