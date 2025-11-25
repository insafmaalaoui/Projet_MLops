import pandas as pd
from pathlib import Path

def load_movielens(data_dir="data/raw/ml-1m"):
    """
    Charge les fichiers MovieLens (ratings.dat, movies.dat)
    et les retourne sous forme de DataFrame pandas.
    """

    data_dir = Path(data_dir)

    ratings_cols = ["UserID", "MovieID", "Rating", "Timestamp"]
    movies_cols = ["MovieID", "Title", "Genres"]

    print("📥 Chargement des fichiers MovieLens...")

    ratings = pd.read_csv(
        data_dir / "ratings.dat",
        sep="::",
        engine="python",
        names=ratings_cols
    )

    movies = pd.read_csv(
        data_dir / "movies.dat",
        sep="::",
        engine="python",
        names=movies_cols
    )

    print("✅ Fichiers chargés avec succès !")
    return ratings, movies
