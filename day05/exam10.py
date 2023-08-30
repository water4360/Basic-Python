# 230830(수)
# 추상클래스abstract
from abc import *
class TV(metaclass=ABCMeta) :
    @abstractmethod # 추상메소드 annotation.
    def power_on(self) :
        pass

class LGTV(TV) :
    def power_on(self) :
        print('power ON...')

lgtv = LGTV()
lgtv.power_on()