class TestResult:

    def __init__(self):
        self.run_count = 0

    def test_startd(self):
        self.run_count += 1

    def summary(self):
        return "{} run, 0 failed".format(self.run_count)


class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.test_startd()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result


class WasRun(TestCase):

    def setUp(self):
        self.log = "setUp "

    def test_method(self):
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert("setUp test_method tearDown " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())


TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
# TestCaseTest("test_failed_result").run()
