import pathlib

def make_download_dir(dir="/tmp/"):
    p = pathlib.Path(dir)
    p.mkdir(mode=0o777, parents=True, exist_ok=True)

    return p.Path(dir).exists()
