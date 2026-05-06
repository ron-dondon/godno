def find_max_drop(temps):
    # Проверка: если данных мало, скачка быть не может
    if len(temps) < 2:
        return 0
    
    max_diff = 0  # Сюда запишем самый большой скачок
    
    # Идем по индексам до предпоследнего
    for i in range(len(temps) - 1):
        # Находим разницу между текущим и следующим
        current_diff = abs(temps[i] - temps[i+1])
        
        # Если текущая разница больше той, что мы видели раньше — обновляем максимум
        if current_diff > max_diff:
            max_diff = current_diff
            
    return max_diff

# Тестируем:
data = [15, 18, 14, 25, 20] 
# Пары: |15-18|=3, |18-14|=4, |14-25|=11, |25-20|=5
print(f"Максимальный скачок: {find_max_drop(data)}")