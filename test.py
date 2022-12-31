from configure import SDR
from DataSample import sample


def main():
    sdr = SDR()
    sample_getter = sample(sdr)
    print(sample_getter.get(10))


if __name__ == "__main__":
    main()
