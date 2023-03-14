import subprocess
git_diff_output = subprocess.check_output('git diff --name-only', shell=True)
print(git_diff_output)

