# HERE WE GONNA TO CREATE AN INITIALIZE OUR BLUEPRINT

from flask import Blueprint  # WE NEED TO IMPORT THE BLUEPRINT CLASS


main = Blueprint('main', __name__)  # HERE WE USE 'MAIN' TO REPRESENT OUR BLUEPRINT, THIS NEEDS TWO ARGUMENTS
# THE NAME OF THE BLUEPRINT AND THE MODULE OR THE PACKAGE WHERE THE BLUEPRINT IS LOCATED.


