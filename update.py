import logging
import re

from altparse import AltSourceManager, Parser, altsource_from_file

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

########################
## ALTSTORE COMPLETE
########################

sources_data = [
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://apps.altstore.io"},
        "ids": ["com.rileytestut.AltStore", "com.rileytestut.AltStore.Beta", "com.rileytestut.Delta", "com.rileytestut.Delta.Beta", "com.rileytestut.Clip", "com.rileytestut.Clip.Beta"],
        "getAllNews": True
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://alpha.altstore.io"},
        "ids": ["com.rileytestut.AltStore.Alpha", "com.rileytestut.Delta.Alpha"],
        "getAllNews": True
    }
]
alternate_app_data = {
    "com.rileytestut.AltStore.Beta": {
        "name": "AltStore (Beta)",
        "beta": False
    },
    "com.rileytestut.Delta.Beta": {
        "name": "Delta (Beta)",
        "beta": False
    },
    "com.rileytestut.Clip.Beta": {
        "name": "Clip (Beta)",
        "beta": False
    }
}

src = altsource_from_file("altstore-complete.json")
alt_complete = AltSourceManager(src, sources_data)
try:
    alt_complete.update()
    alt_complete.update_hashes()
    alt_complete.alter_app_info(alternate_app_data)
    alt_complete.save()
    alt_complete.save(alternate_dir="dist/altstore-complete.min.json",prettify=False)
except Exception as err:
    logging.error(f"Unable to update {alt_complete.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
