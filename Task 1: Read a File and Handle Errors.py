try:
    with open("sample.txt","r") as file:
        for idx, line in enumerate(file, start = 1):
            print(f"Line {idx} : {line.strip()}")

except FileNotFoundError:
    print(f'the file sample.txt was not found')