import tkinter as tk

class AirConditionerApp:
    def __init__(self):
        self.temperature = 24
        self.powered_on = False

        self.root = tk.Tk()
        self.root.title("Control de Aire Acondicionado")

        self.temperature_label = tk.Label(self.root, text="Temperatura: {}°C".format(self.temperature))
        self.temperature_label.pack()

        self.power_button = tk.Button(self.root, text="Encender", command=self.toggle_power)
        self.power_button.pack()

        self.temperature_up_button = tk.Button(self.root, text="↑", command=self.increase_temperature)
        self.temperature_up_button.pack()

        self.temperature_down_button = tk.Button(self.root, text="↓", command=self.decrease_temperature)
        self.temperature_down_button.pack()

    def toggle_power(self):
        if self.powered_on:
            self.powered_on = False
            self.power_button.config(text="Encender")
        else:
            self.powered_on = True
            self.power_button.config(text="Apagar")

    def increase_temperature(self):
        if self.powered_on and self.temperature < 30:
            self.temperature += 1
            self.temperature_label.config(text="Temperatura: {}°C".format(self.temperature))

    def decrease_temperature(self):
        if self.powered_on and self.temperature > 16:
            self.temperature -= 1
            self.temperature_label.config(text="Temperatura: {}°C".format(self.temperature))

    def run(self):
        self.root.mainloop()

app = AirConditionerApp()
app.run()