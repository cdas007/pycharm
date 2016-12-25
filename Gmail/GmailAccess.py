__author__ = 'chiranjitdas'

import imaplib
import sys
import getpass
import email
import email.header
import datetime

""" Program to get information from the gmail account and entry it into the database"""

""" defining variables"""
email_account = "cdasieee@gmail.com"
email_folder = "Inbox"

def process_mailbox(M):
    