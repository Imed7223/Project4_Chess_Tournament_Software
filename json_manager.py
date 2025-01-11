import json


class JSONManager:
    @staticmethod
    def save_to_file(data, filename):
        """
        Enregistre les données dans un fichier JSON.
        """
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False, default=str)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde dans le fichier {filename} : {e}")

    @staticmethod
    def load_from_file(filename):
        """
        Charge les données à partir d'un fichier JSON.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Le fichier {filename} n'existe pas.")
            return None
        except json.JSONDecodeError as e:
            print(f"Erreur lors du décodage du fichier JSON : {e}")
            return None
