from locust import HttpUser, task, between
import random


class FDNHighVariationTest(HttpUser):
    wait_time = between(0.5, 1.5)

    def generate_random_payload(self):
        """
        Generate realistic heart-disease dataset variations.
        Each call produces a unique combination.
        """

        return {
            "age": random.randint(29, 80),
            "sex": random.randint(0, 1),
            "cp": random.randint(0, 3),
            "trestbps": random.randint(94, 200),
            "chol": random.randint(126, 564),
            "fbs": random.randint(0, 1),
            "restecg": random.randint(0, 2),
            "thalach": random.randint(71, 202),
            "exang": random.randint(0, 1),
            "oldpeak": round(random.uniform(0.0, 6.2), 1),
            "slope": random.randint(0, 2),
            "ca": random.randint(0, 4),
            "thal": random.randint(0, 3)
        }

    @task
    def test_fdn_randomized(self):
        payload = self.generate_random_payload()

        with self.client.post(
            "/predictsc",
            json=payload,
            name="FDN Random High Variation",
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"{response.status_code} | {response.text}")