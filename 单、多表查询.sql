单表查询
查询出部门编号为30的所有员工
SELECT * FROM t_employees WHERE deptno=30;
所有销售员的姓名、编号和部门编号。
SELECT ename,empno,deptno FROM t_employees WHERE job ="销售员";
找出奖金高于工资的员工。
SELECT * FROM t_employees WHERE comm > sal;
找出奖金高于工资60%的员工。
SELECT * FROM t_employees WHERE comm > (sal*60);
找出部门编号为10中所有经理，和部门编号为20中所有销售员的详细资料。
SELECT * FROM t_employees WHERE (deptno=10 AND job='经理')OR (deptno=20 AND job='销售员');
找出部门编号为10中所有经理，部门编号为20中所有销售员，还有即不是经理又不是销售员但其工资大或等于20000的所有员工详细资料。
SELECT * FROM t_employees WHERE (deptno=10 AND job='经理') OR (deptno=20 AND job='销售员')OR (sal >=20000 AND job='经理'OR job='销售员');
无奖金或奖金低于1000的员工。
SELECT ename,comm FROM t_employees WHERE comm < 100 OR comm IS NULL;
查询名字由三个字组成的员工。
SELECT * FROM t_employees WHERE ename LIKE '___';
查询2000年入职的员工。
SELECT * FROM t_employees WHERE hiredate='2000-%';
查询所有员工详细信息，用编号升序排序
SELECT * FROM t_employees ORDER BY empno ASC;
查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
SELECT * FROM t_employees  ORDER  BY sal DESC,hiredate ASC;
查询每个部门的平均工资
SELECT deptno ,AVG(sal)FROM t_employees GROUP BY deptno;
查询每个部门的雇员数量
SELECT deptno ,COUNT(*) FROM t_employees GROUP BY deptno;
查询每种工作的最高工资、最低工资、人数
SELECT job,MAX(sal),MIN(sal),COUNT(*) FROM t_employees GROUP BY job;


多表查询
查出至少有一个员工的部门，显示部门编号，部门名称，部门位置，部门人数
SELECT d.*, z1.cnt 
FROM dept d, (SELECT deptno, COUNT(*) cnt FROM emp GROUP BY deptno) z1
WHERE d.deptno = z1.deptno
列出所有员工的姓名及其直接上级的姓名。
SELECT yg. 'ename', sj. 'ename' 
FROM 't_employees' yg JOIN 't_employees' sj ON yg. 'MGR' = sj. 'empno'
 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
 SELECT e.empno, e.ename, e.deptno
FROM emp e, emp m
WHERE e.mgr=m.empno AND e.hiredate<m.hiredate；
SELECT e.empno, e.ename, d.dname
FROM emp e, emp m, dept d
WHERE e.mgr=m.empno AND e.hiredate<m.hiredate AND e.deptno=d.deptno；
列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
SELECT *
FROM emp e RIGHT OUTER JOIN dept d
ON e.deptno=d.deptno
列出最低薪金大于15000的各种工作及从事此工作的员工人数。
SELECT job, COUNT(*)
FROM emp e
GROUP BY job
HAVING MIN(sal) > 15000；

列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
SELECT *
FROM emp e
WHERE e.deptno=(SELECT deptno FROM dept WHERE dname='销售部')
列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
SELECT e.*, d.dname, m.ename, s.grade
FROM emp e, dept d, emp m, salgrade s
WHERE e.sal>(SELECT AVG(sal) FROM emp) AND e.deptno=d.deptno AND e.mgr=m.empno AND e.sal BETWEEN s.losal AND s.hisal
SELECT e.*, d.dname, m.ename, s.grade
FROM 
  emp e LEFT OUTER JOIN dept d ON e.deptno=d.deptno
        LEFT OUTER JOIN emp m ON e.mgr=m.empno
        LEFT OUTER JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.sal>(SELECT AVG(sal) FROM emp)


SELECT * FROM emp;
SELECT * FROM dept;
SELECT * FROM salgrade;
列出与clack从事相同工作的所有员工及部门名称。
SELECT e.*, d.dname
FROM emp e, dept d
WHERE e.deptno=d.deptno AND job=(SELECT job FROM emp WHERE ename='庞统')
列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
SELECT e.ename, e.sal, d.dname
FROM emp e, dept d
WHERE e.deptno=d.deptno AND sal > ALL (SELECT sal FROM emp WHERE deptno=30)


