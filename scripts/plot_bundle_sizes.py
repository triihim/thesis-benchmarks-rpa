import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.style.use("ggplot")

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

frameworks = ["React", "Angular", "Vue", "Blazor AOT", "Blazor NOAOT"]
first_load = np.array([0.142, 0.142, 0.799, 13.1, 2.7])
second_load = np.array([0.142, 0.142, 0.799, 0.349, 0.312])

visits = 100

cumulative = np.around(first_load + ((visits-1) * second_load), 2)

x_index = np.arange(len(frameworks))

fig = plt.figure()

first_load_plot = fig.add_subplot(3,1,1)
second_load_plot = fig.add_subplot(3,1,2)
cumulative_load_plot = fig.add_subplot(3,1,3)

first_cont = first_load_plot.bar(x_index, first_load, color=["#61DBFB", "#DD0031", "#42b883", "#562B88", "#CE3EE5"])
first_load_plot.bar_label(first_cont, first_load)
first_load_plot.set_title("Ensimmäinen lataus")
first_load_plot.set_ylim(0, 15)
first_load_plot.set_xticks(x_index, frameworks)

second_cont = second_load_plot.bar(x_index, second_load, color=["#61DBFB", "#DD0031", "#42b883", "#562B88", "#CE3EE5"])
second_load_plot.bar_label(second_cont, second_load)
second_load_plot.set_title("Toinen lataus")
second_load_plot.set_ylim(0, 1)
second_load_plot.set_xticks(x_index, frameworks)

cumulative_cont = cumulative_load_plot.bar(x_index, cumulative, color=["#61DBFB", "#DD0031", "#42b883", "#562B88", "#CE3EE5"])
cumulative_load_plot.bar_label(cumulative_cont, cumulative)
cumulative_load_plot.set_title(f"Kumulatiiviset {visits} latausta")
cumulative_load_plot.set_ylim(0, 100)
cumulative_load_plot.set_xticks(x_index, frameworks)

fig.supylabel("Tiedonsiirto (MB)")
fig.suptitle("Testisovellusten edellyttämä tiedonsiirto", y=1, fontsize=16)
fig.tight_layout()
fig.savefig("./bundlesize.pgf")

