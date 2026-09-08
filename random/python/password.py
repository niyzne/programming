def password():
    retry_count = 0
    max_retries = 5

    while retry_count < max_retries:
        print(f'Attempting connection... Attempt # {retry_count + 1}')
        retry_count += 1

    print("Loop terminated.")

password()
