-- 사용자 활동 및 통계 리포트 쿼리

-- 1. 월별 활성 사용자(MAU) 집계
SELECT 
    DATE_TRUNC('month', created_at) AS activity_month,
    COUNT(DISTINCT user_id) AS active_users
FROM user_logs
WHERE action_type IN ('LOGIN', 'PURCHASE')
GROUP BY 1
ORDER BY activity_month DESC;

-- 2. 최근 30일간 VIP 대상 고객 조회
SELECT 
    u.user_id,
    u.email,
    SUM(p.amount) AS total_spent,
    MAX(p.created_at) AS last_purchase_date
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE p.created_at >= NOW() - INTERVAL '30 days'
GROUP BY u.user_id, u.email
HAVING SUM(p.amount) > 1000000
ORDER BY total_spent DESC;
