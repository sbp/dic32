# Disk integrity checker

> Maps [inodes](https://en.wikipedia.org/wiki/Inode) to file [mtime](https://en.wikipedia.org/wiki/Stat_%28system_call%29) and [CRC32](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) in an [Sqlite3](https://en.wikipedia.org/wiki/SQLite) database

The `dic32` script stores checksums of any files you throw at it in a database. Later you can check that files which have not been updated still have the same checksum. This helps to protect against data corruption.

## Usage

To store the checksums of your home directory:

```sh
dic32 update ~/.dic32.sqlite3 ~/
```
