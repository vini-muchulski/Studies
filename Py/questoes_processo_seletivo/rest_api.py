import requests
import math

def pulseRate(diagnosisName, doctorId):
  """
  Calculates the average pulse rate for patients with a specific diagnosis and doctor.

  Args:
    diagnosisName: The name of the diagnosis to search for.
    doctorId: The ID of the doctor.

  Returns:
    The average pulse rate of the selected patients truncated to an integer.
  """

  url = "https://jsonmock.hackerrank.com/api/medical_records"
  page = 1
  total_pages = 1
  pulse_rates = []

  while page <= total_pages:
    params = {"page": page}
    response = requests.get(url, params=params)
    data = response.json()

    total_pages = data['total_pages']

    for record in data['data']:
      if (record['diagnosis']['name'] == diagnosisName and 
              record['doctor']['id'] == doctorId):
              pulse_rates.append(record['vitals']['pulse'])

    page += 1

  if pulse_rates:
    average_pulse_rate = sum(pulse_rates) / len(pulse_rates)
    return math.trunc(average_pulse_rate)  # Truncate to an integer
  else:
    return 0  # Return 0 if no matching records found