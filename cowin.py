import asyncio
import aiohttp
import json
from datetime import date, datetime, timedelta
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

BASE_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"


class General(commands.Cog, name="general"):
    """General Command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="start")
    @commands.guild_only()
    async def start(self, ctx: Context, pincode: int):
        pincode = int(pincode)
        dt = date.today().strftime("%d-%m-%y")
        url = f"{BASE_URL}?pincode={pincode}&date={dt}"

        # Calculate end time (1 day from now)
        end_time = datetime.utcnow() + timedelta(days=1)

        while datetime.utcnow() <= end_time:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(url) as response:
                        data = await response.json()
                        embed = await self.process_data(ctx, data)
                        await ctx.send(embed=embed)
                        await asyncio.sleep(300)
                except (aiohttp.ClientError, json.JSONDecodeError) as e:
                    print(f"Error: {e}")
                    continue

    async def process_data(self, ctx: Context, data):
        centres = data["centers"]
        embed = Embed(title="List", description="------------------------------")

        for centre in centres:
            session = centre["sessions"][0]
            if int(session["available_capacity"]) == 0:
                continue
            fields = [
                ("Centre Name", centre["name"], False),
                ("Vaccine", session["vaccine"], False),
                ("Fee type", f"Free <@{ctx.author.id}>" if centre["fee_type"] == "Free" else centre["fee_type"], False),
                ("Date", session["date"], False),
                ("Available capacity", session["available_capacity"], False),
                ("Dose1 Capacity", session["available_capacity_dose1"], False),
                ("Dose2 Capacity", session["available_capacity_dose2"], False),
                ("Min age", session["min_age_limit"], False),
                ("All age", session["allow_all_age"], False),
            ]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

        embed.add_field(name="------------------------------", value="------------------------------")
        return embed


async def setup(bot):
    await bot.add_cog(General(bot))
