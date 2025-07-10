import json
import random
from datetime import datetime, timedelta

services = ["Service1", "Service2", "Service3"]
envs = ["latest", "stage"]
levels = ["INFO", "WARN", "ERROR"]
loggers = ["LoggerA", "LoggerB", "LoggerC"]

base_time = datetime(2025, 7, 8, 12, 34, 56)
records = []

for i in range(100):
    service = random.choice(services)
    env = random.choice(envs)
    level = random.choice(levels)
    logger = random.choice(loggers)
    host = f"host-{str(i%10+1).zfill(2)}"
    thread = f"thread-{123+i}"
    processor = f"proc-{str(i%10+1).zfill(2)}"
    version = f"1.0.{i%10}"
    client_id = f"client-{str(i+1).zfill(3)}"
    wallet_id = f"wallet-{str(i+1).zfill(3)}"
    conv_id = f"conv-{str(i+1).zfill(3)}"
    date = base_time + timedelta(seconds=i*5)
    date_str = date.strftime("%Y-%m-%dT%H:%M:%SZ")
    msg = f"Sample log message {i+1}"

    record = {
        "Host": host,
        "Date": date_str,
        "Thread": thread,
        "Identifiers": {
            "App-Name": service,
            "Processor": processor,
            "Version": version,
            "AuthzClientId": client_id,
            "RequestDateTime": date_str,
            "WalletId": wallet_id,
            "ConversationId": conv_id,
            "CustomAttributes": {
                "AppEnv": env
            }
        },
        "Level": level,
        "Logger": logger,
        "Msg": msg
    }
    records.append(record)

with open("synthetic_logs.json", "w") as f:
    json.dump(records, f, indent=4)
