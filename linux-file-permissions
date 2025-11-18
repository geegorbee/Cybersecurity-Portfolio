Managing File Permissions in Linux

A practical demonstration of least privilege, access control, and secure file handling

Project Overview

This project focuses on reviewing and updating file and directory permissions within a Linux environment to ensure that sensitive research files are only accessible to authorized users. I examined existing permissions using standard Linux commands, identified overly permissive configurations, and applied targeted updates to enforce the principle of least privilege.


The tasks performed include:

Checking permissions on all files and directories in a working folder

Interpreting permission strings and identifying risk

Updating file permissions to remove unnecessary write access

Securing a hidden file

Restricting directory access to a single authorized user

Verifying all applied changes



This project demonstrates foundational Linux security skills relevant to real-world system administration and cybersecurity roles.


1. Checking File and Directory Details
I first inspected the existing permissions for all items in the projects directory:

ls -la

Using the -la flags provides a detailed listing, including ownership, access rights, and hidden files (those beginning with .). The results revealed a hidden file .project_x.txt, multiple project files, and the drafts directory. Reviewing these attributes allowed me to spot files with permissions that were too permissive for the research environment.

 
2. Understanding the Permission String
Each entry in the directory listing includes a 10-character permissions string that describes how the file or directory can be accessed.

The first character indicates type (d for directory, - for file).

The next three groups of three characters define permissions for:

the owner,

the group,

and other users.



For example:

drwxr-x---

This tells us the owner has full access (read/write/execute), the group has read and execute rights, and all other users are denied access.



Understanding these structures was essential for deciding where updates were needed.
 
3. Changing File Permissions on a Hidden File
The hidden file .project_x.txt contained archived information that should not be modified. The research team asked for it to be readable by the appropriate users but protected from changes.

I updated its permissions with:

chmod u-w,g-w,g+r .project_x.txt

This removed write access from both the owner and group while ensuring the group maintained read access. I then confirmed the update with ls -la.



This prevents accidental or unauthorized alterations while keeping the file accessible for reference.


4. Updating Permissions on Project Files
Several project files allowed broader write access than necessary. To reduce the risk of data tampering, I restricted them so that:

the owner can read and write

the group can read

others cannot access the file

Example commands:

chmod 640 project_k.txt
chmod 640 project_m.txt
chmod 640 project_r.txt
chmod 640 project_t.txt

This ensures research data remains intact and traceable to its owner.


5. Changing Directory Permissions
The drafts directory contained early research notes that only researcher2 should be able to access. To prevent group members from entering the directory, I removed the execute bit from the group:

chmod g-x drafts

Execution permissions control a user’s ability to enter and navigate a directory. Removing this bit restricts access while maintaining the owner’s full control. I validated the change using ls -la.


6. Security Impact
By tightening permissions across these files and directories, I:

Reduced unnecessary write access

Prevented unauthorized entry into sensitive directories

Protected archived content from modification

Ensured team members can only access what aligns with their role

Applied the principle of least privilege consistently

Improved system integrity and minimized potential attack surface



These types of permission updates represent common hardening tasks performed in real Linux environments.

Tools and Commands Used
ls -la

chmod (symbolic and numeric modes)

Linux permission model (r, w, x)

Hidden file handling

Directory execution restrictions


Security+ / Google Cybersecurity Alignment

This project reinforces key concepts required for both Google Cybersecurity and CompTIA Security+ SY0-701:

Access control models (1.3)
File system permissions
System hardening (3.3)
Secure configuration (3.1)
Least privilege (2.1, 3.1)


What I Learned
How to interpret and modify Linux file permissions
How execution rights affect directories
How to secure hidden files
How to limit access for different user types (owner, group, others)
How to verify permission changes effectively



