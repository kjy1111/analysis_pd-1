import matplotlib.pyplot as plt


def graph_scatter(result_analysis):
    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)

    for index, result in enumerate(result_analysis):
        subplots[index].scatter(
            result['x'],
            result['y'])

    plt.show()