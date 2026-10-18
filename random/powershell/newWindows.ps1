for ($i = 1; $i -le 5; $i++) {
        Start-Process "C:\Program Files\Mozilla Firefox\firefox.exe" -ArgumentList "-new-window", "https://www.google.com"
}
