"""Team and player bot commands/cogs."""

import discord
from discord.ext import commands
import random
import tabulate
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array
import io

class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playerbest(self, ctx, player, page=1, mods=None):
        """Return the player's sorted best scores, 10 per page, filtered by mods if defined.
        
        The returned scores are equal to `(1+(page-1)*10)` to `page*10`.
        (1 to 10, 11 to 20, ...)\n
        `mods` is a `str` - `"NM"`, `"HR"`, `"HD"`, etc. 
        """
        #get player's score ids via db_manip...
        #get player's actual scores via db_manip (filtered, sorted, and skipped)
        #construct embed here

        table = [["#","Score","Acc","Combo","/b","MP id"]]

        for i in range(1,11):
            score =  "{:,}".format(random.randint(100000,1300000))
            acc = '{:.2%}'.format(random.randint(9000,10000)/10000)
            combo = "{:,}".format(random.randint(0,2000)) + "x"
            map = random.randint(10000,10000000)
            match = random.randint(50000000,70000000)
            table.append([i, score, acc, combo, map, match])

        final = "```" + tabulate.tabulate(table, headers="firstrow") + "```"

        player_url = f'https://osu.ppy.sh/u/{player}'
        em_msg = discord.Embed()
        em_msg.set_footer(text=f"This table may look jank if you don't have enough horizontal space."
                               f"You can also use \"playerbestm\" to convert /b ids into the first "
                               f"20 characters of the format \"artist - title [diff].\"")
        await ctx.send(final)
        await ctx.send(embed=em_msg)

    @commands.command()
    async def playerstats(self, ctx, player):
        """Return miscellaneous stats on a player."""
        #get player's score ids via db_manip...
        #get player's actual scores via db_manip
        general = (
            f"Average Score: 1,000,000 (#999)\n"
            f"Average Accuracy: 100.00% (#999)\n"
            f"Average Team Contrib%: 100.00% (#999)\n"
        )
        score_stats = (
            f"Maps played: 100\n"
            f"Map wins/losses: 99/99 (100.00% winrate)\n"
            f"Hits: 10,000/9,999/9,999/9,999\n"
            f"1,000,000: 10\n"
            f"Average difference on win: 999,999\n"
            f"Average difference on loss: 999,999\n"
        )

        player_url = f'https://osu.ppy.sh/u/{player}'
        em_msg = discord.Embed(title=f'STK8 stats for {player}')
        em_msg.set_author(name=player, url=player_url)
        #fun fact: a.ppy.sh will actually redirect to the player id if a username is entered
        #the problem: said redirect cannot be directly used
        #will be fixed when this actually goes for the mongodb document anyways
        em_msg.set_thumbnail(url=f"https://a.ppy.sh/{player}")
        em_msg.add_field(name='General', value=general, inline=False)
        em_msg.add_field(name='Score stats', value=score_stats, inline=False)
        em_msg.set_footer(text=f"You can get a list of this player's scores with !!playerbest {player}. "
                               f"You can also use !!playercard {player} for their player card.")
        await ctx.send(embed=em_msg)

    @commands.command()
    async def playercard(self, ctx, player):
        """Generate this player's card."""
        embed_desc = '''```
╔════╦═══════════╦═══════════════════════════════════════════════════════╗
║ #  ║ Score     ║ Map                                                   ║
║    ║           ║                                                       ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 1  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 2  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 3  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 4  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 5  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 6  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 7  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 8  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 9  ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╠════╬═══════════╬═══════════════════════════════════════════════════════╣
║ 10 ║ 1,000,000 ║ UNDEAD CORPORTATION - Everything will freeze [Insane] ║
╚════╩═══════════╩═══════════════════════════════════════════════════════╝```'''
        em_msg = discord.Embed(description=embed_desc)
        await ctx.send(embed=em_msg)

class TeamCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def teambest(self, ctx, team_name, page=1, mods=None):
        """Return the player's sorted best scores, 10 per page, filtered by mods if defined.
        
        The returned scores are equal to `(1+(page-1)*10)` to `page*10`.
        (1 to 10, 11 to 20, ...)\n
        `mods` is a `str` - `"NM"`, `"HR"`, `"HD"`, etc. 
        """
        #get player's score ids via db_manip...
        #get player's actual scores via db_manip (filtered, sorted, and skipped)
        #construct embed here
        await ctx.send('unimplemented')

    @commands.command()
    async def teamstats(self, ctx, team_name):
        """Return miscellaneous stats on a player."""
        #get player's score ids via db_manip...
        #get player's actual scores via db_manip
        general = (
            f"Average Score: 1,000,000 (#999)\n"
            f"Average Accuracy: 100.00% (#999)\n"
            f"Average Team Contrib%: 100.00% (#999)\n"
        )
        score_stats = (
            f"Maps played: 100\n"
            f"Map wins|losses: 99|99 (100.00% winrate)\n"
            f"Hits: 10,000/9,999/9,999/9,999\n"
            f"1,000,000: 10\n"
            f"Average difference on win: 999,999\n"
            f"Average difference on loss: 999,999\n"
        )

        player_url = f'https://osu.ppy.sh/u/{player}'
        em_msg = discord.Embed(title=f'STK8 stats for {player}')
        em_msg.set_author(name=player, url=player_url)
        #fun fact: a.ppy.sh will actually redirect to the player id if a username is entered
        #the problem: said redirect cannot be directly used
        em_msg.set_thumbnail(url=f"https://a.ppy.sh/{player}")
        em_msg.add_field(name='General', value=general, inline=False)
        em_msg.add_field(name='Score stats', value=score_stats, inline=False)
        em_msg.set_footer(text=f"You can get a list of this player's scores with !!playerbest {player}. "
                               f"You can also use !!playercard {player} for their player card.")
        await ctx.send(embed=em_msg)

    @commands.command()
    async def teamcard(self, ctx, team_name):
        """Generate this team's card."""
        pass