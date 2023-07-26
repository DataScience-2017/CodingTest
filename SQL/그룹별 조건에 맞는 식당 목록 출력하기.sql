-- MEMBER_PROFILE 테이블을 M, REST_REVIEW 테이블을 R로 별칭(alias)를 주었습니다.
-- 별칭을 사용하면 테이블 이름을 반복해서 쓸 필요가 없어 코드가 간결해집니다.
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, R.REVIEW_DATE
FROM MEMBER_PROFILE M
-- REST_REVIEW 테이블을 서브쿼리로 처리했습니다. 이 서브쿼리는 리뷰를 가장 많이 작성한 회원의 모든 리뷰를 선택합니다.
JOIN (
    SELECT REVIEW_TEXT, REVIEW_DATE, MEMBER_ID
    FROM REST_REVIEW
    WHERE MEMBER_ID = (
        -- 이 내부 서브쿼리는 리뷰를 가장 많이 작성한 회원의 ID를 찾습니다.
        -- GROUP BY를 사용해 회원 ID별로 그룹을 만들고, COUNT(*)를 사용해 각 그룹의 리뷰 개수를 세었습니다.
        -- ORDER BY COUNT(*) DESC를 사용해 리뷰 개수를 기준으로 내림차순 정렬했습니다.
        -- LIMIT 1을 사용해 가장 많은 리뷰를 작성한 회원 하나만 선택했습니다.
        SELECT MEMBER_ID
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY COUNT(*) DESC
        LIMIT 1)
    ) R
-- MEMBER_PROFILE 테이블과 서브쿼리를 조인했습니다. 이렇게 하면 리뷰를 가장 많이 작성한 회원의 이름과 그 회원의 리뷰 정보를 함께 선택할 수 있습니다.
ON R.MEMBER_ID = M.MEMBER_ID
-- 결과를 리뷰 작성일과 리뷰 텍스트 순으로 오름차순 정렬했습니다.
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT
