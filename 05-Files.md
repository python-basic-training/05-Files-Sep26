# Задание 1: Сравнение двух текстовых файлов

Вам даны два файла:

- **old.txt** — старая версия списка задач  
- **new.txt** — новая версия списка задач  

Найти отличия между двумя версиями и создать файл **diff.txt**, в котором:

- строки, которые **есть только в old.txt**, помечаются `-`
- строки, которые **есть только в new.txt**, помечаются `+`
- неизменённые строки выводятся без префикса
- частичное изменение строк не учитывается, считается что это новая/старая строка
- порядок следования строк должен быть сохранен (относительно файла new.txt)

Модуль difflib использовать нельзя.
---

## Пример входных файлов

### old.txt
Buy milk  
Send report to manager  
Clean the kitchen  
Call mom  
Pay electricity bill

### new.txt
Buy milk  
Send report to manager  
Call mom  
Pay electricity bill  
Buy cat food  
Clean the balcony  

### diff.txt
Buy milk  
Send report to manager  
-Clean the kitchen  
Call mom  
Pay electricity bill  
+Buy cat food  
+Clean the balcony  

---

# Задание 2: Эмуляция работы продуктового магазина 

Необходимо разработать модуль, который имитирует работу продуктового магазина.  
Исходные данные о товарах и продажах поступают в формате **JSON**,  
а результаты работы функций должны сохраняться в **CSV‑файлы**.

---

## products.json

```json
{
  "products": [
    {"id": 1, "name": "Milk", "category": "Dairy", "price": 2.49, "expires": "2026-10-15"},
    {"id": 2, "name": "Bread", "category": "Bakery", "price": 1.19, "expires": "2026-10-18"},
    {"id": 3, "name": "Eggs", "category": "Dairy", "price": 3.10, "expires": "2026-10-03"},
    {"id": 4, "name": "Apples", "category": "Fruits", "price": 0.89, "expires": "2026-10-07"},
    {"id": 5, "name": "Chicken Breast", "category": "Meat", "price": 6.49, "expires": "2026-10-09"},
    {"id": 6, "name": "Orange Juice", "category": "Drinks", "price": 3.99, "expires": "2026-10-10"},
    {"id": 7, "name": "Yogurt", "category": "Dairy", "price": 1.49, "expires": "2026-10-29"},
    {"id": 8, "name": "Bananas", "category": "Fruits", "price": 0.59, "expires": "2026-10-18"}
  ]
}
```

## sales.json

```json
{
  "sales": [
    {"product_id": 1, "quantity": 3},
    {"product_id": 4, "quantity": 6},
    {"product_id": 5, "quantity": 2},
    {"product_id": 2, "quantity": 1},
    {"product_id": 7, "quantity": 4}
  ]
}
```

## Функции модуля

### 1. `export_expiring_products(json_data, filename, days)`
Вывести товары, срок годности которых истекает в ближайшие `days` дней.

**CSV‑выход:**  
`id, name, category, expires, days_left`

---

### 2. `export_expired_products(json_data, filename)`
Вывести товары, у которых срок годности уже истёк.

**CSV‑выход:**  
`id, name, category, expires, expired_days_ago`

---

### 3\*. `export_sales_report(json_data, filename)`
Создать отчёт по продажам: название товара, количество проданных единиц, общая выручка.

**CSV‑выход:**  
`product_name, quantity_sold, total_revenue`

---

### 4\*. `export_category_summary(json_data, filename)`
Сгруппировать товары по категориям: количество товаров и средняя цена.

**CSV‑выход:**  
`category, products_count, average_price`
