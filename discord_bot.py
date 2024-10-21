# This example requires the 'message_content' intent.
# https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py

from io import BytesIO
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime, timedelta

from image_handler import merge_two_images_horizontally
from logger_decorator import LogArgsKwargs
from models.match_summary import MatchSummary
from models.timeline import TimelineData
from models.match_v5 import MatchDto, TimelineDto
from models.search_match_model import SearchMatchModel
from remote_league_data import RemoteClient

bot = commands.Bot()
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
print(os.getenv("API_KEY"))
league = RemoteClient()

from discord import ApplicationContext, File


async def send_markdown_file(ctx: ApplicationContext, content):
    file_path = "output.md"
    if not os.path.exists("out"):
        os.makedirs("out")
    file_path = os.path.join("out", f"{file_path}.md")
    with open(file_path, "w") as file:
        file.write(content)
    await ctx.send(file=File(file_path))


@LogArgsKwargs
@bot.slash_command(
    name="get_riot_id",
    description="Input your league name and tag i.e xXBoBXx#EUW",
    #   guild_ids=[...]
)
async def get_riot_id(ctx, league_name: discord.Option(str, required=True)):  # type: ignore
    puuid = league.get_riot_id(name=league_name)
    await ctx.respond(f"You're ID is: {puuid}")


@LogArgsKwargs
@bot.slash_command(
    name="search_matches",
    #   guild_ids=[...]
)
async def search_matches(
    ctx,
    player_id: discord.Option(str, required=True, description="Use the /get_riot_id to get this"),  # type: ignore
    day_to_check: discord.Option(str, required=True, description="Date to check for matches, in the format YYYY-MM-DD. Eg 2024-10-25"),  # type: ignore
    result_size: discord.Option(int, default=10, description="Amount of matches to check for, defaults to 10"),  # type: ignore
):

    day = datetime.strptime(day_to_check, "%Y-%m-%d")
    next_day = day + timedelta(days=1)
    search: SearchMatchModel = SearchMatchModel(
        start_time=day.timestamp(),
        end_time=next_day.timestamp(),
        count=result_size,
        start=0,
    )
    result: list[str] = league.search_matches(puuid=player_id, search_model=search)
    string_out = ""
    for item in result:
        string_out += item + "\n"
    await ctx.respond(f"Matches played: \n\n{string_out}")


@LogArgsKwargs
@bot.slash_command(
    name="get_match",
    description="Input your league name and tag i.e xXBoBXx#EUW",
    #   guild_ids=[...]
)
async def get_match(ctx, match_id: discord.Option(str, required=True, description="The match ID, get this from your match history or from the /search_matches command")):  # type: ignore
    match: MatchDto = league.get_match(match_id=match_id)
    await ctx.respond(f"You're matchID is: {match.metadata.matchId}")


@LogArgsKwargs
@bot.slash_command(
    name="get_match_summary",
    description="Input your league name and tag i.e xXBoBXx#EUW",
    #   guild_ids=[...]
)
async def get_match_summary(
    ctx: discord.ApplicationContext,
    match_id: discord.Option(str, required=True, description="The match ID, get this from your match history or from the /search_matches command"),  # type: ignore
):
    match: MatchDto = league.get_match(match_id=match_id)

    match_summary: MatchSummary = MatchSummary.from_match(match=match)

    # await ctx.respond(str(match_summary))
    for player in match_summary.players:
        await ctx.send(content=str(player))


@LogArgsKwargs
@bot.slash_command(
    name="get_milestone_stats", description="Input a MatchID and the minute you want"
)
async def get_milestone_stats(
    ctx: discord.ApplicationContext,
    match_id: discord.Option(str, required=True, description="The match ID, get this from your match history or from the /search_matches command"),  # type: ignore
    minute: discord.Option(int, required=True, description="The minute you want"),  # type: ignore
):
    match_timeline: TimelineDto = league.get_timeline(match_id=match_id)
    timeline_data = TimelineData.from_riot_api_data(
        api_data=match_timeline, minute=minute
    )
    await ctx.send(
        content=f"Statistics at {minute} minutes:\n======================================"
    )
    for player in timeline_data.players:
        user = league.get_user(player.name)
        await ctx.send(
            content=f"{user['gameName']}'s stats:{str(player)}======================================"
        )


@LogArgsKwargs
@bot.slash_command(
    name="get_damage_graphs", description="Input a MatchID and the minute you want"
)
async def get_damage_graphs(
    ctx: discord.ApplicationContext,
    match_id: discord.Option(str, required=True, description="The match ID, get this from your match history or from the /search_matches command"),  # type: ignore
):
    await ctx.respond("Generating images, they will be sent to the channel shortly.")
    imgs: list[BytesIO] = league.get_damage_graphs(match_id=match_id)
    merged_image = merge_two_images_horizontally(imgs)
    merged_image.seek(0)
    await ctx.send(file=File(merged_image, filename="merged_image.png"))


print("Starting...")
bot.run(bot_token)
