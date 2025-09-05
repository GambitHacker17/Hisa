
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

ReportReason =Union [raw .types .InputReportReasonChildAbuse ,raw .types .InputReportReasonCopyright ,raw .types .InputReportReasonFake ,raw .types .InputReportReasonGeoIrrelevant ,raw .types .InputReportReasonIllegalDrugs ,raw .types .InputReportReasonOther ,raw .types .InputReportReasonPersonalDetails ,raw .types .InputReportReasonPornography ,raw .types .InputReportReasonSpam ,raw .types .InputReportReasonViolence ]

class ReportReason :
    """"""

    QUALNAME ="hisapyro.raw.base.ReportReason"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/report-reason")
