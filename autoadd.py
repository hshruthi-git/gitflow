import os
commit_message = "enter commit message"
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push")
print("git commit and push is successful")
