import collect
import analyze
import visualize
from config import CONFIG
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    resultfiles = dict()

    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    # 1. analysis and visualize
    # result_analysis = analyze.analysis_correlation(resultfiles)
    # visualize.graph_scatter(result_analysis)

    # 2. analysis and visualize
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)

    graph_table = pd.DataFrame(result_analysis, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tourspot')

    graph_table.plot(kind='bar')
    plt.show()