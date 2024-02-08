import sys

def last_10_rows_func(filename, lines=10):
    try:
        # Вказуємо шлях до файлу, що знаходиться у папці "data"
        filepath = f"data/{filename}"
        with open(filepath, 'r') as file:
            queue = []
            for line in file:
                queue.append(line)
                if len(queue) > lines:
                    queue.pop(0)
        for line in queue:
            print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Перевірка, чи сценарій отримав аргумент
if len(sys.argv) == 2:
    filename = sys.argv[1]
    last_10_rows_func(filename)
else:
    print("Error: Please provide a filename as an argument.")
