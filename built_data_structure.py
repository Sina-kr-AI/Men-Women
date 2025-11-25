import os 
import shutil
import pathlib

new_dir=pathlib.Path("men_women_dataset")

def make_subset(base_dir,subset_dir,start,end):
    for category in ("men","women"):
        dir=new_dir/subset_dir/category
        if not os.path.exists(dir):
            os.makedirs(dir)
        files=os.listdir(os.path.join(base_dir,category))
        fnames=[files[i] for i in range(start,end)]
        for fname in fnames:
            shutil.copyfile(src=os.path.join(base_dir,category,fname),dst=os.path.join(dir,fname))

make_subset("traindata/traindata","validation",start=0,end=200)
make_subset("traindata/traindata","train",start=200,end=999)
make_subset("testdata/testdata","test",start=0,end=400)