# ---------------------------------------------------
# Policy3 STEPS: Environment Separation Rules
#
# Feature file:
# env_separation.feature
#
# Class file: asset.py
# ---------------------------------------------------

from behave import *
from hamcrest import *
from asset import AssetEnvironment, AssetRiskFactor, AssetTier
import unittest


@given('all assets need to have assigned tiering tag')
def step_impl(context):
    pass


@when('a source asset resides in {src_tier}')
def source_tier(context, src_tier):
    pass

@when('a destination asset resides in {dst_tier}')
def dst_tier(context, dst_tier):
    pass


@then('communication between source and destination is considered {outcome}')
def tier_jump_decision(context, outcome):
    pass

