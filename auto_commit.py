import random
import subprocess
import time
from datetime import datetime
import os

# CONFIGURACIÓN 
AUTHOR_NAME = "Cristian Vega"
AUTHOR_EMAIL = "crisvegarodri@gmail.com"

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.returncode

commit_types = ["feat", "fix", "refactor", "chore", "docs"]

descriptions = [
    "update logic",
    "improve performance",
    "clean code",
    "adjust config",
    "minor fix",
    "refactor module",
    "update data pipeline",
    "improve logging"
]

def random_commit_message():
    return f"{random.choice(commit_types)}: {random.choice(descriptions)}"

def modify_file():
    file_choice = random.choice(["log.txt", "data.json"])

    if file_choice == "log.txt":
        with open("log.txt", "a") as f:
            f.write(f"{datetime.now()} - event {random.randint(1,9999)}\n")

    else:
        with open("data.json", "a") as f:
            f.write(f'{{"value": {random.randint(1,1000)}, "time": "{datetime.now()}"}},\n')

def is_weekday():
    return datetime.today().weekday() < 5

def decide_commit_volume():
    if random.random() < 0.2:
        return random.randint(5, 10)
    else:
        return random.randint(1, 5)

def maybe_skip_day():
    return random.random() < 0.15

def make_commit():
    run("git add .")

    message = random_commit_message()

    # FORZAR AUTHOR
    cmd = f'git commit --author="{AUTHOR_NAME} <{AUTHOR_EMAIL}>" -m "{message}"'
    return run(cmd)

def main():
    if not is_weekday():
        print("Fin de semana, no actividad")
        return

    if maybe_skip_day():
        print("Día sin actividad (simulación humana)")
        return

    commits = decide_commit_volume()
    print(f"Hoy se harán {commits} commits")

    for i in range(commits):
        modify_file()

        commit_result = make_commit()

        if commit_result != 0:
            print("No hubo cambios, skip commit")
            continue

        sleep_time = random.randint(10, 90)
        print(f"Esperando {sleep_time}s...")
        time.sleep(sleep_time)

    # IMPORTANTE: el push lo manejan los pipelines
    print("Commits generados correctamente")

if __name__ == "__main__":
    main()
