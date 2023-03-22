
import requests
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram.errors import MessageNotModified
from FallenMusic.Modules.func import * 
from asyncio import gather
import httpx
from aiohttp import ClientSession
OPENAI_API = "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"
# Aiohttp Async Client
session = ClientSession()

# HTTPx Async Client
http = httpx.AsyncClient(
    http2=True,
    timeout=httpx.Timeout(40),
)

async def get(url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def head(url: str, *args, **kwargs):
    async with session.head(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def multiget(url: str, times: int, *args, **kwargs):
    return await gather(*[get(url, *args, **kwargs) for _ in range(times)])


async def multihead(url: str, times: int, *args, **kwargs):
    return await gather(*[head(url, *args, **kwargs) for _ in range(times)])


async def multipost(url: str, times: int, *args, **kwargs):
    return await gather(*[post(url, *args, **kwargs) for _ in range(times)])


async def resp_get(url: str, *args, **kwargs):
    return await session.get(url, *args, **kwargs)


async def resp_post(url: str, *args, **kwargs):
    return await session.post(url, *args, **kwargs)

@app.on_message(filters.command("ask") & filters.private | filters.group)
async def chatgpt(c: Client, m: Message):
    randydev = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if not randydev:
       await m.reply(f"use command <code>/{m.command[0]} [question]</code> to ask questions using the API.")
       return
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "prompt": randydev,
        "model": "text-davinci-003",
        "temperature": 0.5,
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "top_p": 0.3,
        "frequency_penalty": 0.5,
    }
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await asyncio.sleep(5)
        await c.send_message(m.chat.id, response["choices"][0]["text"], reply_to_message_id=m.id)
    except Exception:
        await c.send_message(m.chat.id, "Yahh, sorry i can't get your answer.", reply_to_message_id=m.id)
