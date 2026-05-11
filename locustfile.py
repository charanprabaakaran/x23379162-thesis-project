from locust import HttpUser, task, between
import time
import random


class SimpleFDNTest(HttpUser):
    data1 = {
    'age': 45, 'sex': 1, 'cp': 2, 'trestbps': 130,
    'chol': 250, 'fbs': 0, 'restecg': 1, 'thalach': 150,
    'exang': 1, 'oldpeak': 2.3, 'slope': 1, 'ca': 0, 'thal': 2
    }

    data2 = {
        'age': 55, 'sex': 2, 'cp': 2, 'trestbps': 129,
        'chol': 230, 'fbs': 0, 'restecg': 1, 'thalach': 150,
        'exang': 1, 'oldpeak': 2.1, 'slope': 1, 'ca': 0, 'thal': 2
    }

    data3 = {
        'age': 66, 'sex': 1, 'cp': 1, 'trestbps': 119,
        'chol': 232, 'fbs': 0, 'restecg': 1, 'thalach': 150,
        'exang': 1, 'oldpeak': 2.1, 'slope': 1, 'ca': 0, 'thal': 2
    }

    data4 = {
        'age': 69, 'sex': 2, 'cp': 2, 'trestbps': 119,
        'chol': 242, 'fbs': 0, 'restecg': 2, 'thalach': 144,
        'exang': 1, 'oldpeak': 2.1, 'slope': 2, 'ca': 0, 'thal': 2
    }

    data5 = {
        'age': 80, 'sex': 2, 'cp': 1, 'trestbps': 139,
        'chol': 242, 'fbs': 1, 'restecg': 2, 'thalach': 134,
        'exang': 1, 'oldpeak': 2.1, 'slope': 2, 'ca': 0, 'thal': 2
    }

    data6 = {
        'age': 52, 'sex': 1, 'cp': 3, 'trestbps': 128,
        'chol': 220, 'fbs': 0, 'restecg': 0, 'thalach': 160,
        'exang': 0, 'oldpeak': 1.4, 'slope': 1, 'ca': 0, 'thal': 3
    }

    data7 = {
        'age': 60, 'sex': 2, 'cp': 4, 'trestbps': 145,
        'chol': 260, 'fbs': 1, 'restecg': 2, 'thalach': 120,
        'exang': 1, 'oldpeak': 3.0, 'slope': 3, 'ca': 1, 'thal': 2
    }

    data8 = {
        'age': 47, 'sex': 1, 'cp': 1, 'trestbps': 135,
        'chol': 210, 'fbs': 0, 'restecg': 1, 'thalach': 170,
        'exang': 0, 'oldpeak': 0.9, 'slope': 1, 'ca': 0, 'thal': 3
    }

    data9 = {
        'age': 58, 'sex': 2, 'cp': 2, 'trestbps': 150,
        'chol': 280, 'fbs': 1, 'restecg': 2, 'thalach': 130,
        'exang': 1, 'oldpeak': 2.8, 'slope': 2, 'ca': 1, 'thal': 2
    }

    data10 = {
        'age': 62, 'sex': 1, 'cp': 3, 'trestbps': 120,
        'chol': 200, 'fbs': 0, 'restecg': 1, 'thalach': 160,
        'exang': 0, 'oldpeak': 1.0, 'slope': 1, 'ca': 0, 'thal': 3
    }

    data11 = {
        'age': 50, 'sex': 2, 'cp': 2, 'trestbps': 125,
        'chol': 240, 'fbs': 0, 'restecg': 0, 'thalach': 155,
        'exang': 0, 'oldpeak': 1.3, 'slope': 1, 'ca': 0, 'thal': 2
    }

    data12 = {
        'age': 70, 'sex': 1, 'cp': 4, 'trestbps': 160,
        'chol': 290, 'fbs': 1, 'restecg': 2, 'thalach': 110,
        'exang': 1, 'oldpeak': 3.5, 'slope': 3, 'ca': 2, 'thal': 1
    }

    data13 = {
        'age': 42, 'sex': 1, 'cp': 3, 'trestbps': 130,
        'chol': 210, 'fbs': 0, 'restecg': 1, 'thalach': 175,
        'exang': 0, 'oldpeak': 0.8, 'slope': 1, 'ca': 0, 'thal': 3
    }

    data14 = {
        'age': 64, 'sex': 2, 'cp': 2, 'trestbps': 138,
        'chol': 270, 'fbs': 1, 'restecg': 1, 'thalach': 125,
        'exang': 1, 'oldpeak': 2.5, 'slope': 2, 'ca': 1, 'thal': 2
    }

    data15 = {
        'age': 53, 'sex': 1, 'cp': 1, 'trestbps': 132,
        'chol': 240, 'fbs': 0, 'restecg': 0, 'thalach': 155,
        'exang': 0, 'oldpeak': 1.2, 'slope': 1, 'ca': 0, 'thal': 3
    }

    import random
    @task(1)
    def test_cache_behavior(self):
        """Always send the same exact data"""
        start_time = time.time()
        
        with self.client.post(
            "/predictsc", 
            data=self.random.choice([
                self.data1,
                self.data2,
                self.data3,
                self.data4,
                self.data5,
                self.data6,
                self.data7,
                self.data8,
                self.data9,
                self.data10,
                self.data11,
                self.data12,
                self.data13,
                self.data14,
                self.data15
            ]),
            catch_response=True,
            name="FDN Locust Test"
        ) as response:
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                response.success()
                print(f"Response: {response_time:.3f}s")
            else:
                response.failure(f"Failed: {response.status_code}")



