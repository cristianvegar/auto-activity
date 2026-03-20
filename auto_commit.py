import random
import subprocess
from datetime import datetime

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.returncode

def main():
    commits = random.randint(1, 5)

    for i in range(commits):
        # SIEMPRE modificar archivo
        with open("log.txt", "a") as f:
            f.write(f"{datetime.now()} - cambio {random.randint(1,1000)}\n")

        run("git add .")

        # 👇 evitar error si no hay cambios
        commit_result = run(f'git commit -m "update: cambio {i}"')

        if commit_result != 0:
            print("No hubo cambios, saltando commit")

    run("git push origin main")

if __name__ == "__main__":
    main()
