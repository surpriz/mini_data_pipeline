import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et transforme les données.
    
    Args:
        df: DataFrame source
    
    Returns:
        pd.DataFrame: DataFrame transformé avec métriques calculées
    """
    try:
        # Nettoyage
        df = df.dropna()
        
        # Calcul des métriques
        df['total_value'] = df['price'] * df['quantity']
        df['average_price'] = df['price'].mean()
        
        print("✅ Transformations effectuées avec succès")
        return df
    except Exception as e:
        print(f"❌ Erreur lors de la transformation: {str(e)}")
        raise