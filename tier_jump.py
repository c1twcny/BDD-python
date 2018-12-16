# ---------------------------------------------------
# Policy3 STEPS: Environment Separation Rules
#
# Feature file:
# env_separation.feature
#
# Class file: asset.py
# ---------------------------------------------------
from pytest_bdd import *
from behave import *
from hamcrest import *
from asset import AssetEnvironment, AssetRiskFactor, AssetTier
import unittest


@given('all assets need to have assigned tiering tag')
def step_impl(context):
    context.asset_tier = AssetTier()


@when('a source asset resides in {src_tier}')
def source_tier(context, src_tier):
    context.asset_tier.network_tier(src_tier, '')


@when('a destination asset resides in {dst_tier}')
def dst_tier(context, dst_tier):
    context.asset_tier.network_tier(context.asset_tier.src_tier, dst_tier) # pass src_tier value from previous output


@then('communication between source and destination is considered {outcome}')
def tier_jump_decision(context, outcome):
    context.asset_tier.tier_jump(outcome)

