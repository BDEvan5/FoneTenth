import glob
import numpy as np



def KernelValidationRandom():
    folder = "Data/Vehicles/KernelValidationRandom/"

    map_names = ["f1_aut_wide", "f1_mco", "f1_esp"]
    slow_agents = [f"Slow_Rando_Super_{map_name}_1_0" for map_name in map_names]
    fast_agents = [f"Fast_Rando_Super_{map_name}_1_0" for map_name in map_names]
    
    print_maps = ["WAUT", "MCO", "ESP"]
    metrics = ["No. of Interventions per Lap", "Intervention Rate (\%)"]
    metric_inds = [-3, -2]

    data_slow, data_std_slow = [[] for _ in metrics], [[] for _ in metrics]
    data_fast, data_std_fast = [[] for _ in metrics], [[] for _ in metrics]
    
    for agent in slow_agents:
        with open(folder + f"{agent}/TestingSummaryStatistics.txt", 'r') as file:
            lines = file.readlines()
            line = lines[2] # first lap is heading
            line = line.split(',')
            for i in range(len(metrics)):
                metric_data = float(line[metric_inds[i]])
                data_slow[i].append(metric_data)
            line = lines[3] # first lap is heading
            line = line.split(',')
            for i in range(len(metrics)):
                metric_data = float(line[metric_inds[i]])
                data_std_slow[i].append(metric_data)

    for agent in fast_agents:
        with open(folder + f"{agent}/TestingSummaryStatistics.txt", 'r') as file:
            lines = file.readlines()
            line = lines[2] # first lap is heading
            line = line.split(',')
            for i in range(len(metrics)):
                metric_data = float(line[metric_inds[i]])
                data_fast[i].append(metric_data)
            line = lines[3] # first lap is heading
            line = line.split(',')
            for i in range(len(metrics)):
                metric_data = float(line[metric_inds[i]])
                data_std_fast[i].append(metric_data)

    with open(folder + f"RandoPaperMetrics.txt", 'w') as file:
        file.write(f"\\toprule \n")
        file.write(" &  \multicolumn{2}{c}{\\textit{Slow}}  & &  \multicolumn{2}{c}{\\textit{Fast}}  \\\\ \n")
        file.write(" \cmidrule(lr){2-3} \n")
        file.write(" \cmidrule(lr){5-6} \n")
        file.write("\\textbf{Metric} & \\textbf{ " + " } &  \\textbf{ ".join(metrics) + "} & {" + "} & \\textbf{ " + " } &  \\textbf{ ".join(metrics) + "}   \\\\ \n")
        file.write(f"\\midrule \n")
        for i in range(len(print_maps)):
            file.write(f"{print_maps[i]} ".ljust(20))
            for j in range(len(metrics)):
                file.write(f"& {data_slow[j][i]:.1f} $\pm$  {data_std_slow[j][i]:.1f}  ".ljust(25))
            file.write(" & ")
            for j in range(len(metrics)):
                file.write(f"& {data_fast[j][i]:.1f} $\pm$  {data_std_fast[j][i]:.1f}  ".ljust(25))
            file.write("\\\\ \n")
        file.write(f"\\bottomrule \n")


def KernelValidationPP():
    folder = "Data/Vehicles/KernelValidationPP/"

    map_name = "f1_mco"
    speeds = [4, 6, 8]
    std_agents = [f"Fast_PP_Std_{map_name}_{i}_1_0" for i in speeds]
    super_agents = [f"Fast_PP_Super_{map_name}_{i}_1_0" for i in speeds]
    
    print_names = speeds
    metrics_std = ["Lap Time (s)", "Avg. Velocity (m/s)"]
    metrics_super = ["No. Interventions", "Lap Time (s)", "Avg. Velocity (m/s)"]
    std_metric_inds = [8, 9]
    super_metric_inds = [-3, 8, 9]

    data_std = [[] for _ in metrics_std]
    data_super = [[] for _ in metrics_super]

    for agent in std_agents:
        with open(folder + f"{agent}/TestingSummaryStatistics.txt", 'r') as file:
            lines = file.readlines()
            line = lines[2] # first lap is heading
            line = line.split(',')
            for i in range(len(metrics_std)):
                metric_data = float(line[std_metric_inds[i]])
                data_std[i].append(metric_data)
    
    for agent in super_agents:
        with open(folder + f"{agent}/TestingSummaryStatistics.txt", 'r') as file:
            lines = file.readlines()
            line = lines[2] # first lap is heading
            line = line.split(',')
            for i in range(len(metrics_super)):
                metric_data = float(line[super_metric_inds[i]])
                data_super[i].append(metric_data)

    with open(folder + f"KernelValidationPP_{map_name}.txt", 'w') as file:
        file.write(f"\\toprule \n")
        file.write(" &  \multicolumn{2}{c}{\\textit{Pure Pursuit}}  & &  \multicolumn{3}{c}{\\textit{Pure Pursuit with SSS}}  \\\\ \n")
        file.write("\\cmidrule(lr){2-3} \n")
        file.write("\\cmidrule(lr){5-7} \n")
        file.write("\\textbf{Max Speed} & \\textbf{ " + " } &  \\textbf{ ".join(metrics_std) + "} & {" + "} & \\textbf{ " + " } &  \\textbf{ ".join(metrics_super) + "}   \\\\ \n")
        file.write(f"\\midrule \n")
        for i in range(len(print_names)):
            file.write(f"{print_names[i]} ".ljust(20))
            for j in range(len(metrics_std)):
                file.write(f"& {data_std[j][i]:.1f}   ".ljust(15))
            file.write(" & ")
            for j in range(len(metrics_super)):
                file.write(f"& {data_super[j][i]:.1f}   ".ljust(15))
            file.write("\\\\ \n")
        file.write(f"\\bottomrule \n")



# KernelValidationRandom()
KernelValidationPP()


