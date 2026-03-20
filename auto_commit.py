import random
import subprocess
from datetime import datetime

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def main():
    # número random de commits
    commits = random.randint(1, 5)

    for i in range(commits):
        with open("log.txt", "a") as f:
            f.write(f"{datetime.now()} - cambio {random.randint(1,1000)}\n")

        run("git add .")
        run(f'git commit -m "update: cambio automático {i}"')

    run("git push origin main")

if __name__ == "__main__":
    main()
