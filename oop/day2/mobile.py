# class mobile:
#     def brand(self,brand):
#         return f"brand{brand}"
#
#     def model(self,model):
#

class laptop:
    def brand(self, brand):
        return f"brand {brand}"

    def model(self, model):
        return f"model {model}"

    def price(self, price):
        return f"model {price}"


class dell(laptop):
    def storage(self, storage):
        return f"storage{storage}"

    def ram(self, ram):
        return f"ram{ram}"


class mac(laptop):
    def graphics(self, graphics):
        return f"graphics{graphics}"


class hp(laptop):
    def drive(self, drive):
        return f"drive{drive}"


obj = dell()
print(obj.model("hp"))
