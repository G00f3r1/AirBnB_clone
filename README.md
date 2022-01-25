# AirBnB clone - The console

![hbnb logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220124%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220124T063409Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ff6d78594fb8882093f877e532bc12fff7890b8a4d691e87e57a1d752a1ae27e)



## Execution

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220124%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220124T063409Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b11dd2dba7ad4e4f8bf69d7684bbfa6be48b6ecccaca245b6de0962c28513840)


