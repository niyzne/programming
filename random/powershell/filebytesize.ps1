$allFiles = Get-ChildItem "C:\Windows\" -File
$byteNum = 0
foreach ($file in $allFiles) {
	$byteNum = $byteNum + $file.length
}
Write-Output "The files total $byteNum bytes."
