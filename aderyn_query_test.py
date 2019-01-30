class AderynQueryTest:
    """QGIS Plugin Implementation."""

    def __init__(self):
       """Constructor"""

    def sqlQuery(self, parameter):
        """Test sql query """
        sqlTest = "SELECT * FROM lrc_wales_data.records LIMIT 1 OFFSET " + parameter
        self.sql = sqlTest
        return self.sql


