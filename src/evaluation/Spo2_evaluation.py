"""
Documentation, License etc.

@package Spo2_evaluation
"""
import sys
sys.path.append('../..')
from spo2evaluation.evaluation import blant_altman
from argparse import ArgumentParser
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--data_file",
        dest="data_file",
        help="select file holding the data",
        metavar="FILE",
    )
    args = parser.parse_args()
    print("Launching the evaluatio for", args.data_file)

    results_df = pd.read_csv(args.data_file)


    # Extract Camera data
    Data_camera = results_df['spo2_pred']

    # Extract GT data
    Data_gt = results_df['spo2_gt']

    # Do statistical estimation
    least_square_slope_1, least_square_y_intercept_1, R_and_P_1 = blant_altman.Correlation(
        Data_camera, Data_gt
    )
    mean_difference_1, std_difference_1, upper_limit_1, lower_limit_1 = blant_altman.BlandAltmanPlot(
        Data_camera, Data_gt, fig_num=1
    )


if __name__ == "__main__":
    main()
