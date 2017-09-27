# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
`pwd`
`mkdir`
`rm -rf`
`touch foo.txt`
`rm foo.txt`
`mv foo.txt bar.txt`
`ls -a`
`cp bar.txt ../newdir/bar.txt`
`curl`
`grep`

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
`ls`  - list files
`ls -a`  - list all files, including hidden ones
`ls -l`  - list all files in a list with additional information
`ls -lh`  - list all files with additional info and shortens the filesize display
`ls -lah`  - `-a`, `-l`, and `-h` combined
`ls -t`  - sort by time modified
`ls -Glp`  - `-p` will append a `/` to directory names, and `-G` will add colorization


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > My go-to has been `-alt`, but I suppose if I had to pick, I'd throw in `-R` and `-r`

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` basically allows for multiple arguments to be passed (separately) to a single command. For example, say I have a list of files that I want to `grep` through. Instead of individually passing multiple `grep` commands, I can use `xargs grep` and include a list of file names that will run separately.

Two options of doing this is with the `-L` flag and the `-n` flag.

With the `-L` flag, we include a number `n`, and afterwards, `xargs` will treat every `n` number of lines of input as one argument. For example:

`xargs -L 1 grep`
`"foo.txt"`
`"bar.txt"`

The commands above will run grep once for every 1 row of input, in this case `foo.txt` and again for `bar.txt`

The `-n` flag is similar, but instead will treat each standalone input deliminated by the space as an argument. Thus the following will have the same results:

`xargs -n 1 grep`
`"foo.txt" "bar.txt"`

 

