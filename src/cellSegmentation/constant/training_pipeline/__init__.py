#remains contant for every project just change url link.

ARTIFACTS_DIR: str = 'artifacts'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1yEjWa5ii-J9ofrawmKsPFr5cqdsih_af/view?usp=sharing"


DATA_VALIDATION_DIR_NAME: str='data_validation'
DATA_VALIDATION_STATUS_FILE='status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES=['train','valid','test','data.yaml']


MODEL_TRAINER_DIR_NAME:str="model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME:str='yolov8s-seg.pt'
MODEL_TRAINER_NO_EPOCHS:int=50
MODEL_TRAINER_BATCH_SIZE:int=16