from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging

from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import load_object
from sensor.ml.model.estimator import ModelResolver, TargetValueMapping
from sensor.pipeline import training_pipeline
from sensor.constant.training_pipeline import SAVED_MODEL_DIR

from fastapi import FastAPI, File, UploadFile
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import io

app = FastAPI()

origins = ["*"]
# Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    try:
        training_pipeline = TrainPipeline()

        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")

        training_pipeline.run_pipeline()
        return Response("Training successfully completed!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # read uploaded csv into a dataframe
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # dataset uses "na" (string) as its missing value marker, so
        # make sure it's actually treated as a missing value
        df.replace("na", np.nan, inplace=True)

        # drop target column if it happens to be present in the uploaded file
        if "class" in df.columns:
            df.drop(columns=["class"], inplace=True)

        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")

        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)

        y_pred = model.predict(df)

        df["predicted_column"] = y_pred
        df["predicted_column"] = df["predicted_column"].replace(
            TargetValueMapping().reverse_mapping()
        )

        output_path = "prediction_output.csv"
        df.to_csv(output_path, index=False)

        return FileResponse(
            path=output_path,
            media_type="text/csv",
            filename="prediction_output.csv",
        )

    except Exception as e:
        raise SensorException(e, sys)


def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
