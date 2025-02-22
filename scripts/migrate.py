import subprocess

command = "alembic upgrade head"

subprocess.run(command, shell=True)
