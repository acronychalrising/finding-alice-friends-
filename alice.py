# i had too many notes so i put it into readme.py its not a real readme i promise

import requests # POST requests
from bs4 import BeautifulSoup  # parse html
import time   # for infinite loop delays

homepage = "https://space.galaxybuster.net/lib"
#### target = "alice winchester"
targets = ["alice winchester", "alice", "nour", "castiel"]

# run forever until we find alice (and the others)
while True:

    print("refreshing...")

    # refresh emails
    inbox = requests.get(f"{homepage}/get.php").text 
    soup = BeautifulSoup(inbox, "html.parser")

    # 1. get the inbox preview (from get.php) - pull message list
    emails = soup.find_all("div", class_="row-message")
    found = False

    # search the list of emails
    for email in emails:
        msg_id = email.get("data-id") # 2. parse for message id
        sender = email.find("span", class_="left").text.strip() # from
        subject = email.find("span", class_="right").text.strip() # subject

####        if sender.lower() == target.lower(): # case insensitive
        sender_lower = sender.lower()
        if any(t in sender_lower for t in targets):
            print(f"found ya! (ID {msg_id})")
            print(f"subject: {subject}")

            # 3. call view.php with message id - POST
            data_id = {"id": msg_id}
            message_json = requests.post(f"{homepage}/view.php", data=data_id).json()
            html = message_json[0] # index 0 - html email

            # 4. pull html message body from JSON array
            email_soup = BeautifulSoup(html, "html.parser")
            subject = email_soup.find(id="msgSubject").text.strip()
            sender = email_soup.find(id="msgSender").text.strip()
            body = email_soup.find(id="msgBody").get_text("\n").strip()
            date = email_soup.find(id="msgDate").text.strip()

            # display what we've found
            print("\n--- full message ---")
            print("from:", sender)
            print("subject:", subject)
            print("body:\n", body)
            print("date:", date)
            print("--------------------")

            found = True 
            break

        else:
            print(f"from {sender} :( trying again")

    if found:
        break

    time.sleep(3)  # wait before refreshing

print("\n happy to see you :)")
