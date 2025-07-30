import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.tensorflow
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json
import dagshub


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _test_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.test_generator = test_datagenerator.flow_from_directory(
            directory=Path(self.config.training_data) / "test",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._test_generator()
        self.score = self.model.evaluate(self.test_generator)
        self.save_score()


    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
    def log_into_mlflow(self):
        dagshub.init(repo_owner='Mohit0199', repo_name='End_to_End_Animal_Classification_DL', mlflow=True)
        
        with mlflow.start_run() as run:
            mlflow.log_params(self.config.all_params) # logs all params from params.yaml

            # logs the metrics from the model evaluation
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            ) 

            mlflow.tensorflow.log_model(self.model, artifact_path="model") # logs under artifact_path=model

            # Register the logged model
            mlflow.register_model(
                model_uri=f"runs:/{run.info.run_id}/model",
                name="Animal_Classifier"
            )

                    
    


