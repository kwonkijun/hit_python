import openpyxl
import random

# 새로운 엑셀 파일 생성
wb = openpyxl.Workbook()

# 현재 활성화된 시트 선택
ws = wb.active

# 시트 이름 변경
ws.title = "data"

# 헤더 추가
ws.append(['순번', '제품명', '가격', '수량', '합계'])

# 데이터 추가
name_list = ['기계식 키보드', '게이밍 마우스', 
'32인치 모니터', '마우스 패드']

for i in range(1,random.randint(5,11)):
    name = random.choice(name_list)
    if name == "기계식 키보드":
        price = 120000
    elif name == "게이밍 마우스":
        price = 40000
    elif name == "32인치 모니터":
        price = 350000
    elif name == "마우스 패드":
        price = 20000
    ws.append([i, name, price, random.randint(1, 5), f'=C{i+1}*D{i+1}'])


# 엑셀 저장
wb.save('chapter3/11번가.xlsx')