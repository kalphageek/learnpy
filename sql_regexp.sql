4. REGEXP_LIKE : 소문자 3자로 끝나는 라인
SCOTT>SELECT *
  2  FROM reg_test
  3  WHERE REGEXP_LIKE(text,'[a-z]{3}$');
TEXT
----------
123abc

7. REGEXP_REPLACE : 문자사이에 '-'를 넣기
SCOTT>SELECT name, RTRIM(REGEXP_REPLACE(name,'(.)','\1-'),'-') "AFTER"
  3  FROM student
  4  WHERE deptno1=101;
NAME        AFTER
----------  ----------
서진수      서-진-수
김신영      김-신-영
일지매      일-지-매
이윤나      이-윤-나
