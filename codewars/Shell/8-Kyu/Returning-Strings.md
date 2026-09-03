# Returning Strings

---
## Info

Create a function that accepts a parameter representing a `name` and returns the message: `"Hello, <name> how are you doing today?"`.

_[Make sure you type the exact thing I wrote or the program may not execute properly]_

---
Strings | Fundamentals

---
## Code

Solution

```shell
#!/bin/bash
#your code here
```

Sample Tests

```shell
# run the solution and store its result
 output = run_shell args: ['shell']

 describe "sample test" do
   it "should return \"Hello, <name> how are you doing today?\"" do
     expect(output).to eq('Hello, shell how are you doing today?')
   end
 end
```

---
## Code Solution

```shell
#!/bin/bash

name=$1

echo "Hello, $name how are you doing today?"
```

---