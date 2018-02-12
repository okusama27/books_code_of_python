class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):

    def setUp(self):
        # self.was_run = None
        # self.was_set_up = 1
        self.log = "setUp "

    def test_method(self):
        # self.was_run = 1
        self.log = self.log + "test_method "

    def tearDown(self):
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):

    # def setUp(self):
    #     self.test = WasRun("test_method")

    # def test_running(self):
    #     self.test.run()
    #     assert(self.test.was_run)
    #     test = WasRun("test_method")
    #     # assert(not test.was_run)
    #     test.run()
    #     assert(test.was_run)

    def test_template_method(self):
        # self.test.run()
        # assert("setUp test_method")
        test = WasRun("test_method")
        test.run()
        assert("setUp test_method tearDown " == test.log)

    # def test_set_up(self):
    #     self.test.run()
    #     # assert(self.test.was_set_up)
    #     assert("setUp test_method " == self.test.log)

TestCaseTest("test_template_method").run()
# TestCaseTest("test_set_up").run()
