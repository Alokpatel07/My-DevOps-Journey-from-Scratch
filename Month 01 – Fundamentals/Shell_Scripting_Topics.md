# Shell Scripting for DevOps

## 1. Basics of Shell Scripting
- Shell scripting automates repetitive tasks on Linux/Unix systems.  
- Written mostly in **Bash**.  
- Used for deployments, monitoring, server management, and CI/CD pipelines.

---

## 2. File & Directory Management
- `ls -l` → List files with details  
- `pwd` → Show current directory  
- `cd dir` → Change directory  
- `mkdir dir` → Create directory  
- `rm -rf dir` → Remove directory and contents  
- `touch file` → Create empty file  

---

## 3. File Permissions
- `chmod 755 script.sh` → Change file permissions  
- `chown user:group file.txt` → Change ownership  

---

## 4. Text Processing
- `cat file.txt` → Show file content  
- `grep "error" logfile.txt` → Search text  
- `awk '{print $1}' file` → Print first column  
- `sed 's/foo/bar/g' file` → Replace text  

---

## 5. System Monitoring
- `top` → Show processes  
- `ps aux` → List running processes  
- `df -h` → Disk usage  
- `free -h` → Memory usage  
- `uptime` → Load average  

---

## 6. Networking
- `ping google.com` → Test connectivity  
- `curl http://url` → Fetch URL data  
- `wget http://url` → Download file  
- `ss -tulnp` → Show open ports  

---

## 7. Archiving & Compression
- `tar -cvf files.tar dir/` → Create tar archive  
- `tar -xvf files.tar` → Extract tar archive  
- `zip files.zip file1 file2` → Create zip file  
- `unzip files.zip` → Extract zip file  

---

## 8. Automation with Cron
- `crontab -e` → Edit cron jobs  
- `crontab -l` → List jobs  
- `* * * * * /path/script.sh` → Run script on schedule  

---

## 9. File Transfer & Sync
- `scp file user@host:/path` → Copy file to remote  
- `rsync -avz dir/ user@host:/path` → Sync files  
