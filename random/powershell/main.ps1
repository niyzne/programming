Write-Output "Hello, world!"

# comment example: declare and print name
$name = "Alex"
Write-Output $name

Write-Output "Hello $name"

Write-Output "Hello $name, This is very cool"

$age = 20
Write-Output $age
Write-Output "$name is $age years old"

# prints the type of the stuff
$age.GetType().FullName
$name.GetType().FullName

# the stuff is case insensitive, interesting
Write-Output $name
Write-Output $NAME
Write-Output $age
Write-Output $AGE

# Comparision
$z = 10
Write-Output $z
$z -eq 10

$num = "25"
$num.GetType().FullName
$num = [int]$num
$num.GetType().FullName
