"""Async functions for generating and returning images.

Includes team/player card generation and image-based statistics as needed.
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array
import io

player_card_base_img_fp = "src/static/black.png"

'''
async def make_player_card(player):
    """Generate and return a player card (as a direct image)."""
    img = Image.open(player_card_base_img_fp, mode='r')

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("src/static/Nunito-Regular.ttf", 100)
    draw.text((200, 0), "Information:", (255, 255, 255), font=font)
    #i guess you have to seek before you actually do the thing
    #solution from here: #https://stackoverflow.com/questions/63209888/send-pillow-image-on-discord-without-saving-the-image
    with io.BytesIO() as img_binary:
        img.save(img_binary, 'PNG')
        img_binary.seek(0)
        return img_binary
'''

async def make_player_card(player, data):
    """Generate and return a player card (as a discord.py-compatible image).
    
    `data` is a map containing the following information:
    ```
    {
        player_name: str,
    }
    ```"""
    pass

async def make_player_best(player, data):
    """Generate and return a player score leaderboard (as a discord.py-compatible image)."""
    pass

async def make_team_card(player, data):
    """Generate and return a team card (as a discord.py-compatible image)."""
    pass

async def make_team_best(player, data):
    """Generate and return a team score leaderboard(as a discord.py-compatible image)."""
    pass

async def make_map_best(player, data):
    """Generate and return a map leaderboard (as a discord.py-compatible image_."""
    pass

async def make_map_card(player, data):
    """Generate and return a map stats card (as a discord.py-compatible image)."""
    pass