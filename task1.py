def total_salary(path):
    total_sum = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_sum += int(salary)
                count += 1
        average = total / count if count > 0 else 0
        return total_sum, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None

total, average = total_salary("./file1.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
