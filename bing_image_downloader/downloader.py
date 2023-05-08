import os, sys
import shutil
from pathlib import Path
from bing import Bing

def download(query, limit=100, output_dir='dataset', adult_filter_off=True, 
force_replace=False, timeout=60, filter="", verbose=True):

    # engine = 'bing'
    if adult_filter_off:
        adult = 'off'
    else:
        adult = 'on'

    
    image_dir = Path(output_dir).joinpath(query).absolute()

    if force_replace:
        if Path.is_dir(image_dir):
            shutil.rmtree(image_dir)

    # check directory and create if necessary
    try:
        if not Path.is_dir(image_dir):
            Path.mkdir(image_dir, parents=True)

    except Exception as e:
        print('[Error]Failed to create directory.', e)
        sys.exit(1)
    
    import sys
    sys.path.append('/home/barti/PosterRecognition/scraper')
    from similarity_calc import getTransform, getResNet50, getSimilarity

    transform = getTransform()
    model = getResNet50()

    print("[%] Downloading Images to {}".format(str(image_dir.absolute())))
    bing = Bing(query, limit, image_dir, adult, timeout, filter=filter, verbose=verbose, transforms=transform, model=model, similarity_func=getSimilarity)
    bing.run()


if __name__ == '__main__':
    import sys
    sys.path.append('/home/barti/PosterRecognition/scraper')
    from similarity_calc import getTransform, getResNet50, getSimilarity

    transform = getTransform()
    model = getResNet50()

    download('dog', output_dir="./", limit=4, timeout=1)
