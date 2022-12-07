import sys
import pandas as pd
import json

test = sys.argv[1].capitalize()
property = sys.argv[2]
std = sys.argv[3]

output = "./table.txt"

browsers = ["chrome", "edge", "firefox"]
browser_names = {"chrome": "Google Chrome", "edge": "Microsoft Edge", "firefox": "Mozilla Firefox"}
frameworks = ["react", "angular", "vue", "blazor_aot", "blazor_noaot"]
framework_names = {"react": "React", "angular": "Angular", "vue": "Vue", "blazor_aot": "Blazor AOT", "blazor_noaot": "Blazor JIT"}

def get_best(browser):
  best_value = 999999
  best_framework = "NULL"
  for f in frameworks:
    path = f"./temp/{test}_{f}_{browser}.json"
    with open(path, "r") as json_file:
      json_data = json.load(json_file)
      if json_data[property] < best_value:
        best_value = json_data[property]
        best_framework = f
  return (best_framework, best_value)

print(get_best("chrome"))