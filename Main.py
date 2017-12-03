from pyStats import Stats
from pprint import pprint;

number = [1,1,2,34,4,4,2,2,2,1,3,5,2,1,3];

print("Range =>",Stats.Range([13, 13, 13, 13, 14, 14, 16, 18, 21]))

print("Mode =>",Stats.Mode([13, 13, 13, 13, 14, 14, 16, 18, 21]))

freq = Stats.AllFrequencies(number);

pprint(freq)

mean = Stats.Mean([3,5,12]);

print("Mean =>",mean);

sd = Stats.StandardDeviation(number);

print("Standard Deviation =>",sd)

print("Mean Absolute Deviation =>",Stats.MedianAbsoluteDeviation([3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]))

data = ["cat","dog","dog","lion","gorilla","gorilla","dog","dog","dog","cat","donkey","chimpanzee","dog","cat","donkey"];

print("All Frequencies");
pprint(Stats.AllFrequencies(data));

print("A Frequency");
pprint(Stats.AFrequency(data,"dog"));

print("Some Frequencies");
pprint(Stats.SomeFrequencies(data,["dog","donkey","cat"]));
