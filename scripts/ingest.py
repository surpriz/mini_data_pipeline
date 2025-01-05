import pandas as pd

def ingest_data(input_path: str) -> pd.DataFrame:
    """
    Charge les données depuis un fichier CSV.
    
    Args:
        input_path: Chemin vers le fichier CSV source
    
    Returns:
        pd.DataFrame: Les données chargées
    """
    try:
        df = pd.read_csv(input_path)
        print(f"✅ Données chargées depuis {input_path}")
        return df
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {str(e)}")
        raise