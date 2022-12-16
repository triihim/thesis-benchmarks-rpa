import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

plt.style.use("ggplot")

test_avg = bool(sys.argv[1])
property = sys.argv[2]
y_label = sys.argv[3]

# If test_avg flag is true, calculate the average instead of total.
divisor = 1
if test_avg > 0:
  divisor = 3 # Test count

browsers = ["chrome", "edge", "firefox"]
browser_names = {"chrome": "Google Chrome", "edge": "Microsoft Edge", "firefox": "Mozilla Firefox"}
frameworks = ["react", "angular", "vue", "blazor_aot", "blazor_noaot"]
framework_names = {"react": "React", "angular": "Angular", "vue": "Vue", "blazor_aot": "Blazor AOT", "blazor_noaot": "Blazor JIT"}
tests = ["Render", "Update", "Remove"]

def get_property_sum(framework, browser):
  property_sum = 0
  for t in tests:
    fp = f"./temp/{t}_{framework}_{browser}.json"
    with open(fp, "r") as json_file:
      json_data = json.load(json_file)
      property_sum += json_data[property]
  return round(property_sum)

def get_framework_data(framework):
  data = []
  for b in browsers:
    data.append(get_property_sum(framework, b))
  return data

x_indexes = np.arange(len(browser_names))
x_labels = ["Google Chrome", "Microsoft Edge", "Mozilla Firefox"]
bar_width = 0.15

fig = plt.figure()
ax = plt.subplot()

react_data = get_framework_data("react")
angular_data = get_framework_data("angular")
vue_data = get_framework_data("vue")
blazor_aot_data = get_framework_data("blazor_aot")
blazor_noaot_data = get_framework_data("blazor_noaot")

react_bar = ax.bar(x_indexes - 2*bar_width, react_data, width=bar_width, label="React", color="#61DBFB")
ax.bar_label(react_bar, react_data, rotation=90, label_type="center", color="white")
angular_bar = ax.bar(x_indexes - bar_width, angular_data, width=bar_width, label="Angular", color="#DD0031")
ax.bar_label(angular_bar, angular_data, rotation=90, label_type="center", color="white")
vue_bar = ax.bar(x_indexes, vue_data, width=bar_width, label="Vue", color="#42b883")
ax.bar_label(vue_bar, vue_data, rotation=90, label_type="center", color="white")
blazor_aot_bar = ax.bar(x_indexes + bar_width, blazor_aot_data, width=bar_width, label="Blazor AOT", color="#562B88")
ax.bar_label(blazor_aot_bar, blazor_aot_data, rotation=90, label_type="center", color="white")
blazor_noaot_bar = ax.bar(x_indexes + 2*bar_width, blazor_noaot_data, width=bar_width, label="Blazor JIT", color="#CE3EE5")
ax.bar_label(blazor_noaot_bar, blazor_noaot_data, rotation=90, label_type="center", color="white")

ax.set_xticks(x_indexes, x_labels)
ax.legend(facecolor='white', framealpha=1, loc="upper left")

ax.set_title(property)
ax.set_ylabel(y_label)


fig.add_subplot(ax)
fig.show()
plt.show()
