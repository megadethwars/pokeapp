import statistics

class BerryModel:
    def __init__(self, berries_names, growth_times):
        self.berries_names = berries_names
        self.min_growth_time = min(growth_times)
        self.median_growth_time = float(format(float(statistics.median(growth_times)), ".0f"))
        self.max_growth_time = max(growth_times)
        self.variance_growth_time = round(statistics.variance(growth_times), 2)
        self.mean_growth_time = statistics.mean(growth_times)
        self.frequency_growth_time = self.calculate_frequency_growth_time(growth_times)

    def calculate_frequency_growth_time(self, growth_times):
        frequency_growth_time = {}
        for number in growth_times:
            if number in frequency_growth_time:
                frequency_growth_time[number] += 1
            else:
                frequency_growth_time[number] = 1
        return frequency_growth_time
