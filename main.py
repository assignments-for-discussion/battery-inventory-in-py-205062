
def count_batteries_by_health(present_capacities):
  # declaring dictionary to store batteries count
  d = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  
  for i in present_capacities:
    # calculating SoH
    j = 100 * i/120

    # clasification
    if 80<=j<=100:
      d["healthy"]+=1
    elif 62<=j<80:
      d["exchange"]+=1
    else:
      d["failed"]+=1
      
  return d



def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70,70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
