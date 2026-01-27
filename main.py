import yaml
from src.pipelines.hmm_es_pipeline import HMMESPipeline

if __name__ == "__main__":
    with open("config/hmm_es.yaml", "r") as f:
        config = yaml.safe_load(f)

    pipeline = HMMESPipeline(config)
    results = pipeline.run()

    print("HMM Means:\n", results["params"]["means"])
    print("HMM Covariances:\n", results["params"]["covariances"])
