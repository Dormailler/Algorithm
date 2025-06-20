-- 코드를 입력하세요
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS A
WHERE EXISTS (
    SELECT CART_ID 
    FROM CART_PRODUCTS
    WHERE CART_ID = A.CART_ID
      AND NAME = 'Milk'
) 
AND EXISTS (
    SELECT CART_ID 
    FROM CART_PRODUCTS
    WHERE CART_ID = A.CART_ID
      AND NAME = 'Yogurt'
)
ORDER BY CART_ID