# from locust import HttpUser, task, between
# import time
# import random


# class SimpleFDNTest(HttpUser):
#     wait_time = between(0.5, 1.5)

#     data_samples = [

#         {'age': 45, 'sex': 1, 'cp': 2, 'trestbps': 130, 'chol': 250, 'fbs': 0, 'restecg': 1, 'thalach': 150, 'exang': 1, 'oldpeak': 2.3, 'slope': 1, 'ca': 0, 'thal': 2},
#         {'age': 55, 'sex': 2, 'cp': 2, 'trestbps': 129, 'chol': 230, 'fbs': 0, 'restecg': 1, 'thalach': 150, 'exang': 1, 'oldpeak': 2.1, 'slope': 1, 'ca': 0, 'thal': 2},
#         {'age': 66, 'sex': 1, 'cp': 1, 'trestbps': 119, 'chol': 232, 'fbs': 0, 'restecg': 1, 'thalach': 150, 'exang': 1, 'oldpeak': 2.1, 'slope': 1, 'ca': 0, 'thal': 2},
#         {'age': 69, 'sex': 2, 'cp': 2, 'trestbps': 119, 'chol': 242, 'fbs': 0, 'restecg': 2, 'thalach': 144, 'exang': 1, 'oldpeak': 2.1, 'slope': 2, 'ca': 0, 'thal': 2},
#         {'age': 80, 'sex': 2, 'cp': 1, 'trestbps': 139, 'chol': 242, 'fbs': 1, 'restecg': 2, 'thalach': 134, 'exang': 1, 'oldpeak': 2.1, 'slope': 2, 'ca': 0, 'thal': 2},
#         {'age': 52, 'sex': 1, 'cp': 3, 'trestbps': 128, 'chol': 220, 'fbs': 0, 'restecg': 0, 'thalach': 160, 'exang': 0, 'oldpeak': 1.4, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 60, 'sex': 2, 'cp': 4, 'trestbps': 145, 'chol': 260, 'fbs': 1, 'restecg': 2, 'thalach': 120, 'exang': 1, 'oldpeak': 3.0, 'slope': 3, 'ca': 1, 'thal': 2},
#         {'age': 47, 'sex': 1, 'cp': 1, 'trestbps': 135, 'chol': 210, 'fbs': 0, 'restecg': 1, 'thalach': 170, 'exang': 0, 'oldpeak': 0.9, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 58, 'sex': 2, 'cp': 2, 'trestbps': 150, 'chol': 280, 'fbs': 1, 'restecg': 2, 'thalach': 130, 'exang': 1, 'oldpeak': 2.8, 'slope': 2, 'ca': 1, 'thal': 2},
#         {'age': 62, 'sex': 1, 'cp': 3, 'trestbps': 120, 'chol': 200, 'fbs': 0, 'restecg': 1, 'thalach': 160, 'exang': 0, 'oldpeak': 1.0, 'slope': 1, 'ca': 0, 'thal': 3},

#         {'age': 50, 'sex': 2, 'cp': 2, 'trestbps': 125, 'chol': 240, 'fbs': 0, 'restecg': 0, 'thalach': 155, 'exang': 0, 'oldpeak': 1.3, 'slope': 1, 'ca': 0, 'thal': 2},
#         {'age': 70, 'sex': 1, 'cp': 4, 'trestbps': 160, 'chol': 290, 'fbs': 1, 'restecg': 2, 'thalach': 110, 'exang': 1, 'oldpeak': 3.5, 'slope': 3, 'ca': 2, 'thal': 1},
#         {'age': 42, 'sex': 1, 'cp': 3, 'trestbps': 130, 'chol': 210, 'fbs': 0, 'restecg': 1, 'thalach': 175, 'exang': 0, 'oldpeak': 0.8, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 64, 'sex': 2, 'cp': 2, 'trestbps': 138, 'chol': 270, 'fbs': 1, 'restecg': 1, 'thalach': 125, 'exang': 1, 'oldpeak': 2.5, 'slope': 2, 'ca': 1, 'thal': 2},
#         {'age': 53, 'sex': 1, 'cp': 1, 'trestbps': 132, 'chol': 240, 'fbs': 0, 'restecg': 0, 'thalach': 155, 'exang': 0, 'oldpeak': 1.2, 'slope': 1, 'ca': 0, 'thal': 3},

