# 영업 할인율 계산 엔진

def calculate_discount(customer_type, total_amount, promo_code=None):
    """
    고객 등급 및 프로모션 코드에 따른 최종 금액을 계산합니다.
    """
    discount_rate = 0.0

    if customer_type == "VIP":
        discount_rate += 0.10  # VIP 10% 할인
    elif customer_type == "Enterprise":
        discount_rate += 0.20  # Enterprise 20% 할인

    # 프로모션 코드 검증
    if promo_code == "NK2026":
        discount_rate += 0.05  # 5% 추가 할인

    final_price = total_amount * (1 - discount_rate)
    return round(final_price, 2)
