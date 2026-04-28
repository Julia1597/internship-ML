# ENGLISH
# Data Drift Analysis – Implementation (KS-test & PSI)

## 1. Objective

The objective of this part is to implement a method to detect and measure data drift between two datasets.

---

## 2. Method principle

The analysis is based on two complementary approaches:

- The KS-test (Kolmogorov-Smirnov): allows detecting whether there is a difference between two distributions  
- The PSI (Population Stability Index): allows measuring the magnitude of this difference  

---

## 3. Data preparation

The data was loaded using the pandas library.

The dataset was then divided into two parts:

- A reference dataset (df_A) 70%  
- A recent dataset (df_B) 30%  

Objective:  
Compare old data and recent data in order to identify a possible change.

---

## 4. Simulation of data drift

In order to test the methods, a drift was simulated on the variable `windspeed_100m`.

The values of this variable were modified in the recent dataset (df_B).

Objective:  
Create a voluntary difference between the two datasets to verify that the methods correctly detect the drift.

---

## 5. Detection using KS-test

The KS-test was applied on the variable `windspeed_100m`.

Result obtained:
- p-value = 0.0

Interpretation:  
A p-value lower than 0.05 indicates a significant difference between the two distributions.

Conclusion:  
The test detects a data drift.

---

## 6. Measurement using PSI

The PSI was calculated on the same variable.

Result obtained:
- PSI = 0.479

Interpretation:
- PSI < 0.1: stable  
- 0.1 ≤ PSI < 0.25: moderate change  
- PSI ≥ 0.25: significant drift  

Conclusion:  
The observed drift is significant.

---

## 7. Global conclusion

The results show that:

- The KS-test allows detecting the presence of data drift  
- The PSI allows evaluating its importance  

These two methods are complementary and provide a reliable analysis of data evolution.

---

## 8. Perspectives

The next steps consist of:

- Applying these methods to other variables  
- Automating drift detection  
- Integrating the results into a monitoring system  


# FRANCAIS
# Data Drift Analysis – Implementation (KS-test & PSI)

## 1. Objectif

L’objectif de cette partie est de mettre en place une méthode permettant de détecter et mesurer une dérive des données (data drift) entre deux ensembles de données.

---

## 2. Principe de la méthode

L’analyse repose sur deux approches complémentaires :

- Le KS-test (Kolmogorov-Smirnov) : permet de détecter s’il existe une différence entre deux distributions
- Le PSI (Population Stability Index) : permet de mesurer l’ampleur de cette différence

---

## 3. Préparation des données

Les données ont été chargées avec la bibliothèque pandas.

Le dataset a ensuite été divisé en deux parties :

- Un ensemble de référence (df_A) 70%
- Un ensemble de données récentes (df_B) 80%

Objectif :
Comparer les données anciennes et les données récentes afin d’identifier un éventuel changement.

---

## 4. Simulation d’un data drift

Afin de tester les méthodes, une dérive a été simulée sur la variable `windspeed_100m`.

Les valeurs de cette variable ont été modifiées dans le dataset récent (df_B).

Objectif :
Créer un écart volontaire entre les deux ensembles de données pour vérifier que les méthodes détectent correctement le drift.

---

## 5. Détection avec le KS-test

Le KS-test a été appliqué sur la variable `windspeed_100m`.

Résultat obtenu :
- p-value = 0.0

Interprétation :
Une p-value inférieure à 0.05 indique une différence significative entre les deux distributions.

Conclusion :
Le test détecte une dérive des données.

---

## 6. Mesure avec le PSI

Le PSI a été calculé sur la même variable.

Résultat obtenu :
- PSI = 0.479

Interprétation :
- PSI < 0.1 : stable
- 0.1 ≤ PSI < 0.25 : changement modéré
- PSI ≥ 0.25 : dérive importante

Conclusion :
La dérive observée est importante.

---

## 7. Conclusion globale

Les résultats montrent que :

- Le KS-test permet de détecter la présence d’un data drift
- Le PSI permet d’évaluer son importance

Ces deux méthodes sont complémentaires et permettent une analyse fiable des évolutions des données.

---

## 8. Perspectives

Les prochaines étapes consistent à :

- Appliquer ces méthodes sur d’autres variables
- Automatiser la détection du drift
- Intégrer les résultats dans un système de monitoring