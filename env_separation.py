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


@given('{e1} assets can only communicate with other assets in the same type of environment')
def step_impl(context, e1):
    context.asset = AssetEnvironment(e1)


@when('{e1} asset initiates a network L4 session with {e2} asset on {e3} port(s)')
def compare_environment_of_two_endpoints(context, e1, e2, e3):
    context.asset.environment_compare(e1, e2, e3)
    assert_that(all_of(context.asset.e1x, context.asset.e2x), is_not(None))
#    assert_that(context.asset.e2x, equal_to_ignoring_case(context.asset.e1x), 'Environment parameters mismatched')


@then('network connection is {outcome}')
def make_connection_decision(context, outcome):
    assert_that(context.asset.decision, is_not(None))

