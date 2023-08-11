# Linux Live Image Forensics Cheatsheet

### Interesting Files/FilePaths

#### Accounts

``` /home/* ``` - view user accounts visable to the user you are logged in as

``` /etc/passwd ``` All accounts on the machine (system and user)

``` /etc/sudoers ``` Accounts with the permission to use sudo (superuser)

Some commands to narrow down /etc/passwd to specific account types

``` cat /etc/passwd | grep -v false ``` -

``` cat /etc/passwd | grep -v nologin ``` - 

``` cat /etc/passwd | grep -v false | grep -v nologin ``` - display on user accounts

##### Authentication log 

``` /var/log/auth.log ```

There are usually a number of gzipped auth log files stored on the machine as well. ``` gunzip auth.log* ``` will unzip them.

Ater all auth.log files are unzipped, you can use ``` cat /var/log/auth.log ``` to query them all at once. 

This will list a ton of CRON job authentication events if CRON is running. 

If you only want to see authentication events not preformed by a CRON job, you can use ``` cat /var/log/auth.log* | grep -v cron ```

###### Command History

Depending on OS the history files may be found in these directories

``` /var/log/history.log ```

``` /var/log/history/history.log ```

``` /home/*/bash_history ```

There may also be gzipped history.log files in the /var/log directory, unzip these with guzip

##### Syslog

``` /var/log/syslog ``` - System processes and application logs

##### 3rd party application logs 

Installed applications typically will either use the /var/log directory as a dump point for their logs, or create a folder there for logs. 


``` /var/log/* ```

### Persistance

Malware and threat actors may attempt multiple methods of persistance. These persistance mechanism work best in places where the script can be automatically or scheduled to be run. 

###### Cron

Cron jobs are basically scheduled tasks and depending on what Cron folder a script is written to, will determine the frenquency of it being run. Cron jobs can be investigated at the following paths.

``` /etc/crontab/* ```
``` /etc/cron.d/* ```
``` /etc/cron.daily/* ```
``` /etc/cron.weekly/* ```
``` /etc/cron.monthly/* ```
``` /etc/cron.yearly/* ```

###### Services

Malware or backdoors can be installed as a service in order to evade detection as they are in a constant loaded state. The services installed on a host can found in the following directory:

``` /etc/init.d/* ```

###### BashRC Scripts

Malicious scripts can be set to autorun at a user level. If the user has root permissions, the script may still be run as root in this location. BashRC scripts are located in each of the users hoem directories and are hidden files by default. In order to see them you would need to run ``` ls -lah ``` - to list all hidden. They are located at

``` /home/*/.bashrc ```

``` /etc/.bashrc ```

##### Live Analysis Commands

List all processes then view details regarding a specific process

```
ps auxfww
lsof -p [pid]
```

List all services currently running

``` service --status-all ```

Show detached and running screen sessions

``` screen -list ```

##### Network Analysis

List all network connections, then view details regarding what process is responsible for the connection 

```
netstat -a
lsof -p [pid]
```

##### File Analysis

Search for all files that are a specifc filetype

``` find . -type f -iname "*.sh" ```

Calculate the hash of a file. Example is in sha256

``` sha256sum /home/user/test.sh ```

Last edit time of a file 

``` ls -lah | grep filename.txt ```

View the human readable strings of a file

``` strings filename.txt ```
