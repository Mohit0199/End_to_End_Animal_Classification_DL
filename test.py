from cnnClassifier.pipeline.prediction import PredictionPipeline

if __name__ == "__main__":
    # Ask user for image path
    filename = input("Enter path to image file: ").strip()
    
    pipeline = PredictionPipeline(filename)
    result = pipeline.predict()
    
    print("Prediction result:", result)
