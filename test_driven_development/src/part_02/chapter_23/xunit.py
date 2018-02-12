class TestResult:

    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_startd(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return "{} run, {} failed".format(self.run_count, self.error_count)


class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        # result = TestResult()
        result.test_startd()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tearDown()
        # return result


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        # result = TestResult()
        for test in self.tests:
            test.run(result)
        # return result


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

    def setUp(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        # result = TestResult()
        test.run(self.result)
        assert("setUp test_method tearDown " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        # result = TestResult()
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        # result = TestResult()
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def test_failed_result_formatting(self):
        # result = TestResult()
        self.result.test_startd()
        self.result.test_failed()
        assert("1 run, 1 failed" == self.result.summary())

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        # result = TestResult()
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


# print(TestCaseTest("test_template_method").run().summary())
# print(TestCaseTest("test_result").run().summary())
# print(TestCaseTest("test_failed_result").run().summary())
# print(TestCaseTest("test_failed_result_formatting").run().summary())
# print(TestCaseTest("test_suite").run().summary())

suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_failed_result_formatting"))
suite.add(TestCaseTest("test_suite"))
result = TestResult()
suite.run(result)
print(result.summary())