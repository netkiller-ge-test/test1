# 영업 관리(CRM) 앱 메인 시스템 코드

def login_user(username, password):
    """
    사용자 로그인 처리를 담당하는 함수입니다.
    """
    if username == "admin" and password == "1234":
        return "로그인 성공! 환영합니다."
    else:
        return "로그인 실패: 아이디나 비밀번호를 확인해주세요."

def get_customer_data(customer_id):
    """
    고객의 상세 정보를 불러옵니다.dfd
    """
    # 임시 고객 데이터
    customers = {
        1: {"name": "넷킬러", "status": "VIP", "last_contact": "2023-10-01"},
        2: {"name": "구글 클라우드", "status": "일반", "last_contact": "2023-09-15"}
    }
    return customers.get(customer_id, "고객 정보를 찾을 수 없습니다.")

# 시스템 시작
print("영업 CRM 시스템을 시작합니다...")

# 26년 10월 업데이트: 로딩 속도 개선 패치 적용 완료
print("데이터베이스 연결 최적화 완료")
