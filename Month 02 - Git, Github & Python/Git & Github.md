# Git & GitHub for DevOps  

## 1. Basics of Git  
- Git is a **version control system** to track changes in code.  
- Helps in **collaboration, rollback, and branching**.  
- GitHub is a **cloud platform** to host Git repositories.  

---

## 2. Repository Management  
- `git init` → Initialize a new repository  
- `git clone <url>` → Clone a repository from remote  
- `git remote -v` → Show remote connections  
- `git remote add origin <url>` → Link local repo to GitHub  

---

## 3. Staging & Committing  
- `git status` → Show changes  
- `git add file.txt` → Stage a file  
- `git add .` → Stage all changes  
- `git commit -m "message"` → Save staged changes  

---

## 4. Pushing & Pulling  
- `git push origin main` → Push commits to GitHub  
- `git pull origin main` → Get latest changes from GitHub  
- `git fetch` → Fetch changes (without merging)  

---

## 5. Branching & Merging  
- `git branch` → List branches  
- `git branch feature1` → Create new branch  
- `git checkout feature1` → Switch to branch  
- `git merge feature1` → Merge branch into current branch  
- `git branch -d feature1` → Delete branch  

---

## 6. Undoing Changes  
- `git checkout -- file.txt` → Discard local changes  
- `git reset HEAD file.txt` → Unstage file  
- `git revert <commit>` → Undo a commit safely  
- `git reset --hard <commit>` → Reset to specific commit (dangerous)  

---

## 7. Viewing History  
- `git log` → Show commit history  
- `git log --oneline` → Compact history  
- `git diff` → Show changes not staged  
- `git diff --staged` → Show staged changes  

---

## 8. Stashing Changes  
- `git stash` → Save temporary changes  
- `git stash pop` → Reapply stashed changes  
- `git stash list` → View stashed changes  

---

## 9. Tags & Releases  
- `git tag v1.0` → Create lightweight tag  
- `git tag -a v1.0 -m "Release v1.0"` → Annotated tag  
- `git push origin v1.0` → Push tag to GitHub  

---

## 10. GitHub Concepts  
- **Fork** → Copy someone else’s repo to your account  
- **Pull Request (PR)** → Propose changes to main branch  
- **Issues** → Track bugs, tasks, enhancements  
- **GitHub Actions** → Automate CI/CD workflows  
- **README.md** → Project documentation  
- **.gitignore** → Ignore files/folders (e.g., logs, env)  

---

## 11. Collaboration Workflow  
1. Fork repository  
2. Clone locally  
3. Create new branch  
4. Commit & push changes  
5. Open a Pull Request (PR) on GitHub  
