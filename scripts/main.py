from ingest import ingest_data
from transform import transform_data
from export import export_data

def run_pipeline() -> None:
    """
    Exécute le pipeline complet de données.
    """
    try:
        # Configuration
        input_path = "../data/raw_data.csv"
        output_path = "../output/cleaned_data.csv"
        
        # Exécution du pipeline
        print("🚀 Démarrage du pipeline...")
        df_raw = ingest_data(input_path)
        df_transformed = transform_data(df_raw)
        export_data(df_transformed, output_path)
        print("✅ Pipeline exécuté avec succès !")
        
    except Exception as e:
        print(f"❌ Erreur dans le pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()