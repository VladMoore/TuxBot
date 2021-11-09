import discord
from discord.ext import commands
import requests

class randCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ip(self, ctx,*args):
        api =  f'https://ipapi.co/{args[0]}/json/'
        json_data = requests.get(api).json()
        if len(args) < 1:
            embed=discord.Embed(title="Error: Missing Argument!",description=f"You need to provide a valid IP address", color=discord.Color.red())
            await ctx.send(embed=embed)

        elif json_data.get('error'):
            reason = json_data['reason']
            embed=discord.Embed(title="API Error!",description=f"The error message: `{reason}`, was recieved from the API.", color=discord.Color.red())
            await ctx.send(embed=embed)


        else:
            #JSON RESULTS
            countryname = json_data['country_name']
            countrycode = json_data['country_code']
            region = json_data['region']
            regioncode = json_data['region_code']
            city = json_data['city']
            timezone = json_data['timezone']
            utc = json_data['utc_offset']
            org = json_data['org']

            embed=discord.Embed(title=f"IP Lookup for: {args[0]}",color=discord.Color.blue())
            embed.add_field(name='Country', value=f'{countryname} ({countrycode})')
            embed.add_field(name="Region", value=f'region ({regioncode})')
            embed.add_field(name="City", value=f"{city}")
            embed.add_field(name="Timezone", value=f"{timezone}")
            embed.add_field(name="UTC Offset", value=f"{utc}")
            embed.add_field(name="ORG", value=f'{org}')

            await ctx.send(embed=embed)



                







def setup(bot):
    bot.add_cog(randCog(bot))