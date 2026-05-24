import os
import shutil

def on_post_build(config, **kwargs):
    """Copy .well-known directory to the site output."""
    docs_dir = config['docs_dir']
    site_dir = config['site_dir']
    well_known_src = os.path.join(docs_dir, '.well-known')
    well_known_dst = os.path.join(site_dir, '.well-known')

    if os.path.exists(well_known_src):
        os.makedirs(well_known_dst, exist_ok=True)
        for item in os.listdir(well_known_src):
            src = os.path.join(well_known_src, item)
            dst = os.path.join(well_known_dst, item)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
            elif os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
