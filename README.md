#### Markov Regime-Switching Models
Markov-based approaches capture the inherent uncertainty and dynamic transitions in market behavior. By modeling regime shifts probabilistically, these methods help quantify both historical and forward-looking market conditions—making them foundational tools in quantitative finance.

📊 Hidden Markov Models (HMMs)
HMMs assume that market regimes are latent (hidden) and must be inferred from observable features such as returns, volatility, or microstructure signals. This project demonstrates how HMMs can be applied to:

- Identify market states from noisy time series
- Recognize recurring patterns in price dynamics
- Generate regime-aware trading signals
- Support systematic strategy design

The included simplistic study applies HMMs to Henry Hub Natural Gas (NG) data, showcasing how regime inference can enhance pattern recognition and strategy robustness, which can be applied to any instrument:

[Hidden Markov Modeling - Henry Hub Natural Gas (NG)](https://github.com/manuelmusngi/regime_switching_modeling/blob/main/Hidden-Markov-Modeling-Natural-Gas-NG.ipynb) 

🏗️ Project Architecture

hmm-ng-project/\
├── config/\
│   ├── [base.yaml](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/config/base.yaml)\
│   ├── [data.yaml](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/config/data.yaml)\
│   └── [model_hmm.yaml](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/config/model_hmm.yaml)\
├── data/\
│   ├── interim/\
│   └── processed/\
│       └── ng1_features.parquet\
├── scripts/\
│   ├── [run_full_pipeline.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/scripts/run_full_pipeline.py)\
│   └── [run_fit_hmm.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/scripts/run_fit_hmm.py)\
├── src/\
│   └── hmm_ng/\
│       ├── __init__.py\
│       ├── [config.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/config.py)\
│       ├── [logging_utils.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/logging_utils.py)\
│       ├── [paths.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/paths.py)\
│       ├── [data_ingestion.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/data_ingestion.py)\
│       ├── [preprocessing.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/preprocessing.py)\
│       ├── [features.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/features.py)\
│       ├── models/\
│       │   ├── [hmm_model.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/models/hmm_model.py)\
│       │   └── [evaluation.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/models/evaluation.py)\
│       ├── [visualization.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/visualization.py)\
│       └── [pipeline.py](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/src/hmm_ng/pipeline.py)\
└──[pyproject.toml](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/pyproject.toml)

🧊 Dependencies

[requirements.txt](https://github.com/manuelmusngi/regime_switching_modeling-energy-futures/blob/main/requirements.txt)

#### Future Enhancements

Upcoming additions will expand the library to include:

- Hierarchical HMMs

- Markov-Switching VAR / ARIMA models

- Regime-Switching GARCH / Stochastic Volatility models

- Machine-learning–driven regime classifiers

- Hybrid statistical–ML architectures

These extensions aim to broaden the toolkit for regime-aware modeling and systematic strategy development.

📚 Research References  

  - [Understanding the US Natural Gas Market: A Markov Switching VAR Approach](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3156000)
  - [Markov Models for Commodity Futures: Theory and Practice](https://github.com/manuelmusngi/regime_switching_models/blob/main/ssrn-1138782.pdf)
  - [Detecting bearish and bullish markets in financial time series using hierarchical hidden Markov models](https://github.com/manuelmusngi/regime_switching_models/blob/main/2007.14874v1.pdf)
  - [A Markov-switching spatio-temporal ARCH model](https://arxiv.org/abs/2310.02630)
  - [Option Pricing in a Regime Switching Stochastic Volatility Model](https://arxiv.org/abs/1707.01237)

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).


  
  
