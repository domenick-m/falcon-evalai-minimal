#!/usr/bin/env -S uv run --script
# /// script
# requires-python = "==3.11.*"
# dependencies = ["evalai==1.3.18", "setuptools==70.3.0"]  # --version uses pkg_resources.
#
# [tool.uv]
# override-dependencies = ["lxml==6.1.3"]  # Python 3.11 wheels for EvalAI's HTML parser.
# ///
from functools import partial

import docker
from docker.models.images import ImageCollection
from evalai.main import main

get_image = ImageCollection.get


def get_image_with_size(images, name):
    image = get_image(images, name)
    # EvalAI reads VirtualSize when checking the upload limit. New engines return Size.
    if image.attrs.get("VirtualSize") is None:
        image.attrs["VirtualSize"] = image.attrs["Size"]
    return image


if __name__ == "__main__":
    # EvalAI's Docker SDK defaults to API 1.35. Negotiate with the local engine.
    docker.from_env = partial(docker.from_env, version="auto")
    ImageCollection.get = get_image_with_size
    main(prog_name="evalai")
