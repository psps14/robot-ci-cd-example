from robot.api import ExecutionResult

# โหลดผลลัพธ์จาก output.xml
result = ExecutionResult('results/output.xml')

# เตรียมตารางรายงาน
lines = ["| Test Case | Status |", "|-----------|--------|"]

# ลูปผ่านเทสเคสทั้งหมด
for test in result.suite.tests:
    status = "PASS" if test.passed else "FAIL"
    lines.append(f"| {test.name} | {status} |")

# บันทึกไฟล์รายงาน
with open("results/test_summary.txt", "w") as f:
    f.write("\n".join(lines))
