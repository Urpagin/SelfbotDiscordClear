from typing import AsyncGenerator

import discord.ext.commands
from discord.ext import commands

bot: discord.ext.commands.bot.Bot = commands.Bot(command_prefix='!', self_bot=True)


async def get_message(ctx: discord.ext.commands.Context,
                      amount: int, links: bool) -> AsyncGenerator[discord.Message, None]:
    """Gets the messages in a channel. If `amount` < 0 gets all messages.
     If `links` returns only messages containing links"""
    count = 0
    async for message in ctx.channel.history(limit=None):
        if count == amount:
            return
        if message.author != ctx.author:
            continue
        if links:
            if 'http://' in message.content or 'https://' in message.content:
                count += 1
                yield message
            continue
        else:
            count += 1
            yield message


async def delete_messages(messages: list[discord.Message, ...]):
    count = 0
    for message in messages:
        await message.delete()
        count += 1


@bot.command()
async def clearr(ctx: discord.ext.commands.Context, amount: int = 0, links: bool = False):
    if ctx.me.id != bot.user.id:  # Only owner can interact
        return
    await ctx.message.delete()
    if not amount:
        await ctx.send('# :tools: How to use :tools:\n- `!clearr <amount> <links>`\n'
                       '  - `<amount>`: (integer) the amount of own messages to delete\n'
                       '  - `<links>`: (boolean) if true, deletes only messages containing links\n'
                       '# :scroll: Examples :scroll:\n'
                       '- `!clearr 10 1` will delete 10 of your messages containing links\n'
                       '- `!clearr -1` will delete ALL of your messages (may take a long time)', silent=True)
        return

    count = 0
    async for message in get_message(ctx, amount, links):
        await message.delete()
        count += 1

        print(f'Deleted {count}/{"all" if amount < 0 else amount} messages.'
              f' (note that `{"all" if amount < 0 else amount}` is theoretical)')

    print(f'---- Task done, deleted {count} {"message" if count == 1 else "messages"} ----')
    await ctx.send(f':saluting_face: Deleted `{count}` of your messages.', delete_after=5, silent=True)


if __name__ == '__main__':
    while True:
        token: str = input('Enter your Discord token: ').replace('"', '').strip()
        if token:
            break

    bot.run(token)
