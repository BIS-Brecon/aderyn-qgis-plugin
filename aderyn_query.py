class AderynQuery:
    """QGIS Plugin Implementation."""

    def __init__(self):
       """Constructor"""

    def sqlQueryTest(self, parameter):
        """Test sql query """
        sqlTest = "SELECT * FROM lrc_wales_data.records LIMIT 1 OFFSET " + parameter
        self.sql = sqlTest
        return self.sql

    def sqlQuery(self, category, wkt, buffer):
        """Main sql query """
        sql = 'SELECT lrc_wales_data.records.id, ' \
                   'lrc_wales_data.records.lrcs_id, ' \
                   'lrc_wales_data.records.lrc, ' \
                   'lrc_wales_data.records.tok, ' \
                   'lrc_wales_data.records.rtvk, ' \
                   'lrc_wales_data.records.rtlik, ' \
                   'lrc_wales_data.records.actual_name AS actual_name_original, ' \
                   'lrc_wales_data.records.date_start, ' \
                   'lrc_wales_data.records.date_end, ' \
                   'lrc_wales_data.records.date_type, ' \
                   'lrc_wales_data.records.date_entered, ' \
                   'lrc_wales_data.records.date_modified, ' \
                   'lrc_wales_data.records.grid_ref, ' \
                   'CASE WHEN lrc_wales_data.dmt.sensitive_resolution > 0' \
                   '    THEN ' \
                   '        /* Is the cofnod release res set HIGHER than the default release res. */' \
                   '        CASE WHEN lrc_wales_data.records.grid_ref_release_res > lrc_wales_data.dmt.sensitive_resolution' \
                   '        THEN ' \
                   '            /* Use the cofnod res. */' \
                   '            lrc_wales_data.reduce_grid_reference(lrc_wales_data.records.grid_ref, lrc_wales_data.records.grid_ref_release_res, FALSE)' \
                   '        ELSE ' \
                   '            /* Use the default DMT res. */' \
                   '            lrc_wales_data.reduce_grid_reference(lrc_wales_data.records.grid_ref, lrc_wales_data.dmt.sensitive_resolution, FALSE)' \
                   '        END ' \
                   '    ELSE ' \
                   '        /* Just return the normal grid ref as the public grid ref. */' \
                   '        lrc_wales_data.records.grid_ref' \
                   '    END ' \
                   'AS grid_ref_public, ' \
                   'lrc_wales_data.records.grid_ref_type, ' \
                   'lrc_wales_data.records.grid_ref_release_res, ' \
                   'lrc_wales_data.records.location, ' \
                   'lrc_wales_data.records.abundance, ' \
                   'lrc_wales_data.records.recorder, ' \
                   'lrc_wales_data.records.determiner, ' \
                   'lrc_wales_data.records.record_type, ' \
                   'lrc_wales_data.records.source, ' \
                   'lrc_wales_data.records.comments, ' \
                   'lrc_wales_data.records.verification_level, ' \
                   'lrc_wales_data.records.date_formatted, ' \
                   'lrc_wales_data.records.easting_centred, ' \
                   'lrc_wales_data.records.northing_centred, ' \
                   'lrc_wales_data.records.easting_min, ' \
                   'lrc_wales_data.records.northing_min, ' \
                   'lrc_wales_data.records.easting_max, ' \
                   'lrc_wales_data.records.northing_max, ' \
                   'lrc_wales_data.records.grid_ref_10m_sq, ' \
                   'lrc_wales_data.records.grid_ref_100m_sq, ' \
                   'lrc_wales_data.records.grid_ref_1km_sq, ' \
                   'lrc_wales_data.records.grid_ref_10km_sq, ' \
                   'lrc_wales_data.records.latitude, ' \
                   'lrc_wales_data.records.longitude, ' \
                   'lrc_wales_data.records.resolution, ' \
                   'lrc_wales_data.records.updated_at, ' \
                   'lrc_wales_data.records.created_at, ' \
                   '' \
                   'lrc_wales_data.lrcs.name AS name_lrc, ' \
                   'lrc_wales_data.lrcs.full AS full_name_lrc, ' \
                   '' \
                   'lrc_wales_data.taxon_dict.id AS id_taxon_dict, ' \
                   'lrc_wales_data.taxon_dict.actual_name, ' \
                   'lrc_wales_data.taxon_dict.common_name, ' \
                   'lrc_wales_data.taxon_dict.welsh_name, ' \
                   'lrc_wales_data.taxon_dict.taxon_family, ' \
                   'lrc_wales_data.taxon_dict.taxon_order, ' \
                   '' \
                   'lrc_wales_data.dmt.cat, ' \
                   'lrc_wales_data.dmt.mobile_buffer, ' \
                   'lrc_wales_data.dmt.full_status, ' \
                   'lrc_wales_data.dmt.sensitive_resolution, ' \
                   'lrc_wales_data.dmt.sensitive_features, ' \
                   'lrc_wales_data.dmt.cat3_json, ' \
                   '' \
                   'lrc_wales_data.taxon_nbn_groups.id AS id_taxon_nbn_group, ' \
                   'lrc_wales_data.taxon_nbn_groups.name AS name_taxon_nbn_group, ' \
                   'lrc_wales_data.taxon_super_groups.id AS id_taxon_super_group, ' \
                   'lrc_wales_data.taxon_super_groups.name AS name_taxon_super_group, ' \
                   'ST_AsGeoJSON(geom_point) AS geom_point, ' \
                   'ST_AsGeoJSON(geom_poly) AS geom_poly ' \
                   '' \
                   'FROM lrc_wales_data.records ' \
                   '' \
                   'LEFT JOIN lrc_wales_data.lrcs ON lrcs.id = records.lrcs_id ' \
                   'LEFT JOIN lrc_wales_data.taxon_dict ON taxon_dict.rtvk = records.rtvk ' \
                   'LEFT JOIN lrc_wales_data.taxon_nbn_groups ON taxon_nbn_groups.id = taxon_dict.taxon_nbn_groups_id ' \
                   'LEFT JOIN lrc_wales_data.taxon_super_groups ON taxon_super_groups.id = taxon_nbn_groups.taxon_super_groups_id ' \
                   'LEFT JOIN lrc_wales_data.dmt ON dmt.rtvk = taxon_dict.rtvk ' \
                   '' \
                   'WHERE date_type != \'U\' ' \
                   'AND lrc_wales_data.taxon_dict.id IS NOT NULL ' \
                   'AND st_DWithin(records.geom_poly,st_GeomFromText(\'' + wkt + '\',27700),' + buffer + ') '

        if category == 'BATS':
            #$this->search = $this->search->where('dmt.bat', true);
            sql = sql + 'AND dmt.bat = TRUE '
        elif category == 'CAT4':
            sql = sql + 'AND (dmt.cat = \'' + category + '\' OR dmt.cat IS NULL) '
        else:
            sql = sql + 'AND dmt.cat = \'' + category + '\' '

        sql = sql + 'AND resolution <= 2000 '
        sql = sql + 'ORDER BY actual_name ASC'

        self.sql = sql
        return self.sql





