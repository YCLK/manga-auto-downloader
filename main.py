import pyautogui
import pyperclip
import time

mangaTitle = input('저장할 작품의 이름을 지정해 주세요: ')
numb = int(input('시작하는 화를 지정해 주세요: '))
num = 0
num1 = int(input('반복할 횟수를 지정해 주세요: '))
time.sleep(10)

while num < num1:
    num += 1

    # 확장 프로그램 클릭
    pyautogui.moveTo(1545, 51, duration=0.3)
    pyautogui.click()

    time.sleep(3)

    # height를 110이상으로
    # pyautogui.moveTo(286, 164, duration=0.3)
    # pyautogui.click()
    # pyautogui.press('right', presses=11)
    
    # select all 선택
    pyautogui.moveTo(1161, 218, duration=0.3)
    pyautogui.click()

    # 폴더 입력 선택
    pyautogui.moveTo(1233, 637, duration=0.3)
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
    pyautogui.moveTo(1523, 634, duration=0.3)
    pyautogui.click()

    # 확장 프로그램 종료
    pyautogui.moveTo(1683, 585, duration=0.3)
    pyautogui.click()

    time.sleep(10)

    # 다음화 클릭
    pyautogui.moveTo(1375, 948, duration=0.3)
    pyautogui.click()