from robot.api import ExecutionResult
from openpyxl import Workbook

# โหลดผลลัพธ์จาก output.xml
result = ExecutionResult('results/output.xml')

# สร้าง Excel ไฟล์
wb = Workbook()
ws = wb.active
ws.title = "Test Summary"
ws.append(["Test Case", "Status"])

# สร้าง Markdown table
md_lines = ["| Test Case | Status |", "|-----------|--------|"]

def collect_tests(suite):
    for test in suite.tests:
        status = "PASS" if test.passed else "FAIL"
        ws.append([test.name, status])
        md_lines.append(f"| {test.name} | {status} |")
    for sub in suite.suites:
        collect_tests(sub)

collect_tests(result.suite)

# เขียนผลลัพธ์เป็นไฟล์
wb.save("results/test_summary.xlsx")

with open("results/test_summary.txt", "w") as f:
    f.write("\n".join(md_lines))
