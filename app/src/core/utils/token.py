import asyncio
import string
import secrets


async def get_token(length: int = 7) -> str:
    def token(length: int) -> str:
        return "".join(
            secrets.choice(string.ascii_letters + string.digits)
            for _ in range(length)
        )

    result = await asyncio.to_thread(token, length)
    return result


async def get_token_from_url(url: str) -> str:
    def token(url: str) -> str:
        return url.strip().split('/')[-1]

    result = await asyncio.to_thread(token, url)
    return result
