

# TEOREMA DE BAYES
#         P(A)P(B|A)
# P(A|B)= ----------
#           P(B)


# _______|      CANCER        |
# S |    |--------------------|
# Y |    |    SI   |   NO     |
# M |----|--------------------|
# P | SI |    1    |    10    |   11
# T |____|____________________|
# O | NO |    0    |   99989  |  99989
# M |____|____________________|
#             1        99999


def calculo_bayes(prior_a,prob_B_dado_A,prob_B):
    return (prior_a * prob_B_dado_A)/prob_B

if __name__ == "__main__":
    prob_cancer=1/100000   # Total si cancer
    proba_sintoma_dado_cancer = 1  # si sintoma y si cancer
    proba_sintoma_dado_no_cancer = 10/99999  # si sintoma y no cancer
    proba_no_cancer= 1-prob_cancer   # Total no cancer
    prob_sintoma = (proba_sintoma_dado_cancer*prob_cancer) + (proba_sintoma_dado_no_cancer*proba_no_cancer)
# proba de cancer dado si sintoma? 
    prob_cancer_dado_sintoma=calculo_bayes(prob_cancer,proba_sintoma_dado_cancer,prob_sintoma)
    print(prob_cancer_dado_sintoma)