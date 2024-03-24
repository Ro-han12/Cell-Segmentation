import sys,os 
from src.cellSegmentation.pipeline.training_pipeline import TrainPipeline 

obj=TrainPipeline()
obj.run_pipeline()
print("training done")
