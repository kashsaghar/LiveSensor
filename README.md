# LiveSensor - APS Failure Prediction

LiveSensor is an end-to-end MLOps project that predicts Air Pressure System (APS) failures in heavy-duty vehicles using the Scania APS Failure dataset. The project follows a production-style machine learning pipeline with modular architecture, automated training workflows, experiment tracking, and deployment support.

The primary objective is to identify failures in the APS system while minimizing unnecessary maintenance costs caused by false predictions.

---

## Features

- End-to-end ML pipeline
- Automated data ingestion from MongoDB
- Data validation and schema verification
- Data transformation and preprocessing
- Model training and hyperparameter tuning
- Model evaluation and comparison
- Model versioning
- Experiment tracking with MLflow
- Pipeline artifact management
- Logging and exception handling
- Environment variable management
- Ready for deployment

---

## Project Workflow

```
Data Ingestion
        │
        ▼
Data Validation
        │
        ▼
Data Transformation
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Pusher / Saved Model
```

---

## Tech Stack

### Programming Language

- Python 3.x

### Machine Learning

- Scikit-learn
- XGBoost
- NumPy
- Pandas
- SciPy

### Data Storage

- MongoDB

### Experiment Tracking

- MLflow

### Data Visualization

- Matplotlib
- Seaborn

### MLOps & Deployment

- FastAPI
- Uvicorn
- Docker
- Git
- GitHub

### Development Tools

- Jupyter Notebook
- VS Code

### Configuration & Utilities

- python-dotenv
- PyYAML
- Logging
- Custom Exception Handling

---

## Project Structure

```
LiveSensor/
│
├── sensor/
│   ├── components/
│   ├── configuration/
│   ├── data_access/
│   ├── entity/
│   ├── pipeline/
│   ├── utils/
│   ├── cloud/
│   └── constant/
│
├── notebook/
├── saved_models/
├── artifact/
├── logs/
├── config/
├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses the **APS Failure at Scania Trucks** dataset.

- Binary classification problem
- Predicts whether a failure belongs to the APS component or another vehicle component
- Highly imbalanced dataset
- Missing value handling and preprocessing included

---

## Machine Learning Pipeline

- Data Ingestion
- Data Validation
- Data Transformation
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Saving
- Prediction Pipeline

---

## Installation

Clone the repository

```bash
git clone https://github.com/kashsaghar/LiveSensor.git
```

Move into the project

```bash
cd LiveSensor
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows
```
conda activate .\venv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure the required environment variables.

Run the training pipeline

```bash
python main.py
```

---

## Future Improvements

- CI/CD pipeline using GitHub Actions
- Cloud deployment
- Model monitoring
- Drift detection
- REST API deployment
- Dashboard for predictions

---

## Learning Outcomes

This project demonstrates practical experience with:

- End-to-end Machine Learning pipelines
- MLOps principles
- Data engineering workflows
- Production-ready project architecture
- Model experimentation and tracking
- Version control and reproducible ML workflows

---

## Acknowledgements

This project is inspired by the iNeuron MLOps training project and extends it with additional improvements and custom implementations while following industry-standard machine learning engineering practices.