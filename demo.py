from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
print(dir(pipeline))
pipeline.start_data_ingestion()