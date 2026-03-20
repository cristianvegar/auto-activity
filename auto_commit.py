import random
import subprocess
import time
from datetime import datetime

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
    return datetime.today().weekday() < 5  # 0=Lunes, 4=Viernes

def decide_commit_volume():
    # 20% de días muy activos
    if random.random() < 0.2:
        return random.randint(5, 10)
    else:
        return random.randint(1, 5)

def maybe_skip_day():
    # 15% probabilidad de no hacer nada
    return random.random() < 0.15

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

        run("git add .")

        commit_result = run(f'git commit -m "{random_commit_message()}"')

        if commit_result != 0:
            print("No hubo cambios, skip commit")
            continue

        # Delay entre commits (simula trabajo real)
        sleep_time = random.randint(10, 90)
        print(f"Esperando {sleep_time}s...")
        time.sleep(sleep_time)

    run("git push origin main")

if __name__ == "__main__":
    main()
