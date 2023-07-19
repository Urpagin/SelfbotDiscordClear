"""discord module is from `discord.py-self` not discord.py"""
from typing import AsyncGenerator

import discord
from discord.ext import commands

bot: discord.ext.commands.bot.Bot = commands.Bot(command_prefix='!', self_bot=True)


async def get_message(ctx: discord.ext.commands.Context,
                      amount: int, links: bool) -> AsyncGenerator[discord.Message, None]:
    """
    Generator that gets your own messages in a channel
    :param ctx: Used to get the channel history
    :param amount: The amount of messages you want to get. If amount is negative returns all msgs.
    :param links: If set to true only gets messages containing links
    :return: A message of type *discord.Message*
    """
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
        count += 1
        yield message


@bot.command()
async def clearr(ctx: discord.ext.commands.Context, amount: int = 0, links: bool = False) -> None:
    """
    Command listener for *clearr*
    :param ctx: The context
    :param amount: The amount of messages the user wants deleted. Negative means all
    :param links: If set to true only gets messages containing links
    :return: None, deletes the user's messages
    """
    if ctx.me.id != bot.user.id:  # Only owner can interact
        return
    await ctx.message.delete()
    if not amount:
        await ctx.send(
            '# :tools: How to use :tools:\n- `!clearr <amount> <links>`\n'
            '  - `<amount>`: (integer) the amount of own messages to delete\n'
            '  - `<links>`: (boolean) if true, deletes only messages containing links\n'
            '# :scroll: Examples :scroll:\n'
            '- `!clearr 10 1` will delete 10 of your messages containing links\n'
            '- `!clearr -1` will delete ALL of your messages (may take a long time)', silent=True
        )
        return

    # I chose not to use `ctx.channel.delete_messages()` as it does not work in DMs
    # and in the module is the same as `message.delete()` just with a for loop
    count = 0
    async for message in get_message(ctx, amount, links):
        await message.delete()
        count += 1

        print(f'Deleted {count}/{"all" if amount < 0 else amount} messages.'
              f' (note that `{"all" if amount < 0 else amount}` is theoretical)')

    print(f'---- Task done, deleted {count} {"message" if count == 1 else "messages"} ----')
    await ctx.send(f':saluting_face: Deleted `{count}` of your messages.',
                   delete_after=5, silent=True)


if __name__ == '__main__':
    while True:
        token: str = input('Enter your Discord token: ').replace('"', '').strip()
        if token:
            break

    bot.run(token)
