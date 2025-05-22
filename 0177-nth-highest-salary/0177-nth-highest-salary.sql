CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N - 1 ;
  RETURN (
      # Write your MySQL query statement below.
      select (
        select distinct salary
        from Employee
        order by salary Desc
        Limit 1 offset N
      ) 

  );
END