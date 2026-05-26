def evaluate_loan(age: int, income: float, credit_score: int, employment: str) -> str:
    # 1. Kiểm tra ràng buộc dữ liệu đầu vào (Rule 1 - C0)
    if not (18 <= age <= 65):
        return "Invalid Input"
    if not (5.0 <= income <= 500.0):
        return "Invalid Input"
    if not (300 <= credit_score <= 850):
        return "Invalid Input"
    if employment not in ["C", "F"]:
        return "Invalid Input"

    # 2. Nhóm High Risk (Rule 2 - C1)
    if 300 <= credit_score <= 500:
        return "REJECT"
        
    # Xác định biến phụ Medium Risk (C2) để rẽ nhánh dưới
    is_medium_risk = (501 <= credit_score <= 700)
    
    # 3. Xử lý Logic nghiệp vụ dựa trên Thu nhập (C3) và Việc làm (C4)
    if income < 15.0:
        if is_medium_risk:
            return "REJECT"           # Rule 3
        else: # Nhóm Low Risk
            if employment == "F":
                return "REJECT"       # Rule 4
            else:
                return "MANUAL REVIEW" # Rule 5
    else: 
        # Nhóm Thu nhập >= 15.0 (Áp dụng cho cả Low và Medium Risk)
        if employment == "C":
            return "APPROVE"          # Rule 6
        else:
            return "MANUAL REVIEW"     # Rule 7

# ==========================================
# BỘ KIỂM THỬ TỰ ĐỘNG (TEST SUITE RUNNER)
# ==========================================
test_cases = [
    # Nhóm 1: Kiểm tra ngoại lệ (Invalid Inputs)
    {"id": "TC_01", "age": 17, "income": 20.0, "score": 600, "emp": "C", "expected": "Invalid Input"},
    {"id": "TC_02", "age": 66, "income": 20.0, "score": 600, "emp": "C", "expected": "Invalid Input"},
    {"id": "TC_03", "age": 30, "income": 4.9,  "score": 600, "emp": "C", "expected": "Invalid Input"},
    {"id": "TC_04", "age": 30, "income": 500.1,"score": 600, "emp": "C", "expected": "Invalid Input"},
    {"id": "TC_05", "age": 30, "income": 20.0, "score": 299, "emp": "C", "expected": "Invalid Input"},
    {"id": "TC_06", "age": 30, "income": 20.0, "score": 851, "emp": "C", "expected": "Invalid Input"},
    {"id": "TC_07", "age": 30, "income": 20.0, "score": 600, "emp": "A", "expected": "Invalid Input"},
    
    # Nhóm 2: Kiểm tra logic nghiệp vụ (Decision Table)
    {"id": "TC_08", "age": 18, "income": 5.0,  "score": 300, "emp": "C", "expected": "REJECT"},
    {"id": "TC_09", "age": 30, "income": 500.0,"score": 500, "emp": "F", "expected": "REJECT"},
    {"id": "TC_10", "age": 30, "income": 14.9, "score": 501, "emp": "C", "expected": "REJECT"},
    {"id": "TC_11", "age": 30, "income": 10.0, "score": 700, "emp": "F", "expected": "REJECT"},
    {"id": "TC_12", "age": 30, "income": 5.0,  "score": 701, "emp": "F", "expected": "REJECT"},
    {"id": "TC_13", "age": 65, "income": 14.9, "score": 850, "emp": "C", "expected": "MANUAL REVIEW"},
    {"id": "TC_14", "age": 30, "income": 15.0, "score": 600, "emp": "C", "expected": "APPROVE"},
    {"id": "TC_15", "age": 30, "income": 500.0,"score": 850, "emp": "C", "expected": "APPROVE"},
    {"id": "TC_16", "age": 30, "income": 15.0, "score": 701, "emp": "F", "expected": "MANUAL REVIEW"},
    {"id": "TC_17", "age": 30, "income": 20.0, "score": 501, "emp": "F", "expected": "MANUAL REVIEW"},
]

passed_count = 0

print(f"{'Test ID':<9}{'Inputs (Age, Inc, Scr, Emp)':<32}{'Expected':<17}{'Actual':<17}{'Status':<8}")
print("-" * 88)

# Chạy vòng lặp qua từng Test Case
for tc in test_cases:
    actual = evaluate_loan(tc["age"], tc["income"], tc["score"], tc["emp"])
    status = "PASSED" if actual == tc["expected"] else "FAILED"
    if status == "PASSED":
        passed_count += 1
        
    input_str = f"({tc['age']}, {tc['income']}, {tc['score']}, '{tc['emp']}')"
    print(f"{tc['id']:<9}{input_str:<32}{tc['expected']:<17}{actual:<17}{status:<8}")

print("-" * 88)
print(f"KẾT QUẢ KIỂM THỬ: {passed_count}/{len(test_cases)} Test Cases PASSED.")
