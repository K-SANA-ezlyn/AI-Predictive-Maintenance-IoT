import matplotlib.pyplot as plt

def plot_sensor(df):
    plt.figure()
    plt.plot(df['time'], df['sensor2'])
    plt.title("Sensor Trend")
    plt.savefig("images/sensor_plot.png")
