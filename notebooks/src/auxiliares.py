import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import (shapiro,
                         levene,
                         ttest_ind,
                         ttest_rel,
                         f_oneway,
                         wilcoxon,
                         mannwhitneyu,
                         friedmanchisquare,
                         kruskal)

def tabela_distribuicao_frequencias(dataframe, coluna, coluna_frequencia=False):

    """Cria uma tabela de distribuição de frequências para uma coluna de um dataframe.
    Espera uma coluna categórica.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe com os dados.
    coluna : str
        Nome da coluna categórica.
    coluna_frequencia: bool
        Informa se o dataframe já possui coluna de frequencia. Padrão: False

    Returns
    -------
    pd.DataFrame
        Dataframe com a tabela de distribuição de frequências.
    """ 

    df_estatistica = pd.DataFrame()

    if coluna_frequencia:
        df_estatistica["frequencia"] = dataframe[coluna]
        df_estatistica["frequencia_relativa"] = df_estatistica["frequencia"] / df_estatistica["frequencia"].sum()
    else:
        df_estatistica["frequencia"] = dataframe[coluna].value_counts().sort_index()
        df_estatistica["frequencia_relativa"] = dataframe[coluna].value_counts(normalize=True).sort_index()

    df_estatistica["frequencia_acumulada"] = df_estatistica["frequencia"].cumsum()
    df_estatistica["frequencia_relativa_acumulada"] = df_estatistica["frequencia_relativa"].cumsum()

    return df_estatistica


def figura_histograma_boxplot(dataframe, coluna, intervalo="auto"):

    """Cria graficos de histrogramas e boxplots
    
    Parametros:
    dataframe: pd.DataFrame
    coluna: str

    Returns:
    gráficos histrograma e boxplot
    
    """

    fig, (ax1, ax2) = plt.subplots(nrows=2,
                                ncols=1,
                                gridspec_kw={
                                    "height_ratios":(0.15, 0.85),
                                    "hspace": 0.03,
                                    },
                                sharex=True,
                                )
    sns.boxplot(data=dataframe,
                x=coluna,
                showmeans=True,
                meanprops={"color":"C1", "linewidth":1.5, "linestyle":"--"},
                medianprops={"color":"C2", "linewidth":1.5, "linestyle":"--"},
                ax=ax1, meanline=True,
                )

    sns.histplot(data=dataframe, x=coluna, kde=True, bins=intervalo, ax=ax2)

    for ax in (ax1, ax2):
        ax.grid(True, linestyle="--", color="gray", alpha=0.5)
        ax.set_axisbelow(True)

    ax2.axvline(dataframe[coluna].mean(), color="C1", linestyle="--", label="Média")
    ax2.axvline(dataframe[coluna].median(), color="C2", linestyle="--", label="Mediana")
    ax2.axvline(dataframe[coluna].mode()[0], color="C3", linestyle="--", label="Moda")

    ax2.legend()

    plt.show()

def analise_shapiro(dataframe, alfa=0.05):
    print("Teste de Shapiro-Wilk")

    for coluna in dataframe.columns:
        estatistica_sw, pvalue_sw = shapiro(dataframe[coluna], nan_policy="omit")

        print(f"estatistica_sw = {estatistica_sw:.3f}")

        if pvalue_sw > alfa:
            print(f"{coluna} segue uma distribuição normal (valor p: {pvalue_sw:.3f})")
        else:
            print(f"{coluna} não segue uma distribuição normal (valor p: {pvalue_sw:.3f})")


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

def analise_tteste_rel(
        dataframe,
        alfa=0.05,
        alternativas="two-sided"
):
    
    print("Teste de t Students - ttest_rel")

    estatistica_tteste, pvalue_tteste = ttest_rel(*
        [dataframe[coluna] for coluna in dataframe.columns],
        alternative=alternativas,
        nan_policy="omit")
    
    print(f"estatistica_tteste = {estatistica_tteste:.3f}")

    if pvalue_tteste > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_tteste:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_tteste:.3f})")


def analise_anova_one_way(
        dataframe,
        alfa=0.05,
):
    
    print("Teste de ANOVA onde way")

    estatistica_f, pvalue_f = f_oneway(*
        [dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit")
    
    print(f"estatistica_f= {estatistica_f:.3f}")

    if pvalue_f > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_f:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_f:.3f})")


def analise_wilcoxon(
        dataframe,
        alfa=0.05,
        alternativas="two-sided"
):
    
    print("Teste de Wilcoxon")

    estatistica_wilcoxon, pvalue_wilcoxon = wilcoxon(*
        [dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",
        alternative=alternativas)
    
    print(f"estatistica_wilcoxon = {estatistica_wilcoxon:.3f}")

    if pvalue_wilcoxon > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_wilcoxon:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_wilcoxon:.3f})")

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

def analise_friedmanchisquare(
        dataframe,
        alfa=0.05,
):
    
    print("Teste de Friedmanchisquare")

    estatistica_friedmanchisquare, pvalue_friedmanchisquare = friedmanchisquare(*
        [dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",)
    
    print(f"estatistica_friedmanchisquare = {estatistica_friedmanchisquare:.3f}")

    if pvalue_friedmanchisquare > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_friedmanchisquare:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_friedmanchisquare:.3f})")

def analise_kruskal(
        dataframe,
        alfa=0.05,
):
    
    print("Teste de Kruskal")

    estatistica_kruskal, pvalue_kruskal = kruskal(*
        [dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",)
    
    print(f"estatistica_kruskal = {estatistica_kruskal:.3f}")

    if pvalue_kruskal > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {pvalue_kruskal:.3f})")
    else:
        print(f"Rejita a hipótese nula (valor p: {pvalue_kruskal:.3f})")