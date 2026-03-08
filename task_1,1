from datetime import datetime


def get_days_from_today(date_string):
    try:
      
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        
    
        today = datetime.today().date()
        
      
        delta = today - given_date
        

        return delta.days

    except ValueError:
        return "Помилка: Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."
    except TypeError:

        return "Помилка: Вхідні дані мають бути рядком."

print(f"Днів до 2026-07-29: {get_days_from_today('2026-07-29')}")
