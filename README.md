# Password Strength Checker

Author: Girdhar

Internship Task 1 - CodeOrbit Tech (Cyber Security Internship)

A simple Python program that checks if a password is strong or weak and tells the user how to improve it.

## Technologies Used

- Python 3 (basic string operations, no external libraries)

## Features

- Length check (minimum 12 characters, 16+ recommended)
- Uppercase, lowercase, number, and special character checks
- Detects easy patterns (1234, abcd), keyboard clusters (qwerty, asdf), and repeated characters (aaa)
- Detects common words, common names, common number clusters, and years
- Detects passphrases (4 or more random words)
- Warns if personal info (name, DOB, pet name) is used in the password
- Warns if the same password is reused
- Rates the password as WEAK, MEDIUM, or STRONG and shows tips to improve it

## Setup Instructions

1. Install Python 3 from https://www.python.org
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run: `python password_checker.py`
5. Enter your details (optional), then type a password to check it. Type `q` to quit.

## Rating System

| Result | Meaning |
|--------|---------|
| STRONG | All checks passed |
| MEDIUM | Most checks passed |
| WEAK | Many checks failed, or a common word / personal info is found |

## GitHub Repository Link

Add your repository link here: `https://github.com/<your-username>/<repo-name>`
