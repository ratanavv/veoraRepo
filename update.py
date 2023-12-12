import logging
import re

from altparse import AltSourceManager, Parser, altsource_from_file

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

sources_data = [
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "StreamerApp", "repo_name": "Streamer"},
        "ids": ["com.streamer.ios"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "Aidoku", "repo_name": "Aidoku"},
        "ids": ["xyz.skitty.Aidoku"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://raw.githubusercontent.com/arichorn/arichorn.github.io/main/apps.json"},
        "ids": ["com.google.ios.youtube"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "yattee", "repo_name": "yattee"},
        "ids": ["stream.yattee.app"]
    }
]
alternate_app_data = {
        "none"
}

src = altsource_from_file("veorarepo.json")
veora_repo = AltSourceManager(src, sources_data)
try:
    veora_repo.update()
    veora_repo.update_hashes()
    #veora_repo.alter_app_info(alternate_app_data)
    veora_repo.save()
    veora_repo.save(alternate_dir="dist/veorarepo.min.json",prettify=False)
except Exception as err:
    logging.error(f"Unable to update {veora_repo.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
