import datetime

class AderynSpreadsheet:
    """QGIS Plugin Implementation."""

    def __init__(self, SearchName, SearchLocation):
        """Constructor"""
        self.SearchName = SearchName
        self.SearchLocation = SearchLocation

    def linesInformation(self):
        """ Array of lines """
        dateString = datetime.date.today().strftime("%d/%m/%Y")

        lines = []
        lines.append(['text', 'B2', 'BIODIVERSITY INFORMATION SEARCH:', 'cell_format_bold_large'])
        lines.append(['text', 'B4', self.SearchName, 'cell_format_bold_large'])
        lines.append(['text', 'B5', self.SearchLocation.upper(), 'cell_format_bold_large'])
        lines.append(['text', 'B7', 'Prepared on behalf of XXXXXX on ' + dateString, 'cell_format_bold_medium'])
        lines.append(['text', 'B9', 'This report is confidential and should not be passed onto third parties without prior permission from BIS, unless they are named on the associated Data Enquiry and Release Form (DERF). '])
        lines.append(['text', 'B10', 'The data contained within the report is not to be copied, distributed, disseminated, published or broadcast in any format, including on the internet, to anyone unless named on the associated DERF.'])
        lines.append(['text', 'B11', 'For full terms and conditions and the names listed on the DERF, please see the appendix attached to the end of this report. '])
        lines.append(['text', 'B12', 'https://www.bis.org.uk/upload/library/NRW_Data_EFGR__resolution_release.pdf'])

        lines.append(['text', 'B15', 'For further ecological advice on records in this report please see contact notes at end of report or contact relevant County Recorder.'])
        lines.append(['text', 'B16', 'Details on BIS website     https://www.bis.org.uk/get_involved/find_an_expert'])

        lines.append(['text', 'B18', 'For detailed information on Designated Sites in Wales go to NRW website http://naturalresourceswales.gov.uk/'])

        return lines

    def linesTandC(self):
        """ Array of lines """
        dateString = datetime.date.today().strftime("%d/%m/%Y")

        lines = []
        lines.append(['text', 'A1', 'APPENDIX - Terms and Conditions of Data Supply', 'cell_format_bold'])
        lines.append(['text', 'A3', 'These are the terms and conditions that our client originally signed up to.  If you are in possession of this report and were not named on the DERF, you are not permitted to use any part of the report or its contents for any reason.'])
        lines.append(['text', 'A5', 'SENSITIVE AND CONFIDENTIAL INFORMATION:', 'cell_format_bold'])

        lines.append(['text', 'A6', '§  I understand that data marked as sensitive or confidential is provided outside the Environmental Information Regulations 2004 (EIR) and the Freedom of Information Act (FoIA) 2000 (to prevent its becoming by default “public information”). It is issued to only those named above.'])
        lines.append(['text', 'A7', '§  I understand that, when held by a public body (as defined separately by the FoIA and EIR), the data will still be subject to FoIA and EIR, but proper regard must be given to its level of sensitivity in assessing whether to release the data in response to a request under the above legislation in a public interest test.'])
        lines.append(['text', 'A8', '§  I understand that all data (including that marked sensitive or confidential) may not be passed on to other bodies or individuals (including clients, agents and colleagues) unless they are named above and have received a copy of this form. Furthermore I may not copy, distribute, disseminate, publish or broadcast the data in any format, including on the Internet, without written consent from BIS. I agree that where other parties require the information, I will direct them to BIS.'])
        lines.append(['text', 'A9', '§  I agree to keep the data secure from unauthorised or accidental use, access, disclosure or loss, and to take reasonable practical steps to ensure the security of the data. '])
        lines.append(['text', 'A10', '§  I agree to delete or destroy the data after 12 months or after use.'])

        lines.append(['text', 'A12', 'GENERAL TERMS::', 'cell_format_bold'])
        lines.append(['text', 'A13', '§  I understand that BIS operate as a not-for-profit company for the provision of objective biodiversity information. Charges made are purely administrative to reflect the cost of collating, managing and disseminating biodiversity information.'])
        lines.append(['text', 'A14', '§  I confirm that all data requested will be used for legitimate and legal purposes.'])
        lines.append(['text', 'A15', '§  I confirm that to the best of my knowledge I, nor any of my colleagues who may have access to data obtained from BIS, have been investigated for nor convicted of any form of wildlife crime.'])
        lines.append(['text', 'A16', '§  I confirm that to the best of my knowledge neither I nor any of my colleagues have been responsible for any misuse of data obtained from other local records centres.'])
        lines.append(['text', 'A17', '§  I understand that the copyright of raw biological records remains with the original recorder and that copyright of processed data and reports belongs to BIS.'])
        lines.append(['text', 'A18', '§  I acknowledge that I cannot pass records onto third parties (except clients, agents and colleagues) without the written permission of BIS and the original recorders of the data.'])
        lines.append(['text', 'A19',  '§  I acknowledge that I cannot use information for any purpose other than that for which it was requested.'])
        lines.append(['text', 'A20', '§  Data supplied by BIS must not be entered into a computerised database or geographic information system without written permission from BIS, unless supplied in that format.'])
        lines.append(['text', 'A21', '§  BIS will be acknowledged in any publications or reports, which are produced, using data it supplied. BIS would welcome a copy of any such publication or report supplied to BIS free of charge.'])
        lines.append(['text', 'A22', '§  Permission to use data supplied by BIS expires 12 months after receipt. I shall contact BIS within one month of expiry if the data is still required.'])
        lines.append(['text', 'A23', '§  Data is provided ‘as held’ by BIS and was deemed to be accurate at the time of collection. BIS cannot guarantee the accuracy of data supplied, although all data is validated as far as possible.'])
        lines.append(['text', 'A24', '§  I will not hold BIS or its data suppliers liable for problems/financial loss, which might arise from inaccuracy of any data supplied by BIS.'])
        lines.append(['text', 'A25', '§  Past records of presence of a habitat or species do not guarantee continued occurrence. Absence of records does not imply absence of a species, merely that no records are held at BIS.'])
        lines.append(['text', 'A26', '§  Use of BIS data search services does not in any way replace the need for adequate field survey'])

        # lines.append(['A28', 'Names of clients, agents and colleagues who will access data provided by BIS (as listed on the DERF):', 'cell_format_bold_border'])
        # lines.append(['B28', '', 'cell_format_bold', 'cell_format_bold_border'])
        # lines.append(['C28', '', 'cell_format_bold', 'cell_format_bold_border'])
        lines.append(['merge', 'A28:C28', 'Names of clients, agents and colleagues who will access data provided by BIS (as listed on the DERF):', 'cell_format_bold_border'])
        lines.append(['text', 'A29', 'Name (of individual or department)', 'cell_format_bold_border'])
        lines.append(['text', 'B29', 'Organisation', 'cell_format_bold_border'])
        lines.append(['text', 'C29', 'Position', 'cell_format_bold_border'])
        lines.append(['text', 'A30', '', 'cell_format_bold_border'])
        lines.append(['text', 'B30', '', 'cell_format_bold_border'])
        lines.append(['text', 'C30', '', 'cell_format_bold_border'])
        lines.append(['text', 'A31', '', 'cell_format_bold_border'])
        lines.append(['text', 'B31', '', 'cell_format_bold_border'])
        lines.append(['text', 'C31', '', 'cell_format_bold_border'])
        lines.append(['text', 'A32', '', 'cell_format_bold_border'])
        lines.append(['text', 'B32', '', 'cell_format_bold_border'])
        lines.append(['text', 'C32', '', 'cell_format_bold_border'])
        lines.append(['text', 'A33', '', 'cell_format_bold_border'])
        lines.append(['text', 'B33', '', 'cell_format_bold_border'])
        lines.append(['text', 'C33', '', 'cell_format_bold_border'])
        lines.append(['text', 'A34', '', 'cell_format_bold_border'])
        lines.append(['text', 'B34', '', 'cell_format_bold_border'])
        lines.append(['text', 'C34', '', 'cell_format_bold_border'])
        lines.append(['text', 'A35', '', 'cell_format_bold_border'])
        lines.append(['text', 'B35', '', 'cell_format_bold_border'])
        lines.append(['text', 'C35', '', 'cell_format_bold_border'])
        lines.append(['text', 'A36', '', 'cell_format_bold_border'])
        lines.append(['text', 'B36', '', 'cell_format_bold_border'])
        lines.append(['text', 'C36', '', 'cell_format_bold_border'])
        lines.append(['text', 'A37', '', 'cell_format_bold_border'])
        lines.append(['text', 'B37', '', 'cell_format_bold_border'])
        lines.append(['text', 'C37', '', 'cell_format_bold_border'])
        lines.append(['text', 'A38', '', 'cell_format_bold_border'])
        lines.append(['text', 'B38', '', 'cell_format_bold_border'])
        lines.append(['text', 'C38', '', 'cell_format_bold_border'])
        lines.append(['text', 'A39', '', 'cell_format_bold_border'])
        lines.append(['text', 'B39', '', 'cell_format_bold_border'])
        lines.append(['text', 'C39', '', 'cell_format_bold_border'])
        return lines
