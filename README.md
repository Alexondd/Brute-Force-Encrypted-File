# Context for this project

An attacker was able to exploit a vulnerability on an affected server and began installing a ransomware virus. Luckily, the Incident Detection & Response team was able to prevent the ransomware virus from completely installing, so it only managed to encrypt one zip file. 
Internally, the Chief Information Security Officer does not want to pay the ransom, because there isn’t any guarantee that the decryption key will be provided or that the attackers won’t strike again in the future. 
Instead, I’m assigned the task to brute force the decryption key. Based on the attacker’s sloppiness, this isn’t expected to be a complicated encryption key, because they used copy-pasted payloads and immediately tried to use ransomware instead of moving around laterally on the network.

# Task

In this task, I will write a Python script to brute force the decryption key of the encrypted file.
Brute forcing is the act of repeatedly trying different combinations to break the password encryption (based on either randomly generated passwords, or from a list of passwords to try). A small subset of passwords from Rockyou - a widely know password wordlist that contains thousands of common passwords in one wordlist has been provided for this task.
Ransomware will often encrypt all files on a device, and sometimes give the decryption key after the ransom has been paid (but this is not always the case!). In this task, I will break the encryption without paying the ransom.

# How to use this script

1. **Prepare Your Files**
  - Create or download the "rockyou.txt" file containing a list of possible passwords.
  - Have your encrypted ZIP file named 'enc.zip'.

2. **Save and run the script**
  - Save this script as 'crack_zip.py'.
  - Run it using Python from your command-line interface.

3. **Check the output**
  - The script will try each password and let you know if it finds the correct one.

Feel free to use or modify this script for your needs, and always ensure you have the right to access and crack the ZIP files you work with.   
