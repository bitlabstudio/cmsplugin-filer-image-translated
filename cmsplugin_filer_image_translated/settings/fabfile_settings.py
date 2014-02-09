"""Settings for the project's fabfile."""
# ============================================================================
# General settings
# ============================================================================

# This should be the folder name of your Django project
PROJECT_NAME = 'cmsplugin_filer_image_translated'

# This should be the name of the virtualenv on your local machine and on your
# servers
VENV_NAME = PROJECT_NAME

# You should keep db role and db name identical on your local machine and on
# your servers
DB_ROLE = PROJECT_NAME
DB_NAME = PROJECT_NAME
DB_DUMP_FILENAME = '{0}.dump'.format(PROJECT_NAME)

TEST_SETTINGS_PATH = 'cmsplugin_filer_image_translated.settings.test_settings'

# Set this to true if you want to execute makemessages during a deployment
MAKEMESSAGES_ON_DEPLOYMENT = True

# Set this to true if you want to execute compilemessages during a deployment
COMPILEMESSAGES_ON_DEPLOYMENT = True


# ============================================================================
# Set/override this in settings/local_settings.py (needs to be created first)
# ============================================================================

# This should be the superuser of your postgres installation. Usually this is
# either postgres or your login username.
# LOCAL_PG_ADMIN_ROLE = 'postgres'
# LOCAL_COVERAGE_PATH = os.path.join(os.path.dirname(__file__),
#                                    '../../coverage')
