from pyStats import Stats
# from pprint import pprint;
# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt

number = [1,1,2,34,4,4,2,2,2,1,3,5,2,1,3];

print("Range =",Stats.Range([13, 13, 13, 13, 14, 14, 16, 18, 21]))

print("Mode =",Stats.Mode([13, 13, 13, 13, 14, 14, 16, 18, 21]))

# freq = AllFrequencies(number);
#
# pprint(freq)
#
# mean = Mean([3,5,12]);
#
# print("Mean =",mean);
#
# sd = StandardDeviation(number);
#
# print("Standard Deviation =",sd)
#
# print(MedianAbsoluteDeviation([3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]))


# names = [f.Value for f in freq]
# performance = [f.Occurance for f in freq]
#
# y = range(len(freq));
#
# plt.style.use("dark_background")
# plt.bar(y, performance, align='center')
# plt.xticks(y, names)
# plt.ylabel('Occurance')
# plt.title('Frequency of Elements in A List')
#
# plt.show()

# data = ["cat","dog","dog","lion","gorilla","gorilla","dog","dog","dog","cat","donkey","chimpanzee","dog","cat","donkey"];
#
# print("All Frequencies");
# pprint(AllFrequencies(data));
#
# print("A Frequency");
# pprint(AFrequency(data,"dog"));
#
# print("Some Frequencies");
# pprint(SomeFrequencies(data,["dog","donkey","cat"]));
