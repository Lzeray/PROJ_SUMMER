from datetime import datetime
from typing import Dict, List
import os
import json

class Logger:
    LOG_FILE = 'logs.json'
    
    @classmethod
    def init_log_file(cls, log_file: str, clear: bool = True):
        cls.LOG_FILE = log_file
        
        if clear or not os.path.exists(log_file):
            with open(log_file, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)
                   
    @classmethod 
    def write_log(cls, agent_name: str, action: str, dop_info: str = '') -> Dict:
        dop_info = str(dop_info)
        if len(dop_info) > 100:
            dop_info = dop_info[:100] + '...'
            
        log = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'agent_name': agent_name,
            'action': action,
            'dop_info': dop_info
        }
        
        print(log)
        
        try:
            with open(cls.LOG_FILE, 'r', encoding="utf-8") as f:
                logs_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            logs_data = []
            
        logs_data.append(log)
        
        with open(cls.LOG_FILE, 'w', encoding="utf-8") as f:
            json.dump(logs_data, f, ensure_ascii=False, indent=4)
        
        return log
    
    @classmethod
    def read_logs(cls) -> List[Dict]:
        try:
            with open(cls.LOG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    @classmethod
    def get_agent_stats(cls) -> Dict:
        """Возвращает статистику по агентам"""
        logs = cls.read_logs()
        stats = {}
        
        for log in logs:
            agent = log.get('agent_name', 'Unknown')
            if agent not in stats:
                stats[agent] = {
                    'actions': 0,
                    'last_action': None,
                    'first_action': None
                }
            stats[agent]['actions'] += 1
            if not stats[agent]['first_action']:
                stats[agent]['first_action'] = log.get('time')
            stats[agent]['last_action'] = log.get('time')
        
        return stats
    
    @classmethod
    def get_agent_actions(cls, agent_name: str) -> List[Dict]:
        """Возвращает все действия конкретного агента"""
        logs = cls.read_logs()
        return [log for log in logs if log.get('agent_name') == agent_name]