"""
Functions:
    plot_elevation_statistics(stats: dict) -> None
"""

import matplotlib.pyplot as plt

class PlotResults:
    @staticmethod
    def plot_elevation_statistics(stats: dict) -> None:
        """
        Plots a bar chart of elevation statistics.
        Args:
            stats (dict): Dictionary with mean, median, and range values.
        """
        labels = list(stats.keys())
        values = list(stats.values())

        plt.bar(labels, values, color=['green', 'yellow', 'red'])
        plt.title("Elevation Statistics")
        plt.ylabel("Elevation (meters)")
        plt.xlabel("Statistic")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
