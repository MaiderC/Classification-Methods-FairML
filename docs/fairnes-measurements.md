## Types of bias

*Reference:* [A Survey on Bias and Fairness in Machine Learning](https://arxiv.org/pdf/1908.09635.pdf)

### Data to algorithm

- **Measurement bias**: Caused by how we chose, ultilize and measure the data.
- **Ommited variable bias:** Omitted variable bias4 occurs when one or more important variables are left out of the model.
- **Representation bias**: Arises when the selected samples are not representative of the entire population.
- **Aggregation bias:** Aggregation bias (or ecological fallacy) arises when false conclusions are drawn about individuals from observing the entire population.
- **Simposon's paradox**

### Algorithm to user

- **Algorithmic Bias:** Algorithmic bias is when the bias is not present in the input data and is added purely by the algorithm.
- **User interaction bias:** User Interaction bias is a type of bias that can not only be observant on the Web but also get triggered from two sources—the user interface and through the user itself by imposing his/her self-selected biased behavior and interaction.
- **Populatity bias:** Items that are more popular tend to be exposed more. However, popularity metrics are subject to manipulation—for example, by fake reviews or social bots.
- **Emergent bias:** Emergent bias occurs as a result of use and interaction with real users. This bias arises as a result of change in population, cultural values, or societal knowledge usually some time after the completion of design.
- **Evaluation bias:** Evaluation bias happens during model evaluation.

### User to data

Many data sources used for training ML models are user-generated.

- **Historical bias**
- **Population bias**
- **Self selection bias**
- **Social bias**
- **Temporal bias**
- **Content production bias**

## How to measure fairness

### Equalized Odds

$$
P(\hat{Y}=1|A=0,Y=y) = P(\hat{Y}=1|A=1,Y=y)
$$

$$
P[\hat{Y}=1|S=1,Y=0]−P[\hat{Y}=1|S≠1,Y=0]≤ε,
P[\hat{Y}=1|S=1,Y=1]−P[\hat{Y}=1|S≠1,Y=1]≤ε,
$$

- $A$: Protected attiribute

### Equal opportunity

(Specific case of equalized odds)

$$
P(\hat{Y}=1|A=0,Y=1) = P(\hat{Y}=1|A=1,Y=1)
$$

### Demographic parity

$$
P(\hat{Y}|A=0) = P(\hat{Y}|A=1)
$$

### Fairness through awareness

*An algorithm is fair if it gives similar predictions to similar individuals*

### Fairness through unawareness

*An algorithm is fair as long as any protected attributes A are not explicitly used in the decision-making process*

### Treatment Equality

*Treatment equality is achieved when the ratio of false negatives and false positives is the same for both protected group categories*
