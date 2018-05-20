---
title: Portable Work Environment
header-includes:
    <link href="styles.css" rel="stylesheet"/>
---

## Purpose

The purpose here is to create a snapshot of a work
environment in one computer and restore it in different computers
with minimum configuration. This is useful when the main computer
is offline, corrupted or crashed. The options below are some of
the things one can do with available and new tools.

## Backup

A full backup of the system is of course a no-brainer. But the
questions that trouble beginners and even experts are as follows

a) When and how often to perform backup?
b) How can this be automated?
c) How much the process should be automated (full vs partial vs
manual backups, full automation may not be desired in many cases)
d) How to perform intelligent backups - that preserves both
important data and at the same time saves space?
e) What are the best tools for backup?

Backups can be done at various levels. We will start with the
most detailed and then more smarter options that can save space while
maintaining data integrity

## Bare Metal Backup

This is done through tools like
[Clonezilla][1] which allows one to backup a hard drive
block by block. 

Pros:

- Safest option, backs up whole partitions which can be restored to their
previous state
- Works with any OS (for example Windows)
- Offers an integrity test of both source and destination during backup which
can be fixed

Cons:

- Time consuming full backup can take anywhere from 2-10 hours
- Space grabbing, does not support incremental backups so each backup takes the
same time as before
- Not completely beginner level requires knowledge of partitions and disk
checking (the manual is helpful)

## Full System Backup (aka tarballs)

Since in Unix [everything is a file][2] so backups should be
as easy as just tarballing the whole root directory. However this is not often
that straightforward. Special things to consider are of course the boot leader
and the system specific details (if restored on a different computer). This
[link][3] provides an excellent guide on how to do this. The essential command
can be summarized as below.

~~~bash
sudo tar czf /backup.tar.gz --exclude=/backup.tar.gz --exclude=/home \
--exclude=/media --exclude=/dev --exclude=/mnt --exclude=/proc --exclude=/sys \
--exclude=/tmp / 
~~~

More/less `--exclude` options can be chosen if necessary. To install bootloader
one can use the set of commands below (described [here][4]) from a live PC (usb
or cd).

~~~bash
#If there is no separate boot partition
sudo mount /dev/DEVICENAME_FROM_STEP_ONE /mnt
sudo rm -rf /boot    # Careful here, make sure YOU ARE USING THE LIVE CD. I tried it, it works.
sudo ln -s /mnt/boot /boot
#If there is a separate boot partition
sudo mount /dev/DEVICENAME_FROM_STEP_ONE /boot
#Install boot loader
sudo apt-get update
sudo apt-get install grub-pc
sudo grub-install /dev/sda     # NOTE THAT THERE IS NO DIGIT
sudo umount /boot
~~~

## Data Backup (Rsync and Rsnapshot)

The best available tool to reliably backup data in a unix system is rsync. It is
incredibly powerful, intelligent and works across a variety of platforms. The
pros and cons are as below

Pros

- Incremental backup so each time `rsync` knows exactly how much to backup from
  source to destination
- Copies file based on their timestamps so a file will only be overwritten if
it is the newer version in the source
- Works across everything and by that I mean EVERYTHING internal and external
  local devices, across networks in different servers
- Highly configurable through various options

Cons

- Too many options often overwhelming to a beginner
- The commonly used option `-a` may not be what you want in certain cases
  especially when dealing with sources and destinations with different
  permissions
- Dependence on ssh could be a handicap when transferring file across network
  (explained later)
  
[Rsnapshot][5] allows one to automate backups using rsync and crontabs. In
particular one can configure which locations to sync and how often. More details
are available on the website. This tool is based on this [blog][6]

## Virtualization

PC virtualization offers another way of creating easy and portable work
environments which can be used in different platforms. Some
examples of tools offering virtualization are [Virtual Box][7],
[Vagrant][8] and [Vmware][9]

Pros

- Allows to create an isolated environment tailored for specific projects with
  both os and application specific configurations
- Very useful in collaboratio, software testing and creating
  tutorials for applications to ensure everyone is using the same
  environment
- Backups can be made instantly and when necessary

Cons

- Not every PC supports virtualization
- Can be put a significant strain on system resources
- Not suitable for high performance computation

More lightweight applications such as [docker][10] and system
specific virtual environments such as [virtualenv][11] in python
may be more suited to many applications.

## Network Protocols

`ssh` is the de facto standard when it comes to transferring files securely
between different machines over the network. Utilities like `rsync` uses ssh for
file transfer over a network. However the ssh server and client configuration
varies across different machines and the transfer is dependent on ip addresses
of the client and server. So it is difficult to automate when the ip address
keeps changing.

A good alternative is [mosh][12] which operates over UDP, uses `ssh` to
authenticate and allows a much smoother operation in remote shells.

[1]: https://clonezilla.org/
[2]: https://en.wikipedia.org/wiki/Everything_is_a_file
[3]: https://ubuntuforums.org/printthread.php?t=35087&pp=10&page=1
[4]: https://askubuntu.com/questions/6317/how-can-i-install-windows-after-ive-installed-ubuntu/6321#6321
[5]: http://rsnapshot.org/
[6]: http://www.mikerubel.org/computers/rsync_snapshots/
[7]: https://www.virtualbox.org/
[8]: https://www.vagrantup.com/
[9]: https://www.vmware.com/
[10]: https://www.docker.com/
[11]: https://virtualenv.pypa.io/en/stable/
[12]: https://mosh.org/
