import os
from ultralytics import YOLO


ALL_MODELS = ['yolov8n-seg', 'yolov8s-seg', 'yolov8m-seg', 'yolov8l-seg', 'yolov8x-seg', 'yolov9c-seg', 'yolov9e-seg']
BACKBONES_DIR = os.path.join('models', 'backbone')


def get_backbone_path(model_name: str):
    """
    Utility function to get a downloaded backbone model path given the model name.
    
    Args:
        model_name (str): The name of the model.

    Returns:
        str: The full path to the model file.
    """
    return os.path.join(BACKBONES_DIR, model_name + ".pt")
    

def download_models(models_to_download: list = None):
    """
    Downloads the models specified in the list. If no list is provided, all models are downloaded.

    Args:
        models_to_download (list, optional): List of model names to download. Defaults to None.

    Returns:
        None
    """
    os.makedirs(BACKBONES_DIR, exist_ok=True)
    if models_to_download is None:
        models_to_download = ALL_MODELS
    for model in models_to_download:
        YOLO(get_backbone_path(model))


def export_to_onnx(model_path: str, **extra_params):
    model = YOLO(model_path)
    model.export(format="onnx", **extra_params)


def export_to_tensor_rt(model, **extra_params):
    model.export(format="engine", **extra_params)


if __name__ == "__main__":
    # Descargar los modelos a utilizar
    download_models()