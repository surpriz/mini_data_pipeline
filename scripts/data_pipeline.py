import pandas as pd

def ingest_data(input_path: str) -> pd.DataFrame:
    """Charge le dataset depuis un fichier CSV."""
    df = pd.read_csv(input_path)
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Effectue une transformation simple (ex: suppression des NaN)."""
    df = df.dropna()
    return df

def export_data(df: pd.DataFrame, output_path: str) -> None:
    """Exporte le DataFrame nettoyé dans un fichier CSV."""
    df.to_csv(output_path, index=False)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Effectue une transformation simple (ex: suppression des NaN) et calcule des métriques.
    
    Args:
        df: DataFrame source
    Returns:
        DataFrame transformé avec métriques additionnelles
    """
    # Nettoyage basique
    df = df.dropna()
    
    # Calcul de métriques
    df['total_value'] = df['price'] * df['quantity']
    df['average_price'] = df['price'].mean()
    
    return df

if __name__ == "__main__":
    # Points d'entrée
    raw_data_path = "data/raw_data.csv"
    output_path = "output/cleaned_data.csv"

    df_raw = ingest_data(raw_data_path)
    df_clean = transform_data(df_raw)
    export_data(df_clean, output_path)
    print("Pipeline exécuté avec succès !")
