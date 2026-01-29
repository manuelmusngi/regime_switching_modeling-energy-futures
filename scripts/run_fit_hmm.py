from hmm_ng.pipeline import run_pipeline

def main():
    results = run_pipeline()
    print("Transition matrix:")
    print(results["transition_matrix"])

if __name__ == "__main__":
    main()
