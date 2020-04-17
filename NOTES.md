## Titles
- Reduzindo Falsos Positivos em preditores de transações fraudulentas;
- Aprimorando o desempenho de classificadores de transações fraudulentas;
------------------------------

## Structure
1. Introdução
    - Fraudes Financeiras
    - Poucas Bases públicas
    - Poucas elementos amostrais
    - Preditores com Falsos Negativos

2. Revisão Literária
    - Definição de Fraude
        - Técnicas Antifraude
    - Aprendizado de Máquina
        - Tree Classifiers
        - Random Forests Classifiers
        - Percepton
        - MultiLayer Percepton
        - Support Vector Machines
    - Sampling
        - Random Sampling
        - SMOTE

3. Metodologia
    - Base de Dados
        - Breve descritivo & aquisição de dados
        - Análise Exploratória
    - Redução de Dimensionalidade
    - Resultados Preliminares
        - Overfitting e Falsos Negativos
    - Resultados Otimizados
        - Otimização dos modelos

4. Conclusão
- Propostas Futuras

------------------------------

## Model Evaluation

Section aimed on evaluating model´s performance.

### Manual ROS
nn_models - Manual ROS:
- Sigmoidal Activation - SGD:
    - Accuracy:
        - 0.83324 Train
	    - 0.71489 Test
    	- 0.68913 Validation (Only Frauds)
    - Loss: 0.915
    - 100 Epochs - Non Early Stopped

- Relu Activation - ADAM:
    - Accuracy:
        - 0.99940 Train
	    - 0.87329 Test
    	- 0.74812 Validation (Only Frauds)
    - Loss: 6.2861e-04
    - 15 Epochs - Early Stopped in 8 Epochs
    
### SMOTE
- Relu Activation - ADAM:
    - Accuracy:
        - 0.99940 Train
	    - 0.87329 Test
    	- 0.74812 Validation (Only Frauds)
    - Loss: 6.2861e-04
    - 15 Epochs - Early Stopped in 8 Epochs
- RandomForest:
    - Accuract
------------------------------