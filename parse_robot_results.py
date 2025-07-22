from robot.api import ExecutionResult
from openpyxl import Workbook

# โหลด output.xml
result = ExecutionResult('results/output.xml')

# เตรียม Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Test Summary"

# เขียน header
ws.append(["Test Case", "Status"])

# ฟังก์ชันดึง test cases จากทุก suite
def collect_tests(suite):
    for test in suite.tests:
        status = "PASS" if test.passed else "FAIL"
        ws.append([test.name, status])
    for sub in suite.suites:
        collect_tests(sub)

collect_tests(result.suite)

# บันทึกไฟล์ Excel
wb.save("results/test_summary.xlsx")
