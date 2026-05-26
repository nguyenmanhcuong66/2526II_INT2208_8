def evaluate_loan(age: int, income: float, credit_score: int, employment: str) -> str:
    # Rule 1: Kiểm tra ngoại lệ (Invalid Inputs - C0)
    if not (18 <= age <= 65):
        return "Invalid Input"
    if not (5.0 <= income <= 500.0):
        return "Invalid Input"
    if not (300 <= credit_score <= 850):
        return "Invalid Input"
    if employment not in ["C", "F"]:
        return "Invalid Input"

    # Rule 2: High Risk (C1)
    if credit_score <= 500:
        return "REJECT"
        
    # Xác định Medium Risk (C2) - Nếu không phải Medium thì chắc chắn là Low Risk do đã lọc ở trên
    is_medium_risk = (501 <= credit_score <= 700)
    
    # Xử lý Logic dựa trên Thu nhập (C3) và Loại hợp đồng (C4)
    if income < 15.0:
        if is_medium_risk:
            return "REJECT"  # Rule 3
        else:
            # Low Risk
            if employment == "F":
                return "REJECT"  # Rule 4
            else:
                return "MANUAL REVIEW"  # Rule 5
    else:
        # income >= 15.0 (Áp dụng chung cho cả Medium và Low Risk)
        if employment == "C":
            return "APPROVE"  # Rule 6
        else:
            return "MANUAL REVIEW"  # Rule 7