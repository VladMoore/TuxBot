import discord
from discord.ext import commands
import requests

class randCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rand(self, ctx,*args):
        #help:  embed=discord.Embed(title="Usage: RanInt#",url="https://qrng.anu.edu.au/", description="This command functions similar to how the RanInt# function works on a standard scientific calculator. However this uses quantum computing to generate 'true' random integers (Learn more in title): \n\n•Requires you to provide a length for the array.\n•Requires a data type, the data type must be ‘uint8’ (returns integers between 0–255), ‘uint16’ (returns integers between 0–65535) or ‘hex16’ (returns hexadecimal characters between 00–ff).", color=discord.Color.blue())
        if len(args) < 2:
           embed=discord.Embed(title="Error: Missing Args!",description="**You are missing the following arguments in order**: \n    • **Length** of the array\n  • **Data Type**, the data type must be ‘uint8’ (returns integers between 0–255), ‘uint16’ (returns integers between 0–65535) or hex16 (note with hex16 you need to provide a block size).", color=discord.Color.red())
           await ctx.send(embed=embed)
        elif not args[0].isnumeric():
            embed=discord.Embed(title="Error: Incorrect Values!",description=f"You inputted `{args[0]}` which is not a number, you must provide an array **length** Please try again.", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif args[1] not in ['uint16','uint8','hex16']:
            embed=discord.Embed(title="Error: Incorrect Values!",description=f"You inputted `{args[1]}` which is not an accepted **data type**, you must include either: **Uint16**, **Uint8** or **Hex16**", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif args[1] == "hex16":
            if len(args) == 2:
                embed=discord.Embed(title="Error: Missing Arg!",description="You are missing a `Block Size` (Note: with Hex16 you must provide a length for a block. An example of one block is `3e`, two blocks would be `62b2`, so on).", color=discord.Color.red())
                await ctx.send(embed=embed)
            elif not args[2].isnumeric():
                embed=discord.Embed(title="Error: Incorrect Values!",description=f"You inputted `{args[2]}` which is not a number, you must provide a `Block Size` Please try again.", color=discord.Color.red())
                await ctx.send(embed=embed)
            else:
                api =  f'https://qrng.anu.edu.au/API/jsonI.php?length={args[0]}&type={args[1]}&size={args[2]}'

                json_data = requests.get(api).json()
                success = json_data['success']

                if success == True:
                    data = json_data['data']
                    await ctx.send(f'{data}')


        else:

            api =  f'https://qrng.anu.edu.au/API/jsonI.php?length={args[0]}&type={args[1]}'

            json_data = requests.get(api).json()
            success = json_data['success']

            if success == True:
                data = json_data['data']
                await ctx.send(f'{data}')

def setup(bot):
    bot.add_cog(randCog(bot))