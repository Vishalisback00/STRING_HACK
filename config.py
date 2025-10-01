# TEAM PURVI ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "2649377"
    API_HASH = "6586f0276c7748e5468719bdd247d90"
    TOKEN = "8451532457:AAHEaV8KH62pLUoFmnWXoHiMVfkPILIYhU"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://aarbhakar302:effOLpfZ0awCjQxz@cluster0.byhbxty.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://files.catbox.moe/o9bo13.jpg"
    SUDOERS = filters.user(["799634470"])
