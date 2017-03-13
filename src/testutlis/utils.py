from django.test import TestCase


class TestBase(TestCase):

    """Test base Have assertContent method for easy test multiple contents"""

    def assertContents(self, contents):
        for expected_content in contents:
            with self.subTest():
                self.assertContains(self.response, expected_content)


class TestFormBase(TestBase):
    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

