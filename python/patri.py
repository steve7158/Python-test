import matplotlib.pyplot as plt
slices_hours = [70, 2,28]
activities = ['yes', 'no', 'maybe']
colors = ['r', 'g', 'b']
plt.title("If we follow fundametal duties then we are patriotic?")
plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()
