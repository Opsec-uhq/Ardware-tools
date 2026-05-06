# Copyright (c) 2026 Opsec-Ardware-Tools
# Non-commercial use only

from Plugins.Utils import *
from Plugins.Config import *

import requests
from datetime import datetime, timezone

try:
    Title("Feedback")
    Scroll(GradientBanner(feedback_banner))

    # 🔴 Mets ton webhook dans une variable d’environnement ou config
    WEBHOOK_URL = "https://discord.com/api/webhooks/1498751284075827301/SKQ5FSC0MM0Rvd606412cAH_r048ORotCiLmZGNVcawK4KBDIHxbdgehZzcnfUgOsJ7F"

    # 🖼️ Icon personnalisée
    CUSTOM_ICON = "https://cdn.discordapp.com/attachments/1497224622360363019/1498743311551430830/e37ff27d2697b8dacbc4d3a44c64c3aa.png?ex=69f244fa&is=69f0f37a&hm=fd07b2410cad1dbd95ea08940fc2e6911a07b9fb4d190a68f6adf6812c331471&"

    Connection()

    ratings = {
        "01": 1, "02": 2, "03": 3, "04": 4, "05": 5,
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    }

    Scroll(f"""
 {INFO} Rate your experience!

 {PREFIX1}01{SUFFIX1} 1/5
 {PREFIX1}02{SUFFIX1} 2/5
 {PREFIX1}03{SUFFIX1} 3/5
 {PREFIX1}04{SUFFIX1} 4/5
 {PREFIX1}05{SUFFIX1} 5/5
""")

    choice = input(f"{INPUT} Rating {red}->{reset} ").strip()

    if choice not in ratings:
        ErrorChoice()

    rating = ratings[choice]

    message = input(f"{INPUT} Message {red}->{reset} ").strip()

    if not message:
        ErrorInput()

    print(f"{LOADING} Sending..", reset)

    # 🛡️ Safe variables
    username = username_pc or "unknown"
    platform = platform_pc or "unknown"
    version = version_tool or "unknown"

    # ✉️ Discord embed
    embed = {
        "title": "New Feedback!",
        "color": color_embed,
        "thumbnail": {"url": CUSTOM_ICON},
        "fields": [
            {"name": "Rating", "value": f"```{rating}/5```", "inline": True},
            {"name": "Username", "value": f"```{username}```", "inline": True},
            {"name": "Platform", "value": f"```{platform}```", "inline": True},
            {"name": "Version", "value": f"```{version}```", "inline": True},
            {"name": "Message", "value": message[:1000], "inline": False},
        ],
        "footer": {
            "text": name_tool,
            "icon_url": CUSTOM_ICON,
        },
        "timestamp": datetime.utcnow().isoformat()
    }

    payload = {
        "username": f"{username_webhook} | Feedback",
        "avatar_url": CUSTOM_ICON,
        "embeds": [embed]
    }

    response = requests.post(WEBHOOK_URL, json=payload, timeout=10)

    # 🔍 Debug
    if response.status_code in [200, 204]:
        print(f"{SUCCESS} Feedback sent!", reset)
    else:
        print(f"{ERROR} Could not send feedback! ({response.status_code})", reset)
        print(response.text)

    Continue()
    Reset()

except Exception as e:
    Error(e)