from nbresult import ChallengeResultTestCase

class TestPreprocBaseline(ChallengeResultTestCase):

    def test_shape(self):
        self.assertNotEqual(self.result.shape[1], 183,
                            msg="Too many columns. Remember to drop the second column when encoding binary features.")
        self.assertEqual(self.result.shape, (1460, 179))
