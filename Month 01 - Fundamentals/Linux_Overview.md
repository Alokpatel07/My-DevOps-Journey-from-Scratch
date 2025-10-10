# 🐧 Linux for DevOps – Quick Guide
  
This README is a **practical Linux guide** tailored for DevOps learners and practitioners.  
Instead of overwhelming you with everything, it focuses on the **most useful commands and concepts** you’ll actually need in real-world DevOps work.  

---

## 1. 🚀 Getting Started – Basic Commands
These are the everyday commands you’ll use to interact with the system.  

- `pwd` → Shows where you are (current directory).  
- `whoami` → Tells you which user you’re logged in as.  
- `date` → Prints system date and time.  
- `clear` → Cleans up the terminal for a fresh start.  
- `history` → Lists all previously used commands (great for debugging mistakes).  
- `man <command>` → The built-in manual for any command.  

💡 *Tip: When in doubt, try `man` or `<command> --help`.*  

---

## 2. 📂 File & Directory Management
Everything in Linux is a file — knowing how to handle them is core.  

- `ls` → Lists files and directories.  
  - `ls -l` = detailed info  
  - `ls -a` = includes hidden files  
- `cd folder/` → Move into a directory.  
- `touch file.txt` → Create a new empty file.  
- `mkdir project` → Make a new directory.  
- `cp file1 file2` → Copy a file.  
- `mv old.txt new.txt` → Rename/move files.  
- `rm file.txt` → Delete a file (⚠️ careful).  
- `cat file.txt` → Show file contents at once.  
- `less file.txt` → Open file for scrolling.  
- `head -n 5 file.txt` → First 5 lines of a file.  
- `tail -f logfile.log` → Watch logs live in real-time.  

💡 *Tip: Combine commands with `|` (pipe). Example: `cat logfile.log | grep ERROR`*  

---

## 3. 🔑 Working with `sudo` (Superuser Privileges)
Some operations need admin rights. That’s where `sudo` comes in.  

- `sudo <command>` → Run a command with superuser rights.  
- `sudo su` → Switch into the root user account.  
- `sudo apt update && sudo apt upgrade` → Update & upgrade (Debian/Ubuntu).  
- `sudo yum update` → Update system (RHEL/CentOS).  
- `sudo reboot` / `sudo shutdown -h now` → Restart or power off the machine.  

⚠️ *Be extra cautious with `sudo`. A wrong command can break the system.*  

---

## 4. 🌐 Networking Essentials
As a DevOps engineer, you’ll often debug servers and connectivity.  

- `ip a` → Show network interfaces (modern replacement for `ifconfig`).  
- `ping google.com` → Test internet connectivity.  
- `curl <url>` → Fetch data from a URL (great for APIs).  
- `wget <url>` → Download a file.  
- `ssh user@host` → Connect to another server.  
- `scp file.txt user@host:/path` → Copy file to/from remote server.  
- `ss -tulnp` → Show open ports and listening services.  
- `nslookup example.com` / `dig example.com` → DNS checks.  

💡 *Tip: If a website isn’t loading, try `ping`, then `curl`, then check ports with `ss`.*  

---

## 5. 💽 LVM – Logical Volume Management
For handling storage dynamically. Super handy when managing servers.  

- **Step 1: Identify disks**  
  - `lsblk` or `fdisk -l`  

- **Step 2: Create Physical Volume (PV)**  
  - `pvcreate /dev/sdb`  
  - `pvdisplay`  

- **Step 3: Create Volume Group (VG)**  
  - `vgcreate vg_data /dev/sdb`  
  - `vgdisplay`  

- **Step 4: Create Logical Volume (LV)**  
  - `lvcreate -L 5G -n lv_data vg_data`  
  - `lvdisplay`  

- **Step 5: Format & Mount**  
  - `mkfs.ext4 /dev/vg_data/lv_data`  
  - `mount /dev/vg_data/lv_data /mnt`  
  - `df -h` (check mounted storage)  

- **Step 6: Cleanup**  
  - `umount /mnt`  
  - `lvremove /dev/vg_data/lv_data`  
  - `vgremove vg_data`  
  - `pvremove /dev/sdb`  

💡 *Think of LVM like a flexible container for disks – it lets you resize storage on the fly.*  

---

## ✅ Final Notes
- Practice is key! Don’t just read commands — run them.  
- Always double-check destructive commands like `rm -rf`.  
- Keep this as a **cheat sheet** while you work on projects.  

---

✨ With this, you’ve got a **Linux foundation strong enough for DevOps**.  
Next stop → Automation, Cloud, and Containers 🚀  

