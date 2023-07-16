import discord.ext.commands
from discord.ext import commands

bot: discord.ext.commands.bot.Bot = commands.Bot(command_prefix='!', self_bot=True)


@bot.command()
async def clearr(ctx: discord.ext.commands.Context, amount: int = 0, links: bool = False):
    if ctx.me.id != bot.user.id:  # Only owner can interact
        return
    if not amount:
        await ctx.send('Please specify integer argument `amount` of messages to delete. `!clearr <amount> <links>`')
        return

    messages = []
    async for message in ctx.channel.history(limit=None):
        if len(messages) == amount + 1:  # +1 to delete sent command msg
            break
        if message.author == ctx.author:
            if links:
                if 'http://' in message.content or 'https://' in message.content:
                    messages.append(message)
                continue
            messages.append(message)

    try:
        await ctx.channel.delete_messages(messages)
        return
    except Exception as e:
        print(e)
        for msg in messages:
            await msg.delete()

    await ctx.send(f'Deleted {len(messages) - 1} of your messages.', delete_after=5)


if __name__ == '__main__':
    while True:
        token: str = input('Enter your Discord token: ')
        token = token.replace('"', '').strip()
        if token:
            break

    bot.run(token)
