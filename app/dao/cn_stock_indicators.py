from tortoise import Model, fields


class cn_stock_indicators(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    close = fields.FloatField(source_field='close', null=True, description='价格')
    macd = fields.FloatField(source_field='macd', null=True, description='dif')
    macds = fields.FloatField(source_field='macds', null=True, description='macd')
    macdh = fields.FloatField(source_field='macdh', null=True, description='histogram')
    kdjk = fields.FloatField(source_field='kdjk', null=True, description='kdjk')
    kdjd = fields.FloatField(source_field='kdjd', null=True, description='kdjd')
    kdjj = fields.FloatField(source_field='kdjj', null=True, description='kdjj')
    boll_ub = fields.FloatField(source_field='boll_ub', null=True, description='boll上轨')
    boll = fields.FloatField(source_field='boll', null=True, description='boll')
    boll_lb = fields.FloatField(source_field='boll_lb', null=True, description='boll下轨')
    trix = fields.FloatField(source_field='trix', null=True, description='trix')
    trix_20_sma = fields.FloatField(source_field='trix_20_sma', null=True, description='trma')
    tema = fields.FloatField(source_field='tema', null=True, description='tema')
    cr = fields.FloatField(source_field='cr', null=True, description='cr')
    cr_ma1 = fields.FloatField(source_field='cr_ma1', null=True, description='cr_ma1')
    cr_ma2 = fields.FloatField(source_field='cr_ma2', null=True, description='cr_ma2')
    cr_ma3 = fields.FloatField(source_field='cr_ma3', null=True, description='cr_ma3')
    rsi_6 = fields.FloatField(source_field='rsi_6', null=True, description='rsi_6')
    rsi_12 = fields.FloatField(source_field='rsi_12', null=True, description='rsi_12')
    rsi = fields.FloatField(source_field='rsi', null=True, description='rsi')
    rsi_24 = fields.FloatField(source_field='rsi_24', null=True, description='rsi_24')
    vr = fields.FloatField(source_field='vr', null=True, description='vr')
    vr_6_sma = fields.FloatField(source_field='vr_6_sma', null=True, description='mavr')
    roc = fields.FloatField(source_field='roc', null=True, description='roc')
    rocma = fields.FloatField(source_field='rocma', null=True, description='rocma')
    rocema = fields.FloatField(source_field='rocema', null=True, description='rocema')
    pdi = fields.FloatField(source_field='pdi', null=True, description='pdi')
    mdi = fields.FloatField(source_field='mdi', null=True, description='mdi')
    dx = fields.FloatField(source_field='dx', null=True, description='dx')
    adx = fields.FloatField(source_field='adx', null=True, description='adx')
    adxr = fields.FloatField(source_field='adxr', null=True, description='adxr')
    wr_6 = fields.FloatField(source_field='wr_6', null=True, description='wr_6')
    wr_10 = fields.FloatField(source_field='wr_10', null=True, description='wr_10')
    wr_14 = fields.FloatField(source_field='wr_14', null=True, description='wr_14')
    cci = fields.FloatField(source_field='cci', null=True, description='cci')
    cci_84 = fields.FloatField(source_field='cci_84', null=True, description='cci_84')
    tr = fields.FloatField(source_field='tr', null=True, description='tr')
    atr = fields.FloatField(source_field='atr', null=True, description='atr')
    dma = fields.FloatField(source_field='dma', null=True, description='dma')
    dma_10_sma = fields.FloatField(source_field='dma_10_sma', null=True, description='ama')
    obv = fields.FloatField(source_field='obv', null=True, description='obv')
    sar = fields.FloatField(source_field='sar', null=True, description='sar')
    psy = fields.FloatField(source_field='psy', null=True, description='psy')
    psyma = fields.FloatField(source_field='psyma', null=True, description='psyma')
    br = fields.FloatField(source_field='br', null=True, description='br')
    ar = fields.FloatField(source_field='ar', null=True, description='ar')
    emv = fields.FloatField(source_field='emv', null=True, description='emv')
    emva = fields.FloatField(source_field='emva', null=True, description='emva')
    bias = fields.FloatField(source_field='bias', null=True, description='bias')
    mfi = fields.FloatField(source_field='mfi', null=True, description='mfi')
    mfisma = fields.FloatField(source_field='mfisma', null=True, description='mfisma')
    vwma = fields.FloatField(source_field='vwma', null=True, description='vwma')
    mvwma = fields.FloatField(source_field='mvwma', null=True, description='mvwma')
    ppo = fields.FloatField(source_field='ppo', null=True, description='ppo')
    ppos = fields.FloatField(source_field='ppos', null=True, description='ppos')
    ppoh = fields.FloatField(source_field='ppoh', null=True, description='ppoh')
    wt1 = fields.FloatField(source_field='wt1', null=True, description='wt1')
    wt2 = fields.FloatField(source_field='wt2', null=True, description='wt2')
    supertrend_ub = fields.FloatField(source_field='supertrend_ub', null=True, description='supertrend_ub')
    supertrend = fields.FloatField(source_field='supertrend', null=True, description='supertrend')
    supertrend_lb = fields.FloatField(source_field='supertrend_lb', null=True, description='supertrend_lb')
    dpo = fields.FloatField(source_field='dpo', null=True, description='dpo')
    madpo = fields.FloatField(source_field='madpo', null=True, description='madpo')
    vhf = fields.FloatField(source_field='vhf', null=True, description='vhf')
    rvi = fields.FloatField(source_field='rvi', null=True, description='rvi')
    rvis = fields.FloatField(source_field='rvis', null=True, description='rvis')
    fi = fields.FloatField(source_field='fi', null=True, description='fi')
    force_2 = fields.FloatField(source_field='force_2', null=True, description='force_2')
    force_13 = fields.FloatField(source_field='force_13', null=True, description='force_13')
    ene_ue = fields.FloatField(source_field='ene_ue', null=True, description='ene上轨')
    ene = fields.FloatField(source_field='ene', null=True, description='ene')
    ene_le = fields.FloatField(source_field='ene_le', null=True, description='ene下轨')
    stochrsi_k = fields.FloatField(source_field='stochrsi_k', null=True, description='stochrsi_k')
    stochrsi_d = fields.FloatField(source_field='stochrsi_d', null=True, description='stochrsi_d')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_indicators'
        indexes = ["code"]  # 索引
        table_description = '股票指标数据'
