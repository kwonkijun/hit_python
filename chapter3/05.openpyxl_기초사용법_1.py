import openpyxl

# 새로운 엑셀 파일 생성
wb = openpyxl.Workbook()

# 현재 활성화된 시트 선택
ws = wb.active

# 시트 이름 변경
ws.title = "스타트코딩"

# 엑셀 저장
wb.save('chapter3/테스트.xlsx')