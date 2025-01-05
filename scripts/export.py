import pandas as pd

def export_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Exporte les données vers un fichier CSV.
    
    Args:
        df: DataFrame à exporter
        output_path: Chemin du fichier de sortie
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"✅ Données exportées vers {output_path}")
    except Exception as e:
        print(f"❌ Erreur lors de l'export: {str(e)}")
        raise