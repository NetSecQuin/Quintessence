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

``` /var/
