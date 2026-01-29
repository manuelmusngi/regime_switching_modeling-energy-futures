from hmm_ng.pipeline import run_pipeline

def main():
    results = run_pipeline()
    print(results["summary"])

if __name__ == "__main__":
    main()
