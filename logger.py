from datetime import datetime
from typing import Dict
import os

class Logger:
    LOG_FILE = 'logs.txt'
    
    @classmethod
    def init_log_file(cls, log_file: str, clear: bool = True):
        cls.LOG_FILE = log_file
        if clear and os.path.exists(log_file):
            os.remove(log_file)  # Удаляем старый файл
        
        # Создаем новый файл с заголовком
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("="*60 + "\n")
            f.write(f"🧪 ЛОГИ СИСТЕМЫ\n")
            f.write(f"Запуск: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
                   
    @classmethod 
    def write_log(cls, agent_name: str, action: str, dop_info: str = '') -> Dict:
        log = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'agent_name': agent_name,
            'action': action,
            'dop_info': str(dop_info)
        }
        print(log)
        
        with open(cls.LOG_FILE, 'a', encoding="utf-8") as f:
            f.write(str(log) + '\n')
        
        return log