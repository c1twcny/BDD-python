# ----------------------------------------------------
# Class file for cac.py
#
# BDD Feature:
# env_separation.feature
# tier_jump.feature
# ----------------------------------------------------
from hamcrest import *
import unittest

# ----------------------------------------------------
# AssetEnvironment
# ----------------------------------------------------
class AssetEnvironment():
    def __init__(self, asset_env):
        self.environment = asset_env
        self.env_prod = ['prod', 'dr']
        self.env_nonprod = ['non-prod', 'uat', 'dev', 'qa', 'lab']
        assert_that(self.environment, is_not(None), 'Environment variable is not defined')


    def environment_compare(self, e1, e2, e3):
        self.e1, self.e2, self.e3 = e1, e2, e3
        self.e1x, self.e2x, self.e3x = None, None, None
        self.env_pair = [self.e1, self.e2]

        if (self.e1 in self.env_prod):
            self.e1x = 'PROD'
        else:
            self.e1x = 'non-PROD'

        if (self.e2 in self.env_prod):
            self.e2x = 'PROD'
        else:
            self.e2x = 'non-PROD'

        if (self.e1x == self.e2x):
            return('Inside: Environment matched', self.e1x, self.e2x)
        else:
            return('Inside: Environment mismatched', self.e1x, self.e2x)


    def decision(self, outcome):
        self.outcome = None
        if all(x in self.env_prod for x in self.env_pair) or all(x in self.env_nonprod for x in self.env_pair):
            if (self.e3x == 'permitted'):
                self.outcome = 'allowed'
            else:
                self.outcome = 'denied'
        else:
            self.outcome = 'denied'

        return(self.outcome)

# ----------------------------------------------------
# AssetRiskFactor()
# PII: Y/N
# CAF: Y/N
# ----------------------------------------------------
class AssetRiskFactor():
    def risk_pii(self, flag_pii):
        self.flag_pii = flag_pii
        assert_that(self.flag_pii, is_not(None))

    def risk_caf(self, flag_caf):
        self.flag_caf = flag_caf
        assert_that(self.flag_caf, is_not(None))


# ----------------------------------------------------
# AssetTier()
# network tiering: [0, 1, 2, 3]
#
# ----------------------------------------------------
class AssetTier():
    def network_tier(self, src_tier, dst_tier):
        self.src_tier, self.dst_tier = src_tier, dst_tier
        assert_that(all_of(src_tier, dst_tier), is_not(None))