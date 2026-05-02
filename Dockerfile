# Використовуємо офіційний образ Python
FROM python:3.11-slim

# встановлюємо робочу директорію
WORKDIR /app

# копіюємо залежності та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо решту коду
COPY . .

# команда для запуску краулера
CMD ["python", "crawler.py"]
