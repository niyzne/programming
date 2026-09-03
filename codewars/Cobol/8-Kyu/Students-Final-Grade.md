# Student's Final Grade

---
## Info

Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

This function should return a number (final grade). There are four types of final grades:

- 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
- 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
- 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
- 0, in other cases

Examples (**Inputs**-->**Output**):

```
100, 12 --> 100
99, 0 --> 100
10, 15 --> 100

85, 5 --> 90

55, 3 --> 75

55, 0 --> 0
20, 2 --> 0
```

*Use Comparison and Logical Operators.

---
Fundamentals

---
## Code

Solution

```Cobol
       identification division.
       program-id. finalGrade.     
       data division.
       linkage section.
       01  exam          pic 9(3).
       01  projects      pic 9(2).   
       01  result        pic 9(3).      
       procedure division using exam projects result. 
      * your code here
          goback.
       end program finalGrade.
```

Sample Tests

```Cobol
       identification division.
       program-id. tests.
       author. "ejini战神".
      
       data division.
       working-storage section.
       01  exam          pic 9(3).
       01  projects      pic 9(2).     
       01  exam-disp     pic Z(2)9.
       01  projects-disp pic Z9.      
       01  result        pic 9(3).
       01  expected      pic 9(3).
      
       procedure division.    
           testsuite 'Fixed Tests'.     
           move 100  to exam
           move 5    to projects          
           move 100  to expected
           perform dotest
      
           move 99   to exam
           move 0    to projects          
           move 100  to expected
           perform dotest   
         
           move 10   to exam
           move 15   to projects          
           move 100  to expected
           perform dotest
      
           move 85   to exam
           move 5    to projects          
           move 90   to expected
           perform dotest
      
           move 55   to exam
           move 3    to projects          
           move 75   to expected
           perform dotest
      
           move 55   to exam
           move 0    to projects          
           move 0    to expected
           perform dotest
      
           move 20   to exam
           move 2    to projects          
           move 0    to expected
           perform dotest      

           end tests.
      
       dotest.
           move exam to exam-disp
           move projects to projects-disp       
           testcase 'Testing exam = ' function trim(exam-disp) 
                    ', projects = ' function trim(projects-disp).
           initialize result
           call 'finalGrade' using by content exam projects
                                   by reference result
           expect result to be expected.
           .
      
       end program tests.
```

---
## Code Solution

```Cobol
       identification division.
       program-id. finalGrade.     
       data division.
       linkage section.
       01  exam          pic 9(3).
       01  projects      pic 9(2).   
       01  result        pic 9(3).      
       procedure division using exam projects result. 
      * your code here
        IF exam > 90 OR projects > 10
           MOVE 100 TO result
        ELSE
           IF exam > 75 AND projects >= 5
              MOVE 90 TO result
           ELSE
              IF exam > 50 AND projects >= 2
                 MOVE 75 TO result
              ELSE
                 MOVE 0 TO result
              END-IF
           END-IF
        END-IF
          goback.
       end program finalGrade.
```

---
## Resources I used for help

https://www.tutorialspoint.com/cobol/cobol_condition_statements.htm

https://www.mainframestechhelp.com/tutorials/cobol/return-statement.htm

https://www.ibm.com/docs/en/cobol-zos/6.3.0?topic=statements-if-statement

---