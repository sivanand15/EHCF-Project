import subprocess
git_diff_output = subprocess.check_output('git status', shell=True)
print(git_diff_output)
