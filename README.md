# Database Encryption

## Setup
To Use this file you will need to download a few dependencies.
1) You will need to download pysqlcipher which can be found here --> https://github.com/leapcode/pysqlcipher
- You may need to use pysqlcipher3 depending on your version of python

## How to Run (See Video Demonstation here-->

Copy the code and run each method one at a time.
1) The first method will create a database called Balance.db which is an SQLite database. You will need to pass it some data.
2) Next your can use the readPT method to read the plaintext database
3) You can then use the encrypt function to encrypt the database. Be sure to define a key in the secrets.py file
4) Last you can read your encrypted database by passing the key as 'PRAGMA KEY'
5) To see terminal commands please review the video above
