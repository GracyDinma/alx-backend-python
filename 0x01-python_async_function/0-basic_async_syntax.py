#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This coroutine waits for a random float value between 0 and max_delay
    and returns that value.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