#         {'age': 49, 'sex': 1, 'cp': 2, 'trestbps': 128, 'chol': 235, 'fbs': 0, 'restecg': 1, 'thalach': 162, 'exang': 0, 'oldpeak': 1.5, 'slope': 2, 'ca': 0, 'thal': 2},
#         {'age': 57, 'sex': 2, 'cp': 3, 'trestbps': 140, 'chol': 260, 'fbs': 1, 'restecg': 2, 'thalach': 140, 'exang': 1, 'oldpeak': 2.0, 'slope': 2, 'ca': 1, 'thal': 2},
#         {'age': 61, 'sex': 1, 'cp': 4, 'trestbps': 150, 'chol': 300, 'fbs': 1, 'restecg': 2, 'thalach': 115, 'exang': 1, 'oldpeak': 3.2, 'slope': 3, 'ca': 2, 'thal': 1},
#         {'age': 44, 'sex': 2, 'cp': 1, 'trestbps': 118, 'chol': 210, 'fbs': 0, 'restecg': 0, 'thalach': 172, 'exang': 0, 'oldpeak': 0.6, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 68, 'sex': 1, 'cp': 2, 'trestbps': 145, 'chol': 275, 'fbs': 1, 'restecg': 1, 'thalach': 128, 'exang': 1, 'oldpeak': 2.7, 'slope': 2, 'ca': 1, 'thal': 2},

#         {'age': 46, 'sex': 1, 'cp': 3, 'trestbps': 134, 'chol': 220, 'fbs': 0, 'restecg': 1, 'thalach': 168, 'exang': 0, 'oldpeak': 1.0, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 59, 'sex': 2, 'cp': 4, 'trestbps': 155, 'chol': 310, 'fbs': 1, 'restecg': 2, 'thalach': 118, 'exang': 1, 'oldpeak': 3.1, 'slope': 3, 'ca': 2, 'thal': 1},
#         {'age': 63, 'sex': 1, 'cp': 2, 'trestbps': 142, 'chol': 265, 'fbs': 0, 'restecg': 1, 'thalach': 135, 'exang': 1, 'oldpeak': 2.4, 'slope': 2, 'ca': 1, 'thal': 2},
#         {'age': 48, 'sex': 2, 'cp': 1, 'trestbps': 122, 'chol': 215, 'fbs': 0, 'restecg': 0, 'thalach': 178, 'exang': 0, 'oldpeak': 0.7, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 72, 'sex': 1, 'cp': 3, 'trestbps': 165, 'chol': 295, 'fbs': 1, 'restecg': 2, 'thalach': 105, 'exang': 1, 'oldpeak': 3.6, 'slope': 3, 'ca': 2, 'thal': 1},

#         {'age': 54, 'sex': 1, 'cp': 2, 'trestbps': 136, 'chol': 245, 'fbs': 0, 'restecg': 1, 'thalach': 150, 'exang': 0, 'oldpeak': 1.6, 'slope': 2, 'ca': 0, 'thal': 2},
#         {'age': 67, 'sex': 2, 'cp': 4, 'trestbps': 158, 'chol': 285, 'fbs': 1, 'restecg': 2, 'thalach': 112, 'exang': 1, 'oldpeak': 3.3, 'slope': 3, 'ca': 2, 'thal': 1},
#         {'age': 43, 'sex': 1, 'cp': 1, 'trestbps': 124, 'chol': 205, 'fbs': 0, 'restecg': 0, 'thalach': 182, 'exang': 0, 'oldpeak': 0.5, 'slope': 1, 'ca': 0, 'thal': 3},
#         {'age': 65, 'sex': 2, 'cp': 3, 'trestbps': 148, 'chol': 275, 'fbs': 1, 'restecg': 1, 'thalach': 122, 'exang': 1, 'oldpeak': 2.9, 'slope': 2, 'ca': 1, 'thal': 2},
#         {'age': 51, 'sex': 1, 'cp': 2, 'trestbps': 130, 'chol': 235, 'fbs': 0, 'restecg': 1, 'thalach': 158, 'exang': 0, 'oldpeak': 1.1, 'slope': 1, 'ca': 0, 'thal': 2}
#     ]

#     @task
#     def test_cache_behavior(self):
#         payload = random.choice(self.data_samples)

#         with self.client.post(
#             "/predictsc",
#             json=payload,
#             name="FDN Locust Test",
#             catch_response=True
#         ) as response:
#             if response.status_code == 200:
#                 response.success()
#             else:
#                 response.failure(f"Failed: {response.status_code}")