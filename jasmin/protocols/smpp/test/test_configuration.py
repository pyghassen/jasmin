"""
Test cases for jasmin.protocols.smpp.configs module.
"""

from twisted.trial.unittest import TestCase
from jasmin.protocols.smpp.configs import SMPPClientConfig
from jasmin.protocols.smpp.configs import ConfigUndefinedIdError, ConfigInvalidIdError

class SMPPClientConfigTest(TestCase):
    def test_id_is_mandatory(self):
        self.assertRaises(ConfigUndefinedIdError, SMPPClientConfig)
        
    def test_id_syntax_validation(self):
        invalidIds = [ 'zzz s', '', 'a,', 'r#r', '9a', '&"()=+~#{[|\`\^@]}', 'a123456789012345678901234-', 'aa']
        
        for invalidId in invalidIds:
            self.assertRaises(ConfigInvalidIdError, SMPPClientConfig, id=invalidId)