import os
import re
import json

import settings
from helpers import regular_request


class MOEXBase:
    url = ''

    def __init__(self, url=''):
        self.url = url

    def __repr__(self):
        return f'{self.__class__}'

    @staticmethod
    def _join(*args):
        return os.path.join(*args)

    @staticmethod
    def _for_normal_dict(data_dict: dict) -> dict:
        normal_dict = {}

        for key, val in data_dict.items():
            if key == 'metadata':
                continue
            low_vals = [low.lower() for low in val['columns']]
            normal_dict[key] = []
            for data in val['data']:
                row = dict(zip(low_vals, data))
                normal_dict[key].append(row)
        return normal_dict

    @staticmethod
    def _with_metadata(
            data,
            code,
            message=''):
        return {
            'data': data,
            'metadata': {
                'code': code,
                'message': message
            }
        }

    def _make_request(self, url, normal_dict=True):
        result = regular_request(url)
        if result.status_code == 200:
            data = json.loads(result.text)
            data = self._for_normal_dict(data) if normal_dict else data
        else:
            data = {}
        return self._with_metadata(
            data,
            result.status_code,
            result.reason
        )

    def securities(
            self,
            sid: int = None,
            return_type: str = settings.RETURN_TYPE,
            date: str = None
    ):
        url = os.path.join(self.url, f'securities.{return_type}')
        if sid and date:
            raise ValueError('need just one value (sid or date)')
        if sid:
            url = os.path.join(self.url, 'securities', f'{sid}.{return_type}')
        if date:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                raise ValueError('The right format is: YYYY-MM-DD')
            url += f'?date={date}'
        return self._make_request(url)


class BoardMulti(MOEXBase):
    ...


