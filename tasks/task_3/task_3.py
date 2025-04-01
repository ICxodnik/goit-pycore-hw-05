import sys
from collections import Counter

# Функція для парсингу рядка логу
def parse_log_line(line: str):
    parts = line.split(' ', 3)  # Розділяємо на дату, час, рівень та повідомлення
    return {'level': parts[2], 'message': parts[3] if len(parts) > 3 else ''}

# Функція для завантаження логів з файлу
def load_logs(file_path: str):
    try:
        logs = []
        with open(file_path, 'r') as file:
           for line in file:
                logs.append(parse_log_line(line.strip()))
        return logs
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдений.")
        sys.exit(1)

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs, level):
    filtered_logs = []
    for log in logs:
        if log['level'].lower() == level.lower():
            filtered_logs.append(log)
    return filtered_logs


# Головна функція для виконання скрипту
def main():
    if len(sys.argv) < 2:
        print("Помилка: Не вказано шлях до файлу.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    print(logs)
    # Якщо вказано рівень, фільтруємо за ним
    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        logs = filter_logs_by_level(logs, level)

        for log in logs:
            print(f"{log['message']}")

    # Підрахунок кількості записів за рівнями
    counts = Counter(log['level'] for log in logs)

    # Виведення статистики
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

if __name__ == '__main__':
    main()
