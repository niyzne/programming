# Keep Hydrated!

---
## Info

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded _down_.

For example:

```
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
```

---
Algorithms | Mathematics | Fundamentals

---
## Code

Solution

```PowerShell
function stayHydratred($time){

  #Your Code here

}
```

Sample Tests

```PowerShell
BeforeAll {
  .$PSCommandPath.Replace('.Tests.ps1', '.ps1')
  
  function testing($time, $expect) 
    {
        $ans = stayHydratred $time
        $ans | Should -Be $expect
    }

  function fixed()
    {
        testing 2 1
        testing 1.4 0
        testing 12.3 6
        testing 0.82 0
        testing 11.8 5
        testing 1787 893
        testing 0 0 
    }
}

Describe "stayHydrated" {
  Context "Fixed Tests" {
    It "Should Pass Fixed Tests" {
      fixed
    } 
  }
}
```

---
## Code Solution

```PowerShell
function stayHydratred($time){
	[Math]::Floor($time * 0.5)
}
```

---