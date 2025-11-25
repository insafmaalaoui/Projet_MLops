import os
import shutil

def preprocess(data_dir="data/raw", output_dir="data/processed"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for item_name in os.listdir(data_dir):
        src_path = os.path.join(data_dir, item_name)
        dst_path = os.path.join(output_dir, item_name)

        if os.path.isdir(src_path):
            # Copier tout le dossier
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            # Copier un fichier
            shutil.copy(src_path, dst_path)

    print(f"✅ Preprocessing terminé, contenu copié dans {output_dir}")
