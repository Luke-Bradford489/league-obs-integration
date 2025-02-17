from io import BytesIO
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image, ImageDraw, ImageFont
import requests

from models.ten_min_stats_model import TenMinStatsModel

def _getRemoteImage(name: str) -> BytesIO:
    ddragon_url_template = (
        f"https://ddragon.leagueoflegends.com/cdn/14.20.1/img/champion/"
    )
    file_type = f".png"
    return Image.open(
        BytesIO(requests.get(url=f"{ddragon_url_template}{name}{file_type}").content)
    )


def _add_image(img, y, ax: plt.Axes, invert_y:bool = False):
    im = OffsetImage(img, zoom=0.35)  # Adjust the zoom to resize the image
    if invert_y:
        y_limits = ax.get_ylim()
        y = y_limits[1] - y + y_limits[0]  # Adjust y to match the inverted axis

    ab = AnnotationBbox(
        im,
        (0, y),
        xycoords=("data", "data"),
        box_alignment=(0, 0.5),
        frameon=False,
    )
    ax.add_artist(ab)


def plotBar(damage_list: list[int], champ_name_list: list[str], invert_graph=False, y_limit= 50000):
    color = "#0397AB"
    if invert_graph:
        champ_name_list = champ_name_list[::-1]
        color = "#ff3333"
    print(champ_name_list)
    icons = [_getRemoteImage(champ) for champ in champ_name_list]
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(facecolor="black")
    bars = ax.barh(champ_name_list, damage_list, color=color)

    for i, path in enumerate(icons):
        print(i / len(icons))
        _add_image(path, i, ax, invert_y=invert_graph)

    if invert_graph:
        for bar in bars:
            ax.text(
                bar.get_width() + 5, 
                bar.get_y() + bar.get_height() / 2,  
                f"{bar.get_width()}", 
                va="center",  
                ha="right",
                color=color,
                fontsize=24
            )
    else:
        for index, value in enumerate(damage_list):
            ax.text(
                value + 1, index, str(value), va="center", color=color, fontsize=24
            )
    ax.set_xlim([0, y_limit])
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])
    fig.set_size_inches((6, 5))
    fig.gca().spines["top"].set_visible(False)
    fig.gca().spines["right"].set_visible(False)
    fig.gca().spines["left"].set_visible(False)
    fig.gca().spines["bottom"].set_visible(False)

    # Optional: remove ticks
    fig.gca().tick_params(left=False, bottom=False)
    if invert_graph:
        fig.gca().invert_xaxis()
    ax.set_facecolor("black")
    fig.set_facecolor("black")
    buffer: BytesIO = BytesIO()
    fig.savefig(buffer, dpi=300, bbox_inches="tight")
    return buffer

# K/D/A
# Gold earned
# DPM
# Kill participation
# Wards placed
# Wards destroyed
def ten_min_stats(stats: TenMinStatsModel):
    width, height = 300, 180

    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', size=20)

    x, y = 10, 10
    spacing = 30

    draw.text((x, y), "0/0/0", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing), "K/D/A", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 2), "0", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 3), "MINION KILLS (CS)", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 4), "0%", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 5), "CHAMPION DAMAGE SHARE", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 6), "0", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 7), "WARDS PLACED", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 8), "0%", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 9), "KILL PARTICIPATION", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 10), "0", font=font, fill=(255, 255, 255))
    draw.text((x, y + spacing * 11), "WARDS DESTROYED", font=font, fill=(255, 255, 255))


    # Save the image
    img.save('stats_image.png')


if __name__ == "__main__":
        # Data for the bar graph
    categories = ["Ashe", "Bard", "Corki", "Diana", "Zoe"]
    values = [5123, 7222, 31333, 8123, 633]
    buf = plotBar(champ_name_list=categories, damage_list=values, invert_graph=True)
    with open('file.png', 'wb') as file:
        file.write(buf.getvalue())
