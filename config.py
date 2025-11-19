# configuration file containing confidential credentials
# user authentication password is used to login to the application
# edit mode password is required to add, delete or update any patient, doctor or department record 
# doctor/medical lab scientist (MLS) access code is given only to the doctors and MLSs, using which they can add, delete or update any prescription and/or medical test record

password = '1234'                               # e.g. password = '1234'
database_name = 'database_1A'                                 # e.g. database_name = 'database_1A'
edit_mode_password = 'allow_edit'                               # e.g. edit_mode_password = 'allow_edit'
dr_mls_access_code = 'access_auth'      # e.g. dr_mls_access_code = 'access_auth'
# ---------------------------------------------------------------------------
# Personal Injury & Healthcare System Configuration
# ---------------------------------------------------------------------------

# This section contains configuration values that are specific to the
# personal injury and provider management adaptation of the existing
# healthcare information system.

PERSONAL_INJURY_FEATURES_ENABLED = True

# This flag can be used later to conditionally enable personal injury
# specific workflows, reporting, or UI elements.
MARKETING_ANALYTICS_ENABLED = True

# Placeholder for the environment (e.g., "development", "staging", "production").
# This can be used to control logging or database settings later.
APPLICATION_ENVIRONMENT = "development"
