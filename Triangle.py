def classify_triangle(a: int, b: int, c: int) -> str:
    # 1. Kiểm tra ràng buộc dữ liệu đầu vào 
    if not (1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100):
        return "Invalid Input"
        
    # 2. Kiểm tra bất đẳng thức tam giác
    if not (a + b > c and a + c > b and b + c > a):
        return "Not a Triangle"
        
    # 3. Phân loại tam giác dựa trên logic nghiệp vụ
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# ==========================================
# BỘ KIỂM THỬ TỰ ĐỘNG (TEST SUITE SUITE RUNNER)
# ==========================================
test_cases = [
    {"id": "TC_01", "a": 0, "b": 50, "c": 50, "expected": "Invalid Input"},
    {"id": "TC_02", "a": 101, "b": 50, "c": 50, "expected": "Invalid Input"},
    {"id": "TC_03", "a": 50, "b": 0, "c": 50, "expected": "Invalid Input"},
    {"id": "TC_04", "a": 50, "b": 101, "c": 50, "expected": "Invalid Input"},
    {"id": "TC_05", "a": 50, "b": 50, "c": 0, "expected": "Invalid Input"},
    {"id": "TC_06", "a": 50, "b": 50, "c": 101, "expected": "Invalid Input"},
    {"id": "TC_07", "a": 10, "b": 20, "c": 50, "expected": "Not a Triangle"},
    {"id": "TC_08", "a": 1, "b": 2, "c": 3, "expected": "Not a Triangle"},
    {"id": "TC_09", "a": 50, "b": 50, "c": 50, "expected": "Equilateral"},
    {"id": "TC_10", "a": 100, "b": 100, "c": 100, "expected": "Equilateral"},
    {"id": "TC_11", "a": 50, "b": 50, "c": 40, "expected": "Isosceles"},
    {"id": "TC_12", "a": 40, "b": 50, "c": 50, "expected": "Isosceles"},
    {"id": "TC_13", "a": 50, "b": 40, "c": 50, "expected": "Isosceles"},
    {"id": "TC_14", "a": 3, "b": 4, "c": 5, "expected": "Scalene"},
    {"id": "TC_15", "a": 98, "b": 99, "c": 100, "expected": "Scalene"},
]

passed_count = 0
print(f"{'Test ID':<10}{'Input (a, b, c)':<20}{'Expected':<20}{'Actual':<20}{'Status':<10}")
print("-" * 80)

for tc in test_cases:
    actual = classify_triangle(tc["a"], tc["b"], tc["c"])
    status = "PASSED" if actual == tc["expected"] else "FAILED"
    if status == "PASSED":
        passed_count += 1
    print(f"{tc['id']:<10}{str((tc['a'], tc['b'], tc['c'])):<20}{tc['expected']:<20}{actual:<20}{status:<10}")

print("-" * 80)
print(f"KẾT QUẢ KIỂM THỬ: {passed_count}/{len(test_cases)} Test Cases PASSED.")