class Boards(MOEXBase):

    def __init__(self, url):
        super().__init__(url)
        self.tqif = BoardMulti(self._join(self.url, 'tqif'))
        self.tqtf = BoardMulti(self._join(self.url, 'tqtf'))
        self.tqbr = BoardMulti(self._join(self.url, 'tqbr'))
        self.tqbs = BoardMulti(self._join(self.url, 'tqbs'))
        self.tqnl = BoardMulti(self._join(self.url, 'tqnl'))
        self.tqlv = BoardMulti(self._join(self.url, 'tqlv'))
        self.tqli = BoardMulti(self._join(self.url, 'tqli'))
        self.tqne = BoardMulti(self._join(self.url, 'tqne'))
        self.tqde = BoardMulti(self._join(self.url, 'tqde'))
        self.tqpi = BoardMulti(self._join(self.url, 'tqpi'))
        self.tqtd = BoardMulti(self._join(self.url, 'tqtd'))
        self.tqfd = BoardMulti(self._join(self.url, 'tqfd'))
        self.tqpd = BoardMulti(self._join(self.url, 'tqpd'))
        self.eqbr = BoardMulti(self._join(self.url, 'eqbr'))
        self.eqbs = BoardMulti(self._join(self.url, 'eqbs'))
        self.eqnl = BoardMulti(self._join(self.url, 'eqnl'))
        self.eqlv = BoardMulti(self._join(self.url, 'eqlv'))
        self.eqde = BoardMulti(self._join(self.url, 'eqde'))
        self.eqli = BoardMulti(self._join(self.url, 'eqli'))
        self.eqne = BoardMulti(self._join(self.url, 'eqne'))
        self.speq = BoardMulti(self._join(self.url, 'speq'))
        self.smal = BoardMulti(self._join(self.url, 'smal'))
        self.tqdp = BoardMulti(self._join(self.url, 'tqdp'))
        self.eqdp = BoardMulti(self._join(self.url, 'eqdp'))
        self.eqtd = BoardMulti(self._join(self.url, 'eqtd'))
        self.tqbe = BoardMulti(self._join(self.url, 'tqbe'))
        self.tqte = BoardMulti(self._join(self.url, 'tqte'))
        self.tqfe = BoardMulti(self._join(self.url, 'tqfe'))
        self.tqpe = BoardMulti(self._join(self.url, 'tqpe'))
        self.tqty = BoardMulti(self._join(self.url, 'tqty'))
        self.tqpy = BoardMulti(self._join(self.url, 'tqpy'))
        self.eqtu = BoardMulti(self._join(self.url, 'eqtu'))
        self.tqth = BoardMulti(self._join(self.url, 'tqth'))
        self.tqph = BoardMulti(self._join(self.url, 'tqph'))
        self.eqcc = BoardMulti(self._join(self.url, 'eqcc'))
        self.tqob = BoardMulti(self._join(self.url, 'tqob'))
        self.tqos = BoardMulti(self._join(self.url, 'tqos'))
        self.tqno = BoardMulti(self._join(self.url, 'tqno'))
        self.tqov = BoardMulti(self._join(self.url, 'tqov'))
        self.tqnb = BoardMulti(self._join(self.url, 'tqnb'))
        self.tqus = BoardMulti(self._join(self.url, 'tqus'))
        self.tqcb = BoardMulti(self._join(self.url, 'tqcb'))
        self.tqrd = BoardMulti(self._join(self.url, 'tqrd'))
        self.tqir = BoardMulti(self._join(self.url, 'tqir'))
        self.tqod = BoardMulti(self._join(self.url, 'tqod'))
        self.tqud = BoardMulti(self._join(self.url, 'tqud'))
        self.tqiu = BoardMulti(self._join(self.url, 'tqiu'))
        self.tqtc = BoardMulti(self._join(self.url, 'tqtc'))
        self.eqob = BoardMulti(self._join(self.url, 'eqob'))
        self.eqos = BoardMulti(self._join(self.url, 'eqos'))
        self.eqno = BoardMulti(self._join(self.url, 'eqno'))
        self.eqov = BoardMulti(self._join(self.url, 'eqov'))
        self.eqdb = BoardMulti(self._join(self.url, 'eqdb'))
        self.eqnb = BoardMulti(self._join(self.url, 'eqnb'))
        self.equs = BoardMulti(self._join(self.url, 'equs'))
        self.eqeo = BoardMulti(self._join(self.url, 'eqeo'))
        self.spob = BoardMulti(self._join(self.url, 'spob'))
        self.eqtc = BoardMulti(self._join(self.url, 'eqtc'))
        self.eqeu = BoardMulti(self._join(self.url, 'eqeu'))
        self.eqgo = BoardMulti(self._join(self.url, 'eqgo'))
        self.eqyo = BoardMulti(self._join(self.url, 'eqyo'))
        self.aubb = BoardMulti(self._join(self.url, 'aubb'))
        self.auct = BoardMulti(self._join(self.url, 'auct'))
        self.tqdb = BoardMulti(self._join(self.url, 'tqdb'))
        self.tqoe = BoardMulti(self._join(self.url, 'tqoe'))
        self.tqed = BoardMulti(self._join(self.url, 'tqed'))
        self.tqie = BoardMulti(self._join(self.url, 'tqie'))
        self.tqdu = BoardMulti(self._join(self.url, 'tqdu'))
        self.tqoy = BoardMulti(self._join(self.url, 'tqoy'))
        self.tqiy = BoardMulti(self._join(self.url, 'tqiy'))
        self.pact = BoardMulti(self._join(self.url, 'pact'))
        self.rpmo = BoardMulti(self._join(self.url, 'rpmo'))
        self.rpeq = BoardMulti(self._join(self.url, 'rpeq'))
        self.rpma = BoardMulti(self._join(self.url, 'rpma'))
        self.rpeu = BoardMulti(self._join(self.url, 'rpeu'))
        self.rpua = BoardMulti(self._join(self.url, 'rpua'))
        self.rpuo = BoardMulti(self._join(self.url, 'rpuo'))
        self.rpeo = BoardMulti(self._join(self.url, 'rpeo'))
        self.rpey = BoardMulti(self._join(self.url, 'rpey'))
        self.rpgo = BoardMulti(self._join(self.url, 'rpgo'))
        self.rpcc = BoardMulti(self._join(self.url, 'rpcc'))
        self.pteu = BoardMulti(self._join(self.url, 'pteu'))
        self.ptif = BoardMulti(self._join(self.url, 'ptif'))
        self.pttc = BoardMulti(self._join(self.url, 'pttc'))
        self.pttf = BoardMulti(self._join(self.url, 'pttf'))
        self.pteq = BoardMulti(self._join(self.url, 'pteq'))
        self.ptes = BoardMulti(self._join(self.url, 'ptes'))
        self.ptnl = BoardMulti(self._join(self.url, 'ptnl'))
        self.ptlv = BoardMulti(self._join(self.url, 'ptlv'))
        self.ptli = BoardMulti(self._join(self.url, 'ptli'))
        self.ptne = BoardMulti(self._join(self.url, 'ptne'))
        self.ptno = BoardMulti(self._join(self.url, 'ptno'))
        self.ptus = BoardMulti(self._join(self.url, 'ptus'))
        self.ptde = BoardMulti(self._join(self.url, 'ptde'))
        self.ptpi = BoardMulti(self._join(self.url, 'ptpi'))
        self.pstd = BoardMulti(self._join(self.url, 'pstd'))
        self.psfd = BoardMulti(self._join(self.url, 'psfd'))
        self.pspd = BoardMulti(self._join(self.url, 'pspd'))
        self.psif = BoardMulti(self._join(self.url, 'psif'))
        self.pstc = BoardMulti(self._join(self.url, 'pstc'))
        self.pstf = BoardMulti(self._join(self.url, 'pstf'))
        self.pseq = BoardMulti(self._join(self.url, 'pseq'))
        self.pses = BoardMulti(self._join(self.url, 'pses'))
        self.psnl = BoardMulti(self._join(self.url, 'psnl'))
        self.pslv = BoardMulti(self._join(self.url, 'pslv'))
        self.psde = BoardMulti(self._join(self.url, 'psde'))
        self.psli = BoardMulti(self._join(self.url, 'psli'))
        self.psne = BoardMulti(self._join(self.url, 'psne'))
        self.psos = BoardMulti(self._join(self.url, 'psos'))
        self.psno = BoardMulti(self._join(self.url, 'psno'))
        self.psov = BoardMulti(self._join(self.url, 'psov'))
        self.psnb = BoardMulti(self._join(self.url, 'psnb'))
        self.psus = BoardMulti(self._join(self.url, 'psus'))
        self.pspi = BoardMulti(self._join(self.url, 'pspi'))
        self.psgo = BoardMulti(self._join(self.url, 'psgo'))
        self.psau = BoardMulti(self._join(self.url, 'psau'))
        self.paus = BoardMulti(self._join(self.url, 'paus'))
        self.paeu = BoardMulti(self._join(self.url, 'paeu'))
        self.pacy = BoardMulti(self._join(self.url, 'pacy'))
        self.pagb = BoardMulti(self._join(self.url, 'pagb'))
        self.psbb = BoardMulti(self._join(self.url, 'psbb'))
        self.psbe = BoardMulti(self._join(self.url, 'psbe'))
        self.otcb = BoardMulti(self._join(self.url, 'otcb'))
        self.otcu = BoardMulti(self._join(self.url, 'otcu'))
        self.otce = BoardMulti(self._join(self.url, 'otce'))
        self.pttd = BoardMulti(self._join(self.url, 'pttd'))
        self.ptfd = BoardMulti(self._join(self.url, 'ptfd'))
        self.ptpd = BoardMulti(self._join(self.url, 'ptpd'))
        self.psbu = BoardMulti(self._join(self.url, 'psbu'))
        self.ptoe = BoardMulti(self._join(self.url, 'ptoe'))
        self.pted = BoardMulti(self._join(self.url, 'pted'))
        self.ptie = BoardMulti(self._join(self.url, 'ptie'))
        self.psse = BoardMulti(self._join(self.url, 'psse'))
        self.pste = BoardMulti(self._join(self.url, 'pste'))
        self.psfe = BoardMulti(self._join(self.url, 'psfe'))
        self.pspe = BoardMulti(self._join(self.url, 'pspe'))
        self.ptse = BoardMulti(self._join(self.url, 'ptse'))
        self.ptte = BoardMulti(self._join(self.url, 'ptte'))
        self.ptfe = BoardMulti(self._join(self.url, 'ptfe'))
        self.ptpe = BoardMulti(self._join(self.url, 'ptpe'))
        self.ptob = BoardMulti(self._join(self.url, 'ptob'))
        self.ptos = BoardMulti(self._join(self.url, 'ptos'))
        self.ptov = BoardMulti(self._join(self.url, 'ptov'))
        self.ptnb = BoardMulti(self._join(self.url, 'ptnb'))
        self.ptdb = BoardMulti(self._join(self.url, 'ptdb'))
        self.ptir = BoardMulti(self._join(self.url, 'ptir'))
        self.ptod = BoardMulti(self._join(self.url, 'ptod'))
        self.ptud = BoardMulti(self._join(self.url, 'ptud'))
        self.ptiu = BoardMulti(self._join(self.url, 'ptiu'))
        self.psob = BoardMulti(self._join(self.url, 'psob'))
        self.psdb = BoardMulti(self._join(self.url, 'psdb'))
        self.psir = BoardMulti(self._join(self.url, 'psir'))
        self.pseu = BoardMulti(self._join(self.url, 'pseu'))
        self.psud = BoardMulti(self._join(self.url, 'psud'))
        self.psiu = BoardMulti(self._join(self.url, 'psiu'))
        self.pseo = BoardMulti(self._join(self.url, 'pseo'))
        self.psed = BoardMulti(self._join(self.url, 'psed'))
        self.psie = BoardMulti(self._join(self.url, 'psie'))
        self.psyo = BoardMulti(self._join(self.url, 'psyo'))
        self.psiy = BoardMulti(self._join(self.url, 'psiy'))
        self.ptiy = BoardMulti(self._join(self.url, 'ptiy'))
        self.ptoy = BoardMulti(self._join(self.url, 'ptoy'))
        self.psty = BoardMulti(self._join(self.url, 'psty'))
        self.pspy = BoardMulti(self._join(self.url, 'pspy'))
        self.ptty = BoardMulti(self._join(self.url, 'ptty'))
        self.ptpy = BoardMulti(self._join(self.url, 'ptpy'))
        self.psth = BoardMulti(self._join(self.url, 'psth'))
        self.psph = BoardMulti(self._join(self.url, 'psph'))
        self.ptth = BoardMulti(self._join(self.url, 'ptth'))
        self.ptph = BoardMulti(self._join(self.url, 'ptph'))
        self.pscc = BoardMulti(self._join(self.url, 'pscc'))
        self.sndx = BoardMulti(self._join(self.url, 'sndx'))
        self.rtsi = BoardMulti(self._join(self.url, 'rtsi'))
        self.inav = BoardMulti(self._join(self.url, 'inav'))
        self.mmix = BoardMulti(self._join(self.url, 'mmix'))
        self.agro = BoardMulti(self._join(self.url, 'agro'))
        self.inpf = BoardMulti(self._join(self.url, 'inpf'))
        self.sdii = BoardMulti(self._join(self.url, 'sdii'))
        self.stmr = BoardMulti(self._join(self.url, 'stmr'))
        self.sdmr = BoardMulti(self._join(self.url, 'sdmr'))
        self.stad = BoardMulti(self._join(self.url, 'stad'))
        self.sdad = BoardMulti(self._join(self.url, 'sdad'))
        self.strp = BoardMulti(self._join(self.url, 'strp'))
        self.sdrp = BoardMulti(self._join(self.url, 'sdrp'))
        self.clmr = BoardMulti(self._join(self.url, 'clmr'))
        self.clad = BoardMulti(self._join(self.url, 'clad'))
        self.eqrd = BoardMulti(self._join(self.url, 'eqrd'))
        self.eqre = BoardMulti(self._join(self.url, 'eqre'))
        self.eqwp = BoardMulti(self._join(self.url, 'eqwp'))
        self.eqwd = BoardMulti(self._join(self.url, 'eqwd'))
        self.eqwe = BoardMulti(self._join(self.url, 'eqwe'))
        self.eqrp = BoardMulti(self._join(self.url, 'eqrp'))
        self.eqmp = BoardMulti(self._join(self.url, 'eqmp'))
        self.eqmd = BoardMulti(self._join(self.url, 'eqmd'))
        self.eqme = BoardMulti(self._join(self.url, 'eqme'))
        self.eqtp = BoardMulti(self._join(self.url, 'eqtp'))
        self.etqd = BoardMulti(self._join(self.url, 'etqd'))
        self.eqte = BoardMulti(self._join(self.url, 'eqte'))
        self.liqr = BoardMulti(self._join(self.url, 'liqr'))
        self.eqry = BoardMulti(self._join(self.url, 'eqry'))
        self.psry = BoardMulti(self._join(self.url, 'psry'))
        self.eqwy = BoardMulti(self._join(self.url, 'eqwy'))
        self.eqmy = BoardMulti(self._join(self.url, 'eqmy'))
        self.eqty = BoardMulti(self._join(self.url, 'eqty'))
        self.psrp = BoardMulti(self._join(self.url, 'psrp'))
        self.psrd = BoardMulti(self._join(self.url, 'psrd'))
        self.psre = BoardMulti(self._join(self.url, 'psre'))
        self.fkrp = BoardMulti(self._join(self.url, 'fkrp'))
        self.fkow = BoardMulti(self._join(self.url, 'fkow'))
        self.fksw = BoardMulti(self._join(self.url, 'fksw'))
        self.fkfw = BoardMulti(self._join(self.url, 'fkfw'))
        self.fkom = BoardMulti(self._join(self.url, 'fkom'))
        self.fksm = BoardMulti(self._join(self.url, 'fksm'))
        self.fktm = BoardMulti(self._join(self.url, 'fktm'))
        self.fkum = BoardMulti(self._join(self.url, 'fkum'))
        self.fkoy = BoardMulti(self._join(self.url, 'fkoy'))
        self.frrp = BoardMulti(self._join(self.url, 'frrp'))
        self.frow = BoardMulti(self._join(self.url, 'frow'))
        self.frsw = BoardMulti(self._join(self.url, 'frsw'))
        self.frfw = BoardMulti(self._join(self.url, 'frfw'))
        self.from_ = BoardMulti(self._join(self.url, 'from'))
        self.frtm = BoardMulti(self._join(self.url, 'frtm'))
        self.tqqi = BoardMulti(self._join(self.url, 'tqqi'))
        self.eqqi = BoardMulti(self._join(self.url, 'eqqi'))
        self.psqi = BoardMulti(self._join(self.url, 'psqi'))
        self.ptqi = BoardMulti(self._join(self.url, 'ptqi'))
        self.rpqi = BoardMulti(self._join(self.url, 'rpqi'))
        self.rpuq = BoardMulti(self._join(self.url, 'rpuq'))
        self.tqqd = BoardMulti(self._join(self.url, 'tqqd'))
        self.sotc = BoardMulti(self._join(self.url, 'sotc'))
        self.mxbd = BoardMulti(self._join(self.url, 'mxbd'))
        self.tdep = BoardMulti(self._join(self.url, 'tdep'))
        self.ndep = BoardMulti(self._join(self.url, 'ndep'))
        self.ndpu = BoardMulti(self._join(self.url, 'ndpu'))
        self.ndpe = BoardMulti(self._join(self.url, 'ndpe'))
        self.tdpu = BoardMulti(self._join(self.url, 'tdpu'))
        self.tdpe = BoardMulti(self._join(self.url, 'tdpe'))
        self.tdpy = BoardMulti(self._join(self.url, 'tdpy'))
        self.ndpy = BoardMulti(self._join(self.url, 'ndpy'))
        self.adep = BoardMulti(self._join(self.url, 'adep'))
        self.liqb = BoardMulti(self._join(self.url, 'liqb'))
        self.ciqb = BoardMulti(self._join(self.url, 'ciqb'))
        self.gcrp = BoardMulti(self._join(self.url, 'gcrp'))
        self.gcow = BoardMulti(self._join(self.url, 'gcow'))
        self.gcsw = BoardMulti(self._join(self.url, 'gcsw'))
        self.gcom = BoardMulti(self._join(self.url, 'gcom'))
        self.gcsm = BoardMulti(self._join(self.url, 'gcsm'))
        self.gctm = BoardMulti(self._join(self.url, 'gctm'))
        self.gcum = BoardMulti(self._join(self.url, 'gcum'))
        self.gcoy = BoardMulti(self._join(self.url, 'gcoy'))
        self.psgc = BoardMulti(self._join(self.url, 'psgc'))
        self.gurp = BoardMulti(self._join(self.url, 'gurp'))
        self.guow = BoardMulti(self._join(self.url, 'guow'))
        self.gusw = BoardMulti(self._join(self.url, 'gusw'))
        self.guom = BoardMulti(self._join(self.url, 'guom'))
        self.gusm = BoardMulti(self._join(self.url, 'gusm'))
        self.gutm = BoardMulti(self._join(self.url, 'gutm'))
        self.guum = BoardMulti(self._join(self.url, 'guum'))
        self.guoy = BoardMulti(self._join(self.url, 'guoy'))
        self.pugc = BoardMulti(self._join(self.url, 'pugc'))
        self.gerp = BoardMulti(self._join(self.url, 'gerp'))
        self.geow = BoardMulti(self._join(self.url, 'geow'))
        self.gesw = BoardMulti(self._join(self.url, 'gesw'))
        self.geom = BoardMulti(self._join(self.url, 'geom'))
        self.gesm = BoardMulti(self._join(self.url, 'gesm'))
        self.getm = BoardMulti(self._join(self.url, 'getm'))
        self.geum = BoardMulti(self._join(self.url, 'geum'))
        self.geoy = BoardMulti(self._join(self.url, 'geoy'))
        self.pegc = BoardMulti(self._join(self.url, 'pegc'))
        self.gcnm = BoardMulti(self._join(self.url, 'gcnm'))
        self.gunm = BoardMulti(self._join(self.url, 'gunm'))
        self.genm = BoardMulti(self._join(self.url, 'genm'))
        self.gyrp = BoardMulti(self._join(self.url, 'gyrp'))
        self.gyow = BoardMulti(self._join(self.url, 'gyow'))
        self.gysw = BoardMulti(self._join(self.url, 'gysw'))
        self.gyom = BoardMulti(self._join(self.url, 'gyom'))
        self.gysm = BoardMulti(self._join(self.url, 'gysm'))
        self.gytm = BoardMulti(self._join(self.url, 'gytm'))
        self.gyum = BoardMulti(self._join(self.url, 'gyum'))
        self.gynm = BoardMulti(self._join(self.url, 'gynm'))
        self.gyoy = BoardMulti(self._join(self.url, 'gyoy'))
        self.pygc = BoardMulti(self._join(self.url, 'pygc'))
        self.fcow = BoardMulti(self._join(self.url, 'fcow'))
        self.fcsw = BoardMulti(self._join(self.url, 'fcsw'))
        self.fcom = BoardMulti(self._join(self.url, 'fcom'))
        self.fcsm = BoardMulti(self._join(self.url, 'fcsm'))
        self.fctm = BoardMulti(self._join(self.url, 'fctm'))
        self.fcum = BoardMulti(self._join(self.url, 'fcum'))
        self.fcnm = BoardMulti(self._join(self.url, 'fcnm'))
        self.fcoy = BoardMulti(self._join(self.url, 'fcoy'))
        self.fyow = BoardMulti(self._join(self.url, 'fyow'))
        self.fysw = BoardMulti(self._join(self.url, 'fysw'))
        self.fyom = BoardMulti(self._join(self.url, 'fyom'))
        self.fysm = BoardMulti(self._join(self.url, 'fysm'))
        self.fytm = BoardMulti(self._join(self.url, 'fytm'))
        self.fyum = BoardMulti(self._join(self.url, 'fyum'))
        self.fynm = BoardMulti(self._join(self.url, 'fynm'))
        self.fyoy = BoardMulti(self._join(self.url, 'fyoy'))
        self.fqbh = BoardMulti(self._join(self.url, 'fqbh'))
        self.fqdh = BoardMulti(self._join(self.url, 'fqdh'))
        self.fqbr = BoardMulti(self._join(self.url, 'fqbr'))
        self.fqde = BoardMulti(self._join(self.url, 'fqde'))
        self.tqbd = BoardMulti(self._join(self.url, 'tqbd'))
        self.tqdd = BoardMulti(self._join(self.url, 'tqdd'))
        self.fqby = BoardMulti(self._join(self.url, 'fqby'))
        self.fqdy = BoardMulti(self._join(self.url, 'fqdy'))
        self.ftsh = BoardMulti(self._join(self.url, 'ftsh'))
        self.ftdh = BoardMulti(self._join(self.url, 'ftdh'))
        self.fssh = BoardMulti(self._join(self.url, 'fssh'))
        self.fsdh = BoardMulti(self._join(self.url, 'fsdh'))
        self.fteq = BoardMulti(self._join(self.url, 'fteq'))
        self.ftde = BoardMulti(self._join(self.url, 'ftde'))
        self.pssd = BoardMulti(self._join(self.url, 'pssd'))
        self.psdd = BoardMulti(self._join(self.url, 'psdd'))
        self.ftsy = BoardMulti(self._join(self.url, 'ftsy'))
        self.ftdy = BoardMulti(self._join(self.url, 'ftdy'))
        self.fssy = BoardMulti(self._join(self.url, 'fssy'))
        self.fsdy = BoardMulti(self._join(self.url, 'fsdy'))
        self.fseq = BoardMulti(self._join(self.url, 'fseq'))
        self.fsde = BoardMulti(self._join(self.url, 'fsde'))
        self.ptsd = BoardMulti(self._join(self.url, 'ptsd'))
        self.ptdd = BoardMulti(self._join(self.url, 'ptdd'))
        self.crer = BoardMulti(self._join(self.url, 'crer'))
        self.creu = BoardMulti(self._join(self.url, 'creu'))
        self.cree = BoardMulti(self._join(self.url, 'cree'))
        self.crey = BoardMulti(self._join(self.url, 'crey'))
        self.cteq = BoardMulti(self._join(self.url, 'cteq'))
        self.ctsd = BoardMulti(self._join(self.url, 'ctsd'))
        self.ctse = BoardMulti(self._join(self.url, 'ctse'))
        self.ctob = BoardMulti(self._join(self.url, 'ctob'))
        self.ctoy = BoardMulti(self._join(self.url, 'ctoy'))
        self.ctod = BoardMulti(self._join(self.url, 'ctod'))
        self.ctoe = BoardMulti(self._join(self.url, 'ctoe'))
        self.cpmo = BoardMulti(self._join(self.url, 'cpmo'))
        self.cpeu = BoardMulti(self._join(self.url, 'cpeu'))
        self.cpeo = BoardMulti(self._join(self.url, 'cpeo'))
        self.cpey = BoardMulti(self._join(self.url, 'cpey'))
        self.ciqr = BoardMulti(self._join(self.url, 'ciqr'))
        self.main = BoardMulti(self._join(self.url, 'main'))
        self.rpdd = BoardMulti(self._join(self.url, 'rpdd'))
        self.negd = BoardMulti(self._join(self.url, 'negd'))
        self.gndx = BoardMulti(self._join(self.url, 'gndx'))
        self.cets = BoardMulti(self._join(self.url, 'cets'))
        self.sdbp = BoardMulti(self._join(self.url, 'sdbp'))
        self.curr = BoardMulti(self._join(self.url, 'curr'))
        self.cngd = BoardMulti(self._join(self.url, 'cngd'))
        self.licu = BoardMulti(self._join(self.url, 'licu'))
        self.fixs = BoardMulti(self._join(self.url, 'fixs'))
        self.fixn = BoardMulti(self._join(self.url, 'fixn'))
        self.waps = BoardMulti(self._join(self.url, 'waps'))
        self.wapn = BoardMulti(self._join(self.url, 'wapn'))
        self.aucb = BoardMulti(self._join(self.url, 'aucb'))
        self.spec = BoardMulti(self._join(self.url, 'spec'))
        self.futs = BoardMulti(self._join(self.url, 'futs'))
        self.futn = BoardMulti(self._join(self.url, 'futn'))
        self.fixi = BoardMulti(self._join(self.url, 'fixi'))
        self.otct = BoardMulti(self._join(self.url, 'otct'))
        self.otcf = BoardMulti(self._join(self.url, 'otcf'))
        self.fob = BoardMulti(self._join(self.url, 'fob'))
        self.rfud = BoardMulti(self._join(self.url, 'rfud'))
        self.ropd = BoardMulti(self._join(self.url, 'ropd'))
        self.fiqs = BoardMulti(self._join(self.url, 'fiqs'))
        self.oiqs = BoardMulti(self._join(self.url, 'oiqs'))
        self.focm = BoardMulti(self._join(self.url, 'focm'))
        self.gsel = BoardMulti(self._join(self.url, 'gsel'))
        self.obbo = BoardMulti(self._join(self.url, 'obbo'))
        self.sugr = BoardMulti(self._join(self.url, 'sugr'))
        self.aigr = BoardMulti(self._join(self.url, 'aigr'))
        self.abgr = BoardMulti(self._join(self.url, 'abgr'))
        self.octr = BoardMulti(self._join(self.url, 'octr'))
        self.octu = BoardMulti(self._join(self.url, 'octu'))
        self.ocbr = BoardMulti(self._join(self.url, 'ocbr'))
        self.ocby = BoardMulti(self._join(self.url, 'ocby'))
        self.ocbu = BoardMulti(self._join(self.url, 'ocbu'))


