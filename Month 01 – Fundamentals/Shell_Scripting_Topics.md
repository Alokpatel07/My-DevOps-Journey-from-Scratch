# Shell Scripting for DevOps

## Overview
Shell scripting is a key DevOps skill to automate tasks, manage servers, monitor systems, and integrate with CI/CD pipelines.

---

## Essential Commands

### File & Directory
- `ls -l` → List files with details  
- `pwd` → Show current directory  
- `cd ..` → Move back one directory  
- `mkdir dir` → Create directory  
- `rm -rf dir` → Remove directory and contents  
- `touch file` → Create empty file  

### File Permissions
- `chmod 755 script.sh` → Change file permissions  
- `chown user:group file` → Change ownership  

### Text Processing
- `cat file.txt` → Show file content  
- `grep "error" log` → Search text in file  
- `awk '{print $1}' file` → Print first column  
- `sed 's/foo/bar/g' file` → Replace text  

### System Monitoring
- `top` → Show running processes  
- `ps aux` → List all processes  
- `df -h` → Check disk usage  
- `free -h` → Check memory usage  
- `uptime` → Show load average  

### Networking
- `ping google.com` → Test connectivity  
- `curl http://url` → Fetch URL data  
- `wget http://url` → Download file  
- `ss -tulnp` → Show open ports  

### Archiving & Compression
- `tar -cvf file.tar dir/` → Create tar archive  
- `tar -xvf file.tar` → Extract tar archive  
- `zip file.zip file1 file2` → Create zip file  
- `unzip file.zip` → Extract zip file  

### Automation (Cron Jobs)
- `crontab -e` → Edit cron jobs  
- `* * * * * /path/script.sh` → Run every minute  

### File Transfer
- `scp file user@host:/path` → Copy file to remote  
- `rsync -avz dir/ host:/path` → Sync files  

---

## Example Script
```bash
#!/bin/bash
echo "System Health Check"
uptime
df -h | grep '^/dev/'
free -h
