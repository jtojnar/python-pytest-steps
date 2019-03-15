from pytest_steps.steps import test_steps, cross_steps_fixture, CROSS_STEPS_MARK
from pytest_steps.steps_generator import optional_step, one_fixture_per_step
from pytest_steps.steps_parametrizer import StepsDataHolder, depends_on

__all__ = [
    # the submodules
    'steps', 'steps_generator', 'steps_parametrizer', 'steps_harvest',
    'steps_harvest_df_utils',
    # all symbols imported above
    # -- for fixtures
    'cross_steps_fixture', 'CROSS_STEPS_MARK',
    # -- for tests
    'test_steps',
    # ---- specific to parametrizer mode
    'StepsDataHolder', 'depends_on',
    # ---- specific to generator mode
    'optional_step', 'one_fixture_per_step'
    ]

try:
    from pytest_harvest import get_all_pytest_fixture_names
except ImportError:
    # pytest-harvest is not installed
    pass
else:
    from pytest_steps.steps_harvest import handle_steps_in_results_dct, remove_step_from_test_id, \
        get_all_pytest_param_names_except_step_id
    from pytest_steps.steps_harvest_df_utils import pivot_steps_on_df, get_flattened_multilevel_columns, \
        flatten_multilevel_columns, handle_steps_in_results_df

    __all__ = __all__ + [
        # harvest-related
        'handle_steps_in_results_dct', 'remove_step_from_test_id', 'get_all_pytest_param_names_except_step_id',
        'pivot_steps_on_df', 'get_flattened_multilevel_columns', 'flatten_multilevel_columns',
        'handle_steps_in_results_df'
    ]
