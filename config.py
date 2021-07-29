#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://stream.zeno.fm/rcuskc7h208uv")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM
from data import *
class Config:
    ADMIN = SUDO
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = API_ID
    CHAT = CHAT
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    ARQ_API=ARQ_API
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", "Helo ser\n\nIam a Bot to play music, Not to chat with you!")
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    SESSION = SESSION
    playlist=[]
    msg = {}
