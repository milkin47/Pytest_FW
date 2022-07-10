import pytest

@pytest.mark.usefixtures("setup")
class Testfixture():
    def test_fixturedemo1(self):
        print("I will be executing inbetween 1")

    def test_fixturedemo2(self):
        print("I will be executing inbetween 2")

    def test_fixturedemo3(self):
        print("I will be executing inbetween 3")

    def test_fixturedemo4(self):
        print("I will be executing inbetween 4")

@pytest.mark.usefixtures("dataload")
class Testhomepage():
    def test_firstpage(self, dataload):
        print("dataload : ", dataload)

@pytest.mark.usefixtures("withparam")
def test_params(withparam):
    print(withparam)

