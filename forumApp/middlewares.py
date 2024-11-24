import time

from django.utils.deprecation import MiddlewareMixin


def measure_time_execution(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request, *args, **kwargs)
        end_time = time.time()

        print(f"Total time needed for execution was {end_time - start_time}")
        return response

    return middleware


class MeasureTimeExecution(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()



    def process_response(self, request, response):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f"New class measure time: {total_time}")
        return response