# security_task
A security task for an job interview, in Python

https://www.mbd.hu/uris/readme.txt

A random remote service keeps publishing a set of URIs to this WEB location (right next to this little text file), in random time intervals, as follows:
Each time it places the list of URIs in a text file and publishes it zipped, password protected, in a folder which name was generated from timestamp when it was created, in YYYY_MM_DD_hh_mm_ss form. When a new set is published, the previous one is removed (in other words, only one set is published at a time).
The password to the zip file is always the file/directory creation time of the _previous_ URI set, in epoch time format (UTC time).
Whether the URIs are valid or active, or safe to visit, reoccurring or not, it's not guaranteed. However, the most often reoccurring URI of the URI sets, is safe to visit an contains a message.
If you managed to find this message, send it back to us in email, to the colleague you received this exercise from. ;)
Remember, this is a programming and not a hacking/cracking excercise. Try to use a programming language you think that suits to this problem the most. Should you have any questions, don't hesitate to ask ;)
