from robot.api import ExecutionResult

# โหลดผลลัพธ์
result = ExecutionResult('results/output.xml')

# เตรียมตารางรายงาน
lines = ["| Test Case                   | Status |", "|--------------------------------|--------|"]

# ฟังก์ชันวนซ้ำเพื่ออ่านทุก test case จากทุก suite ย่อย
def collect_tests(suite):
    for test in suite.tests:
        status = "PASS" if test.passed else "FAIL"
        lines.append(f"| {test.name} | {status} |")
    for sub in suite.suites:
        collect_tests(sub)

# เริ่มจาก root suite
collect_tests(result.suite)

# เขียนไฟล์
with open("results/test_summary.txt", "w") as f:
    f.write("\n".join(lines))
