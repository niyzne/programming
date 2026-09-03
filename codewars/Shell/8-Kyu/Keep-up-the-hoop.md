# Keep up the hoop

---
## Info

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (`n`) how many times the hoop goes round and it will return him an encouraging message:

- If Alex gets 10 or more hoops, return the string `"Great, now move on to tricks"`.
- If he doesn't get 10 hoops, return the string `"Keep at it until you get it"`.

---
Fundamentals

---
## Code

Solution

```shell
#!/bin/bash
n=$1

#code here
```

Sample Tests

```shell
output = run_shell args: ['8']


 describe "Solution" do
   it "should return the argument passed in" do
     expect(output).to eq('Keep at it until you get it')
   end
 end
```

---
## Code Solution

```shell
#!/bin/bash
n=$1

if [ $n -ge 10 ]; then
  echo "Great, now move on to tricks"
else
  echo "Keep at it until you get it"
fi
```

---
## Resources I used for help

https://www.geeksforgeeks.org/linux-unix/conditional-statements-shell-script/

https://www.pluralsight.com/resources/blog/cloud/conditions-in-bash-scripting-if-statements

https://www.digitalocean.com/community/tutorials/if-else-in-shell-scripts

https://stackoverflow.com/questions/20449543/shell-equality-operators-eq

---