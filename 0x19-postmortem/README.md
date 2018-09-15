# Postmortem

**Issue Summary**

The date was a sunny morning (the morning of 9/11/18). Our web server (Apache) stops working from about 12:00pm to 12:35pm (PDT). What could’ve went wrong? I try to curl our localhost (127.0.0.1) with the -s (silent) and -I (headers only) option and all I get returned is a HTTP /1.0 500 internal server error. Users could no longer access the webpage because the web server is down. 100% of users are now affected by this. The root cause of this is that Apache contained some mislabeled files in our web server which cause it to crash.

**Timeline:**

12:00 pm - The issue was detected via an email notifying us that our website was down.

12:05 pm - I try to curl our local host (127.0.0.1) with the -s (silently) and -I (headers only) options but I all get returned is a 500 internal server error. This confirms that we could not reach our web server and that we have an issue.

12:06 pm - I use `top` to see the current running processes to see if our web server is down. It shows us our web server apache being run from root (PID -45) and www-data (PID -54). At this point, I am not sure where the issue lies.

12:07 pm - I use a program called `strace` while attaching the PID (process identifier) for the root. From this point, it returns a continuous timeout response.

12:08 pm - I open another terminal and ssh into our server. I curl our localhost and get nothing.

12:10 pm - I figure that wasn’t the issue and so I try to strace our www-data PID. This instead wait’s for a response for me to curl in another tab.

12:12 pm - When I curl this time I get a big error response in the terminal window where I was using the program `strace`. From here I take my time looking through the error response until I am able to find an issue or an error (an error shows up as -1 within strace).

12:18 pm - I notice some `.phpp` files with a -1 error returned after it. An example of a line of code I noticed:  (lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7fff3fa0f610) = -1 ENOENT (No such file or directory)).

12:19 pm - This is new to me and so I try to see if `.phpp` was a certain extension but then I realized it was a typo and it should’ve actually been `.php`.

12:20 pm - After noticing that this should be changed I go to the directory where everything for wp (wordpress) is located. 

12:22 pm - After looking through this directory I locate a module called `wp-settings.php` which will let me configure all of wp’s settings. 

12:30 pm - Realizing I could substitute all of the .phpp typos to .php using sed and some puppet script, I opt for this route. Our puppet script will execute the command `sed -i 's/.phpp/.php/g'` on the file /var/www/html/wp-settings.php. (the path for the command sed is located in /bin and must be specified)

12:35 pm - After developing and running the puppet script, I try to curl -sI our localhost (127.0.0.1) again and get a working response. Our issue is now resolved.



**Root cause and resolution:**

*Root cause:*

The cause of the issue was that their were some wordpress files with the wrong extension. They ended with the .phpp extension instead of the .php extension which was not allowing Apache (our web server) to be run. 

*Resolution:*

By replacing all of the wrong .phpp extensions with the proper .php extension (within our wp-settings), we were able to get get our web server up and running again. The technologies used were top (to list all processes), strace (this helped us detect where our error lied), sed (this replaced all .phpp extensions), and puppet (this enables us to automate our script to do it again in case of this same error).


**Corrective and preventative measures:**

Things that we could to prevent this from happening again would be to remember to check file extension names while working within the server (all the time actually) and to always check if the server is up and running after work is done to it.
We have a puppet script to fix this issue in case another issue like this ever arises.
