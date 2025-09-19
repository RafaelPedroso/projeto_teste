from scipy.stats import (levene,
                         ttest_ind,
                         mannwhitneyu,
                         shapiro,
                        )
#deixar
def analise_levene(dataframe, alfa=0.05, centro="mean"):
    print("Teste de Levene")

    estatistica_levene, pvalue_levene = levene(*
        [dataframe[coluna] for coluna in dataframe.columns], 
        center=centro,
        nan_policy="omit")

    print(f"estatistica_levene = {estatistica_levene:.3f}")

    if pvalue_levene > alfa:
        print(f"Variâncias iguais (valor p: {pvalue_levene:.3f})")
    else:
        print(f"Ao menos uma variância é diferente (valor p: {pvalue_levene:.3f})")


def analises_shapiro_levene(dataframe, alfa=0.05, centro="mean"):
    
    print("Teste de Shapiro e Levene")

    analise_shapiro(dataframe=dataframe, alfa=alfa)

    print()

    analise_levene(dataframe=dataframe, alfa=alfa, centro=centro)

# deixar
def analise_tteste_ind(
        dataframe,
        alfa=0.05,
        variancias_iguais=True,
        alternativas="two-sided"
):
    print("Teste de t Students - ttest_ind")

    estatistica_tteste, pvalue_tteste = ttest_ind(*
        [dataframe[coluna] for coluna in dataframe.columns],
        equal_var=variancias_iguais,
        alternative=alternativas,
        nan_policy="omit")
    
    print(f"estatistica_tteste = {estatistica_tteste:.3f}")

    if pvalue_tteste > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_tteste:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_tteste:.3f})")

# deixar
def analise_mannwhitneyu(
        dataframe,
        alfa=0.05,
        alternativas="two-sided"
):
    
    print("Teste de MannWhitney")

    estatistica_mannwhitneyu, pvalue_mannwhitneyu = mannwhitneyu(*
        [dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",
        alternative=alternativas)
    
    print(f"estatistica_mannwhitneyu = {estatistica_mannwhitneyu:.3f}")

    if pvalue_mannwhitneyu > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_mannwhitneyu:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_mannwhitneyu:.3f})")

def analise_shapiro(dataframe, alfa=0.05):
    print("Teste de Shapiro-Wilk")

    for coluna in dataframe.columns:
        estatistica_sw, pvalue_sw = shapiro(dataframe[coluna], nan_policy="omit")

        print(f"estatistica_sw = {estatistica_sw:.3f}")

        if pvalue_sw > alfa:
            print(f"{coluna} segue uma distribuição normal (valor p: {pvalue_sw:.3f})")
        else:
            print(f"{coluna} não segue uma distribuição normal (valor p: {pvalue_sw:.3f})")

def remove_outliers(dados, largura_bigodes=1.5):
    q1 = dados.quantile(0.25)
    q3 = dados.quantile(0.75)
    iqr = q3 - q1
    return dados[(dados >= q1 - largura_bigodes * iqr) & (dados <= q3 + largura_bigodes * iqr)]