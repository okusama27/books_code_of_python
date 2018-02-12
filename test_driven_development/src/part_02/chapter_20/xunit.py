class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):

    # def __init__(self, name):
    #     self.was_run = None
    #     # self.name = name
    #     super().__init__(name)

    def setUp(self):
        self.was_run = None
        self.was_set_up = 1

    # def run(self):
    #     method = getattr(self, self.name)
    #     method()

    def test_method(self):
        self.was_run = 1


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert(self.test.was_run)
        test = WasRun("test_method")
        # assert(not test.was_run)
        test.run()
        assert(test.was_run)

    def test_set_up(self):
        self.test.run()
        assert(self.test.was_set_up)


TestCaseTest("test_running").run()
TestCaseTest("test_set_up").run()
