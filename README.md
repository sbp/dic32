# Data integrity checker

> Maps [inodes](https://en.wikipedia.org/wiki/Inode) to file [mtime](https://en.wikipedia.org/wiki/Stat_%28system_call%29) and [CRC32](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) in an [Sqlite3](https://en.wikipedia.org/wiki/SQLite) database

The `dic32` script stores checksums of any files you throw at it in a database. Later you can check that files which have not been updated still have the same checksum. This helps to protect against data corruption.

## Usage

To store the checksums of your home directory:

```sh
dic32 update ~/.dic32.sqlite3 ~/
```

## Caution

`dic32` comes with NO WARRANTY, and is untested. You must understand how it works to properly assess what manner of protection it provides. For example, inodes are unique to a volume, so you can't use `dic32` on a backup using a master database file. You'd have to create a new database for the backup.

## Installation

Either download this repository and use the `dic32` script as is:

```sh
git clone https://github.com/sbp/dic32
```

Or use pip3 to install:

```sh
pip3 install dic32
```

## Requirements

`dic32` requires Python 3, with the `sqlite3` module included. Some builds of Python 3 may not include `sqlite3` by default. There is no plan for Python 2 compatibility.
