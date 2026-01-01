#### Markov Regime-Switching Models
Markov-based approaches capture the inherent uncertainty and dynamic transitions in market behavior. By modeling regime shifts probabilistically, these methods help quantify both historical and forward-looking market conditions—making them foundational tools in quantitative finance.

#### Hidden Markov Models (HMMs)
HMMs assume that market regimes are latent (hidden) and must be inferred from observable features such as returns, volatility, or microstructure signals. This project demonstrates how HMMs can be applied to:

- Identify market states from noisy time series

- Recognize recurring patterns in price dynamics

- Generate regime-aware trading signals

- Support systematic strategy design

The included study applies HMMs to E-mini S&P 500 (ES) data, showcasing how regime inference can enhance pattern recognition and strategy robustness.

[Hidden Markov Modeling - ES - E-mini S&P 500](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/1-Hidden-Markov-Modeling-%20ES%20-%20E-mini%20S%26P%20500.ipynb) 

[Hidden-Markov-Models- ES - Systematic-Strategy](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/2-Hidden-Markov-Models-%20ES%20-%20Systematic-Strategy.ipynb)

####

<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/5a0783d5-17b6-467c-9a30-a0c620773cac" /> Project Architecture

regime_switching_models/\
├── config/\
│   ├── [config.yaml](https://github.com/manuelmusngi/regime_switching_models/blob/main/config/config.yaml)         
├── src/\
│   ├── [__init__.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/init.py)          
│   ├── [data_loader.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/data_loader.py)        
│   ├── [feature_engineering.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/feature_engineering.py)  
│   ├── [hmm_model.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/hmm_model.py)          
│   ├── [signal_generation.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/signal_generation.py)  
│   ├── [backtesting.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/backtesting.py)        
│   ├── [utils.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/utils.py)              
│   ├── [plotter.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/src/plotter.py)             
├── [requirements.txt](https://github.com/manuelmusngi/regime_switching_models/blob/main/requirements.txt)          
└── [main.py](https://github.com/manuelmusngi/regime_switching_models/blob/main/main.py)                   


#### Dependencies
  - [requirements.txt](https://github.com/manuelmusngi/hidden-markov-modeling/blob/main/requirements.txt)

#### Future Enhancements

Upcoming additions will expand the library to include:

- Hierarchical HMMs

- Markov-Switching VAR / ARIMA models

- Regime-Switching GARCH / Stochastic Volatility models

- Machine-learning–driven regime classifiers

- Hybrid statistical–ML architectures

These extensions aim to broaden the toolkit for regime-aware modeling and systematic strategy development.

#### References
  - [Detecting bearish and bullish markets in financial time series using hierarchical hidden Markov models](https://github.com/manuelmusngi/regime_switching_models/blob/main/2007.14874v1.pdf)
  - [Markov Models for Commodity Futures: Theory and Practice](https://github.com/manuelmusngi/regime_switching_models/blob/main/ssrn-1138782.pdf)
  - [Predicting Daily Probability Distributions of S&P500 Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1288468)
  - [Option Pricing in a Regime Switching Stochastic Volatility Model](https://arxiv.org/abs/1707.01237)
  - [A Markov-switching spatio-temporal ARCH model](https://arxiv.org/abs/2310.02630)

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).


  
  
