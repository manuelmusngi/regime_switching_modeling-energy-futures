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

  - [Markov Models for Commodity Futures: Theory and Practice](https://github.com/manuelmusngi/regime_switching_models/blob/main/ssrn-1138782.pdf)
  - [Detecting bearish and bullish markets in financial time series using hierarchical hidden Markov models](https://github.com/manuelmusngi/regime_switching_models/blob/main/2007.14874v1.pdf)
  - [A Markov-switching spatio-temporal ARCH model](https://arxiv.org/abs/2310.02630)
  - [Option Pricing in a Regime Switching Stochastic Volatility Model](https://arxiv.org/abs/1707.01237)

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).


  
  
