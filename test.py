import datetime
import logging

from configure import SDR
from DataSample import sample


def main():
    logging.basicConfig(filename='logs/{}.log'.format(datetime.datetime.now().strftime("%m-%d-%y_%H-%M-%S")),
                        encoding='utf-8', level=logging.DEBUG)


    logging.debug("Getting SDR Object")
    sdr = SDR()
    logging.debug("SDR Object {}".format(str(sdr)))
    logging.debug("Getting sample getter")
    sample_getter = sample(sdr)
    logging.debug("Sample getter {}".format(sample_getter))

    data = sample_getter.get(50)
    print(data)
    logging.debug("Got Data! - Size:{}".format(len(data)))




if __name__ == "__main__":
    main()
