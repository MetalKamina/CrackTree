import numpy as np
import os
import sys
from PIL import Image
import pickle
import pandas as pd


def load_data(path):
    print("Loading data...")
    jobs = []
    for file in os.listdir(path):
        try:
            im = Image.open(path+"/"+file).convert('L')
            im = im.resize((227,227))
            gray = np.array(im)
            gray = gray.flatten()
            jobs.append(gray)
        except:
            print("Failed to load "+file+".")
            exit()
    return np.array(jobs), os.listdir(path)

def make_preds(data):
    print("Predicting...")
    try:
        model = pickle.load(open("model.pkl","rb"))
    except:
        print("Failed to load model.\nTry downloading from https://github.com/MetalKamina/CrackTree/")
        exit()

    preds = model.predict(data)
    return preds

def export_results(preds,files,path):
    print("Exporting...")
    try:
        df = pd.DataFrame()
        df["filename"] = files
        df["prediction"] = preds
        df.to_csv(path+"/"+"output.csv")
    except:
        print("Failed to export.")
        exit()

if __name__ == "__main__":
    args = sys.argv
    if(len(args) != 2):
        print("Usage: python predict.py \"path/to/folder\"")
        exit()
    data,files = load_data(args[1])
    preds = make_preds(data)
    export_results(preds,files,args[1])