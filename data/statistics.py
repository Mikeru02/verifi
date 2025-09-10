class Statistics:
    __document_count = 0
    __total_size = 0
    __average_kb = 0
    __average_time = 0
    __recent_kb = 0
    __recent_time = 0
    __prediction_times = []

    @staticmethod
    def get_average_kb():
        return Statistics.__average_kb
    
    @staticmethod
    def get_average_time():
        return Statistics.__average_time
    
    @staticmethod
    def get_prediction_times():
        return Statistics.__prediction_times
    
    @staticmethod
    def get_document_count():
        return Statistics.__document_count
    
    @staticmethod
    def get_total_size():
        return Statistics.__total_size
    
    @staticmethod
    def get_recent_kb():
        return Statistics.__recent_kb
    
    @staticmethod
    def set_recent_kb(value):
        Statistics.__recent_kb = value
    
    @staticmethod
    def get_recent_time():
        return Statistics.__recent_time
    
    @staticmethod
    def set_recent_time(value):
        Statistics.__recent_time = value

    @staticmethod
    def add_document(size_kb, elapsed_time):
        Statistics.__recent_kb = size_kb
        Statistics.__recent_time = elapsed_time
        Statistics.__document_count += 1
        Statistics.__total_size += size_kb
        Statistics.__prediction_times.append(elapsed_time)

    @staticmethod
    def compute_average():
        if Statistics.__document_count > 0:
            Statistics.__average_kb = Statistics.__total_size / Statistics.__document_count
            Statistics.__average_time = sum(Statistics.__prediction_times) / len(Statistics.__prediction_times)
        return Statistics.__average_kb, Statistics.__average_time
