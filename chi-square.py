from  scipy.stats import chi2_contingency
import numpy as np
kf_data = np.array([[142004,2855], [1403201,105740]])
kf = chi2_contingency(kf_data)
print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)
# chisq-statistic=0.4054, p-value=0.5243, df=1 expected_frep=[[39.22580645 24.77419355][36.77419355 23.22580645]]
