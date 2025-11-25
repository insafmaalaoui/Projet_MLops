import pandas as pd
from pathlib import Path
from .load_data import load_movielens

def preprocess(raw_dir="data/raw/ml-1m", output_dir="data/processed"):
    ratings, movies = load_movielens(raw_dir)

    # Tri temporel
    ratings = ratings.sort_values(["UserID", "Timestamp"])

    # Split : dernier film noté = test
    test_idx = ratings.groupby("UserID").tail(1).index
    test = ratings.loc[test_idx]
    train = ratings.drop(test_idx)

    # Création dossier processed
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Sauvegarde
    train.to_csv(Path(output_dir) / "train.csv", index=False)
    test.to_csv(Path(output_dir) / "test.csv", index=False)

    print("✅ Préprocessing terminé ! Données enregistrées.")

if __name__ == "__main__":
    preprocess()
