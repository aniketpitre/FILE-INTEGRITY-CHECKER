File Integrity Checker-

This is a Python script that generates and checks the integrity of files in a specified directory using SHA-256 hashes.

Features- 

Generate SHA-256 hashes for all files in a directory.

Save the hashes to file_hashes.json.

Check for modifications, new files, or missing files.

Requirements-

Python 3.x

Usage

Run the script:

python app.py



Enter the directory path to monitor.

Choose an action:

generate to generate and save hashes.

check to compare current files with saved hashes.

Example

Enter the directory path: sample-dir\
Generate new hashes or check files? (generate/check): generate
Hashes generated and saved.

Enter the directory path: sample-dir\
Generate new hashes or check files? (generate/check): check
[MODIFIED] The following files were changed:
 - sample-dir\sample.txt
 - sample-dir\sample1.txt

Files

app.py: Main script for hash generation and verification.

file_hashes.json: Stores the hash values.