class MarketMulti(MOEXBase):

    def __init__(self, url):
        super().__init__(url)
        self.boards = Boards(self._join(self.url, 'boards'))


class Markets(MOEXBase):

    def __init__(self, url):
        super().__init__(url)
        self.shares = MarketMulti(self._join(self.url, 'shares'))
        self.bonds = MarketMulti(self._join(self.url, 'bonds'))
        self.index = MarketMulti(self._join(self.url, 'index'))


class EngineMulti(MOEXBase):

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self._join(self.url, 'markets'))


class Engines(MOEXBase):

    def __init__(self, url):
        super().__init__(url)
        self.stock = EngineMulti(self._join(self.url, 'stock'))
        self.currency = EngineMulti(self._join(self.url, 'currency'))
        self.futures = EngineMulti(self._join(self.url, 'futures'))
        self.state = EngineMulti(self._join(self.url, 'state'))
        self.offboard = EngineMulti(self._join(self.url, 'offboard'))
        self.otc = EngineMulti(self._join(self.url, 'otc'))
        self.commodity = EngineMulti(self._join(self.url, 'commodity'))
        self.interventions = EngineMulti(self._join(self.url, 'interventions'))
        self.agro = EngineMulti(self._join(self.url, 'agro'))


class History(MOEXBase):

    def __init__(self, url):
        super().__init__(url)
        self.engines = Engines(self._join(self.url, 'engines'))


class MOEX(MOEXBase):
    url = 'https://iss.moex.com/iss'

    def __init__(self):
        super().__init__(self.url)
        self.engines = Engines(self._join(self.url, 'engines'))
        self.history = History(self._join(self.url, 'history'))

    def index(self, return_type='json'):
        url = self._join(self.url, f'index.{return_type}')
        return self._make_request(url)


if __name__ == '__main__':
    moex = MOEX()
    # print(moex.index())
    print(moex.securities())
    print(moex.securities(sid=419728227))
    print(moex.engines.securities())
    print(moex.engines.stock.securities())
    print(moex.engines.stock.markets.securities(date='2022-03-12'))
    print(moex.engines.stock.markets.shares.securities())
    print(moex.engines.stock.markets.bonds.boards.securities(sid=12345))
    print(moex.engines.stock.markets.bonds.boards.ocby.securities())
    print(moex.history.engines.stock.markets.bonds.boards.ocby.securities())
    print(moex.history.engines.securities())
    print(moex.history.engines.stock.securities(return_type='xml'))
    print(moex.history.engines.stock.markets.securities())
    print(moex.history.engines.stock.markets.shares.securities(date='2022-03-12'))

