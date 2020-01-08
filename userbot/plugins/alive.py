""".admin Plugin for @XtraTgBot"""
import asyncio
from telethon import events
from telethon import version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname, python_version

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("dis @XtraTgBot\n\n"
                     f"Telethon version: {version.__version__} \n"
                     f"Python version: {python_version()} \n"
                     f"`me`: {DEFAULTUSER} \n"
                     )
